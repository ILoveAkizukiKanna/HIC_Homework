import time
import json
from flask_cors import *
from flask import Flask, request
from flask import Response

'''
flask： web框架，通过flask提供的装饰器@server.route()将普通函数转换为服务
登录接口，需要传url、username、passwd
'''

# 创建Flask对象app并初始化，把当前这个python文件当做一个服务
app = Flask(__name__)
CORS(app, supports_credentials=True)


def get_message():
    """this could be any function that blocks until data is ready"""
    time.sleep(1)
    s = time.ctime(time.time())
    return json.dumps(['当前时间：' + s, 'a'], ensure_ascii=False)


@app.route('/capture')
def capture():
    user_id = request.args.get('user_id')
    print(user_id)

    def eventStream():
        id = 0
        while True:
            id += 1
            # wait for source data to be available, then push it

            yield 'id: {} \n event: add \n data: {} \n'.format(id, get_message())
    return Response(eventStream(), mimetype="text/event-stream")


if __name__ == "__main__":
    app.run()
