from flask import Flask, request

app = Flask(__name__)

def trans(name):
    import os
    import sys
    import urllib.request
    import json
    textonly = ''
    client_id = "WB4pSWKamy4XCWvxpC7S" # 개발자센터에서 발급받은 Client ID 값
    client_secret = "PRJTYR0NUS" # 개발자센터에서 발급받은 Client Secret 값
    encText = urllib.parse.quote(name)
    data = "source=en&target=ko&text=" + encText
    url = "https://openapi.naver.com/v1/papago/n2mt"
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read().decode('utf-8')
        text = json.loads(response_body)
        textonly = text['message']['result']['translatedText']
    else:
        textonly = "Error Code:" + rescode

  
    return f'''<!doctype html>
    <html>
        <body>
            <h1>{textonly}</h1>
        </body>
    </html>
    '''

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        content = '''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <title></title>
            <meta charset="UTF-8">
        </head>

        <body>
        <h1>what is your name?</h1><br />
        <form action="/" method="POST">
            Your name : 
            <input type="text" name="name">
            <input type="submit" value="trans"></button>
            <h2 id="feedback" style="color:red; display:none">input the your name</h2>
        </form>
        </body>
        </html>
        '''
        return content
    elif request.method == 'POST':
        name = request.form['name']
        return trans(name)

app.run(port=5000, debug=True)