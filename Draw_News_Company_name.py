# 通过官网循环获取公司title——2017.9.2
# coding=utf-8

import pymongo

import CH_Change_pin


# app = Flask(__name__)


# @app.route('/<word>/get_News', methods={"POST", "GET"})
def Word_FS(word):
    # word = input('输入关键字：')
    # print('在右边的查询格式中选择想要的格式输入：filetype:xls加空格 ，filetype:pdf加空格 ，filetype:ppt加空格，filetype:doc加空格 ，filetype:rtf加空格')
    # bs = input('我的格式是： (可不填)')
    conn = pymongo.MongoClient('172.25.254.17:27017', 27017)
    # db = conn.TestSinoMo

    # conn = pymongo.MongoClient('localhost:27017', 27017)
    # collection = db.word（链接建立数据库方法1）
    db = conn['eTensorDB']
    P_word = CH_Change_pin.Change_ToPinYin(word)
    _table1 = db['Company_News_From_KeyWord_' + P_word]
    _table2 = db['Company_Names_' + P_word]
    # _table2.insert_one({"Company_Name", })
    for text_one in _table1.find():
        data = {}
        Company_Name = text_one["Company_Name"]
        results = _table2.find_one({'Company_Name': {'$regex': Company_Name}})  # 用正则表达式判断title是否在mongoDB中
        # print(results)
        if results is None:
            data["Company_Name"] = Company_Name
            _table2.insert_one(data)
            print(data)
            # Baidu = Python_Juhe_BaiduSearch.Search_News(title, word)
            # _360 = Python_Juhe_360Search.Search_News(title, word)
            # China_New = Python_Juhe_ChinaSearch.Search_News(title, word)
            # print("返回结果：" + Baidu + "..." + _360 + "...")  # + _360 + "..." + China_New


if __name__ == '__main__':
    word = input(":")
    Word_FS(word)
    # app.run(host='localhost', port=8080)
    # for item in db.S1001.find():
    #     print(item)
