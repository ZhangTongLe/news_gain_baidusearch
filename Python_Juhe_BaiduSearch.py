# 传进百度搜索的新闻到mongoDB数据库，数据库名为：TestSinoMo，表名为：'_' + word_list + '_Baidu_News'
# # @zf - 2017.9.8
# __coding:utf-8__
# python version：3.5
# author:sharpdeep
import re
import urllib

import pymongo
import requests
from bs4 import BeautifulSoup as BS
# import sys
# reload(sys)
# sys.setdefaultencoding("utf-8")
from flask import Flask, jsonify, request

import Clean_NewsTitle
import CH_Change_pin
import Deal_Html_Text_p
# Search_N = Flask(__name__)
# @Search_N.route('/<company>/Search_News/',methods={"POST","GET"})
import URL_ProfilePageText

app = Flask(__name__)
from flask_cors import CORS  # 提供给前端显示的数据接口会遇到跨域问题,需要导入flask_cors

CORS(app, supports_credentials=True)


@app.route('/health')
def helthe():
    return jsonify('Program Is Ready !')


@app.route('/eTensor/crawl/BaiDuSearchNews', methods={'POST'})
def Search_News():
    word_list = request.form.get('comp')
    word = request.form.get('wordKey')
    pages = request.form.get('pages')
    try:
        n = 0
        try:
            word_list = word_list.replace('-', '').replace(' ', '')
            if "公司" in word_list:
                word_list = re.findall('(.+?)公司', word_list, re.S)
                word_list[0] = word_list[0] + "公司"
                word_list = str(word_list[0])
            else:
                word_list = word_list[0:15]
                # print(wordlist[0] + '            das')
        except Exception as e:
            print(str(e))
        # print(wordlist + '            123')
        # data_cdv = pd.DataFrame(
        #     columns=['id', 'Company_Name', 'New_URL', 'News_Soure', 'News_Time', 'News_Title', 'New_Details', 'News_HTML'])

        baseUrl = 'http://news.baidu.com/ns'
        for page in range(1, int(pages) + 1):
            conn = pymongo.MongoClient('172.25.254.17:27017', 27017)
            # conn = pymongo.MongoClient('localhost:27017', 27017)
            # conn = pymongo.MongoClient(host='localhost', port=27017)
            db = conn['eTensorDB']
            # print(word_list)
            try:
                word = CH_Change_pin.Change_ToPinYin(word)
            except Exception as e:
                print(str(e) + "转拼音错误！")
                continue
            # print(P_word_list)
            # print(page)
            try:
                _table = db['Company_News_From' + '_KeyWord_' + word]
                This_Count = _table.count()  # 获取最后一条数据的id，向后存放新数据
                print(This_Count)
                # # .sort([("id", 1)])
                # for i_list in _table.find().skip(This_Count - 1).limit(1):
                #     # print(i_list)
                #     n = i_list["id"] + 1
                #     # print(n)
            except Exception as e:
                print(str(e))
                if This_Count != 0:
                    continue
            data = {'word': word_list, 'pn=': str(page - 1) + '0', 'cl': '2', 'ct': '1', 'tn': 'news', 'rn': '20',
                    'ie': 'utf-8', 'bt': 0, 'et': 0}
            data = urllib.parse.urlencode(data)
            # print(data)
            url = baseUrl + '?' + data
            print(url)
            # n = _table.find().count()
            try:
                html = requests.get(url)  # 获取网页
                html = html.text
                # html = urlopen(url)
                # print(html.read())
            except:
                continue
            # div = soup.find_all(class_='c-title')
            # div_str = html.find_all('div', class_='result')  # 查找属性是result"的div
            div_list = re.findall('<div class="result"(.+?)百度快照</a>', html, re.S)  # 获取百度中的一个新闻篇幅

            for list_1 in div_list:
                data_cdv = {}
                # break
                try:
                    list_URL = "<div class=\"result\"" + str(list_1) + "百度快照</a></span></div></div>"
                    list_URL = re.findall('http://[^\s]*?"', list_URL, re.S)
                    list_Soure_and_Time = re.findall('<p class="c-author">(.+?)</p>', list_1, re.S)
                    list_Soure_and_Time = str(list_Soure_and_Time[0])
                    list_Soure_and_Time = list_Soure_and_Time.split("&nbsp;")
                    # print(list_Soure_and_Time[2])
                    list_1 = list_1.replace(' ', '').replace('\n', '')
                    # print(list_1)
                    list_Title1 = re.findall('target="_blank">(.+?)</a>', list_1, re.S)
                    # print(list_Title1)
                    list_Title1 = str(list_Title1[0].replace('<em>', '').replace('</em>', ''))
                    # print(list_Title1)
                    # print(list_Title1[3:8])
                    results = _table.find_one(
                        {'News_Title': {'$regex': '^(.*?)' + list_Title1[3:8] + '(.*)'}})  # 用正则表达式判断title是否在mongoDB中
                    # print(results)
                    if results == None:
                        # for post in results:
                        # print("*****************************")
                        list_Details1 = re.findall('</p>(.+?)<spanclass="c-info"', list_1, re.S)
                        # print(list_1)
                        list_Details1 = str(list_Details1[0].replace('<em>', '').replace('</em>', ''))
                        # print(str(list_Details1))
                        list_URL = str(list_URL[0])
                        list_URL = list_URL.replace('[\'', '').replace('\"', '').replace('\']', '')
                        # print(list_URL)
                        News_HTML = URL_ProfilePageText.DetailsPage(list_URL)
                        soup = BS(News_HTML, 'html.parser')
                        list_Title2 = soup.find('title' or 'TITLE').text
                        list_Title2 = Clean_NewsTitle.clean_titles(list_Title2)  # 清理title
                        if list_Title2 == 0 or list_Title2 == "0" or "服务器" in list_Title2 or "安全检查" in list_Title2:  # # 当 检查出title有问题时，自动略过此网站
                            continue
                        # print(title)
                        # data_cdv["id"] = n
                        # data_cdv = {"id": n,
                        #             "Company_Name": word_list,
                        #             "New_URL": list_URL,
                        #             "News_Soure": list_Soure_and_Time[0],
                        #             "News_Time": list_Soure_and_Time[2],
                        #             "News_Title": list_Title1,
                        #             "News_HTML": News_HTML,
                        #             "New_Details": list_Details1
                        #             }
                        # data_cdv["id"] = n
                        data_cdv["Company_Name"] = word_list
                        data_cdv["New_URL"] = list_URL
                        data_cdv["News_Soure"] = list_Soure_and_Time[0]
                        data_cdv["News_Time"] = list_Soure_and_Time[2]
                        if list_Title2 is not None:
                            data_cdv["News_Title"] = list_Title2
                        else:
                            data_cdv["News_Title"] = list_Title1
                        # data_cdv["News_Title"] = list_Title1
                        data_cdv["News_HTML"] = News_HTML
                        list_Details2 = Deal_Html_Text_p.deal_html(News_HTML)
                        if list_Details2 is not None:
                            data_cdv["News_Details"] = list_Details2
                        else:
                            data_cdv["News_Details"] = list_Details1
                        data_cdv["Table_Souse"] = "百度搜索"
                        data_cdv["News_Classification"] = "企业新闻"
                        print(data_cdv)
                        try:
                            _table.insert(data_cdv)
                        except Exception as e:
                            print(str(e) + '储存失败')
                        # print(word_list)
                        # _table.update_one({"News_Title": list_Title1}, {'$set': {"News_Title": list_Title2}})
                        n = n + 1
                    else:
                        print("重复")
                        continue
                except Exception as e:
                    list_Title2 = list_Title1
                    print(str(e) + "获取失败")
                    continue
                    # print(data_cdv[0:3])
                    # dict = []
                    # dict.append()
                    # qwe = data_cdv.to_dict(orient="index")
                    # print(qwe)
                    # _table.update_many(qwe)
        return "true"
    except Exception as e:
        return "本次循环结束"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    # Search_N.run(host='localhost',port=8080)
    # Search_News('芜湖造船厂', "造船厂")
