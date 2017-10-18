#标题：通过百度新闻引擎查找新闻并处理存储到mongoDB中

>Data:2017-9-12/----10-16改

>Author:zf

##版本V1：（bug简说）
#####1.少数获得的新闻网址进不去的问题

    描述：有些新闻的来源已删除或者原网站已关闭或正在维护中的情况，所以网页进不去
    
解决方案：暂无解决方案

#####2.少数获取的公司名称不规范

    描述：如图所示，原本获取的逛网名称就不太规范，所以搜索新闻时遇到搜索数量少，不相关等问题。
    
![](image/guanwangmingcheng.png)
   
解决方案：暂无解决（可解决）

#####3.在获取关于新闻的题目不太规范
    描述：如图所示获取相关标题时标题会跟一个后缀。
    
   ![](image/xiangguanguanjianzixinwentimu.png)

#####4.新闻新闻详细页面获取不上的问题

     描述：极少部分的新闻详情可进去，但获取不上，一般有两种情况获取不上详情页的信息：
      - 1.详细页面没有成段文字，大多数都是图片构成的新闻。
      - 2.详情页打不开或加载超时。
     
#####解决方案：V2版本加入图片解析识别并获取功能



##功能描述
此项目主要实现如下几点：
 - 1.通过输入的数据库中的官网名称进入百度新闻引擎查找并获得信息，表单如下:
 
    >["id","Company_Name","New_URL","News_Soure","News_Time","News_Title","News_HTML","News_Details","Table_Souse","News_Classification"]
 
 - 2.通过获得的新闻url，进入新闻原网站获得原网站的html
 - 3.对获得的“html”进行处理获取里面的主要信息




# 通过百度新闻引擎查找新闻并处理存储到mongoDB中微服务操作接口

# API Server
#####健康性：

`/health`

#####接口：

`POST`: `/eTensor/crawl/BaiDuSearchNews`

# 日志

使用此接口时，"wordKey"为动态新闻存放表关键词，建议前端后台选择框形式固定

`POST`: 
{	
   "comp":"沪东中华造船集团有限公司"
   "wordKey": '造船 船舶 公司 造船厂'
   "pages":"2"
}

>注：本功能为搜索传进的单个公司，搜索出关于这个公司的新闻，一般"pages"超过 _4_ 就和公司无关

Data:

```data
{                                
    "_id" : ObjectId("59e03ec4a994ab33f82854a5"),
    "Company_Name" : "沪东中华造船集团有限公司",
    "New_URL" : "http://www.huaue.com/mxdt2014/201710892836.htm",
    "News_Soure" : "华禹教育网",
    "News_Time" : "2017年10月08日 09:37",
    "News_Title" : "上海杉达学院校长李进：聚焦高素质应用型人才培养办人民满意的高等教育",
    "News_HTML" : "<html>\n<head>\n<title>上海杉达学院校长李进：聚焦高素质应用型人才培养</body>\n</html>\n",
    "News_Details" : "上海杉达学院建校25年来，稳步推进多科性、国际化、高水平民办应用技术大学建设。",
    "Table_Souse" : "百度搜索",
    "News_Classification" : "企业新闻"
}
```