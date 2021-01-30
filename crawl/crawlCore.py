#coding=utf-8
import requests
import json
from crawl import crawlException
url  = "http://qackqi.cn/OnlineCourseBot/topic"
headers = {
                'Content-type': 'application/x-www-form-urlencoded'
            }
class Crawl:
    def __init__(self, question, token = "") -> None:
        self.data = {
            "q":question,
            "token":token
        }
        

    def get_answer(self):
        try:
            self.response = requests.post(url=url, headers = headers, data=self.data)
            if (self.response.status_code == 200):
                
                return self.response.content
            else:
                raise crawlException.ParameterError("参数错误,连接失败...")
        except:
            raise crawlException.ServerConnectFailed("服务器故障,连接失败...")
    def tidy_answer(self):
        dict_answer = json.loads(self.get_answer().decode())
        if dict_answer["success"] == "true":
            return dict_answer
        else:
            raise crawlException.NoSuchQuestion("找不到这个问题的答案...")


