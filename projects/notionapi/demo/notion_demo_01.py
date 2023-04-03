import os
import requests
import json


class Notion:

    def __init__(self, notion_token="secret_Buv6HYwFmrvP4SUfixhlmV9x5342OBwi3HgXNLay9yU"):
        self.headers = {
            'Notion-Version': '2022-06-28',
            'Authorization': 'Bearer ' + notion_token
        }
        self.base_url = "https://api.notion.com/v1"
    
    def list_users(self):
        url = self.base_url + "/users"
        url = "https://api.notion.com/v1/users?page_size=100"
        response = requests.request("GET", url, headers=self.headers, verify=False)

        return response

notion_con = Notion()
response = notion_con.list_users()
print(response.text)