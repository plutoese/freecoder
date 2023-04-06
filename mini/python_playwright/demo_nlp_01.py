from aip import AipNlp

""" 你的 APPID AK SK """
APP_ID = '你的 App ID'
API_KEY = '你的 Api Key'
SECRET_KEY = '你的 Secret Key'

client = AipNlp("", "", "")

text = "苹果是一家伟大的公司"

""" 调用情感倾向分析 """
print(client.sentimentClassify(text))