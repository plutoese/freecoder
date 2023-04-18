from aip import AipNlp
import configparser

config = configparser.ConfigParser()
config.read('D:/backup/configuration/baidunlp/nlp.ini')

""" 你的 APPID AK SK """
APP_ID = config['nlpapp']['APP_ID']
API_KEY = config['nlpapp']['API_KEY']
SECRET_KEY = config['nlpapp']['SECRET_KEY']

client = AipNlp(APP_ID, API_KEY, SECRET_KEY)

text = "不开心"

""" 调用情感倾向分析 """
result = client.sentimentClassify(text)
print(result["items"][0]["confidence"], result["items"][0]["sentiment"])