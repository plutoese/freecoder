from aip import AipNlp

""" 你的 APPID AK SK """
APP_ID = ''
API_KEY = ''
SECRET_KEY = ''

client = AipNlp(APP_ID, API_KEY, SECRET_KEY)

text = "迎难而上前瞻布局  TCL科技储备显示产业新动能"

""" 调用情感倾向分析 """
print(client.sentimentClassify(text))