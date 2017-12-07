# -*- coding: utf-8 -*-
# 日本語を使う場合は絶対に必要

# flaskなどの必要なライブラリをインポート
import os
from flask import Flask
import json
import apiai

# 自分の名称を app という名前でインスタンス化
app = Flask(__name__)
CLIENT_ACCESS_TOKEN = '4aeaa4b06488499693d12e4987c081c6'

@app.route('/')
def index():
    return 'Hello World!'


def main():
    ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)

    request = ai.text_request()

    request.lang = 'ja'  # optional, default value equal 'en'

    request.session_id = '<SESSION ID, UNIQUE FOR EACH USER>'

    request.query = u'味噌ラーメンをお願いします。'

    response = request.getresponse()

    print (response.read())

# bashで叩いたかimportで入れたかを判定する
if __name__ == '__main__':
    app.run()
