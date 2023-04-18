import time
import configparser
import pandas as pd
from aip import AipNlp
from pathlib import Path

config = configparser.ConfigParser()
config.read('D:/backup/configuration/baidunlp/nlp.ini')

""" 你的 APPID AK SK """
APP_ID = config['nlpapp']['APP_ID']
API_KEY = config['nlpapp']['API_KEY']
SECRET_KEY = config['nlpapp']['SECRET_KEY']

client = AipNlp(APP_ID, API_KEY, SECRET_KEY)

print(Path(__file__))
rdata = pd.read_excel(Path(__file__).parent.joinpath("input/上市企业报纸数据.xls"))

i = 1
confidences = list()
sentiments = list()
for item in rdata["title"].values:
    print(f"{i} => {item}")
    try:
        result = client.sentimentClassify(item)
        confidence, sentiment = result["items"][0]["confidence"], result["items"][0]["sentiment"]
        confidences.append(confidence)
        sentiments.append(sentiment)
    except:
        confidences.append(None)
        sentiments.append(None)
    time.sleep(0.1)

rdata["confidence"] = confidences
rdata["sentiment"] = sentiments
rdata.to_excel(Path(__file__).parent.joinpath("output/上市企业报纸数据情感分析.xls"))