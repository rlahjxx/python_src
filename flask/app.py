#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask

app = Flask(__name__)

@app.route('/')  # route : 웹서비스를 처음 시작하는 디렉토리
def hello_html():
    return 'Hello Flask !!'

if __name__ == '__main__':
    app.run()

