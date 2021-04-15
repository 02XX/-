#coding=utf-8
import requests
import json
# from need.crawl import crawlException
url  = "http://imnu.52king.cn/api/wk/index.php"
headers = {
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36 Edg/88.0.705.81",
                'Content-type': 'application/x-www-form-urlencoded'
            }
class Crawl:
    def __init__(self, question) -> None:
        self.param = {
            "c":question,
        }
        

    def get_answer(self):
        try:
            self.response = requests.get(url=url, params=self.param,headers=headers)
            if (self.response.status_code == 200):
                
                return self.response.content
            else:
                raise crawlException.ParameterError("参数错误,连接失败...")
        except:
            raise crawlException.ServerConnectFailed("服务器故障,连接失败...")
    def tidy_answer(self):
        dict_answer = json.loads(self.get_answer().decode())
        if dict_answer["code"] == 0:
            return {"question":dict_answer["title"], "answer": dict_answer["answer"]}
        else:
            raise crawlException.NoSuchQuestion("找不到这个问题的答案...")


