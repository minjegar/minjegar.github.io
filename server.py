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

  
    return textonly


def nav_sty():    
    return '''
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <style>
                body {
                    margin: 0;
                    font-family: Arial, Helvetica, sans-serif;
                }
                .topnav {
                    overflow: hidden;
                    background-color: #333;
                }
                .topnav a {
                    float: left;
                    color: #f2f2f2;
                    text-align: center;
                    padding: 14px 16px;
                    text-decoration: none;
                    font-size: 17px;
                }
                .topnav a:hover {
                    background-color: #ddd;
                    color: black;
                }
                .topnav a.active {
                    background-color: #04AA6D;
                    color: white;
                }
            </style>
        </head>

        <body>


        </body>
        </html>
        '''
  
    

def maker_form():    

    return '''
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <style>
                <!-- Fonts -->
                @import url(//fonts.googleapis.com/earlyaccess/hanna.css);
                @import url(//fonts.googleapis.com/earlyaccess/jejugothic.css);
                @import url(//fonts.googleapis.com/earlyaccess/jejuhallasan.css);
                @import url(//fonts.googleapis.com/earlyaccess/jejumyeongjo.css);
                @import url(//fonts.googleapis.com/earlyaccess/kopubbatang.css);
            </style>
        </head>

        <body>
            <!-- NavBar 해당페이지는 active class를 놓으면 된다.-->
            <div class="topnav">  
                <a href="http://127.0.0.1:5000">Home</a>
                <a class="active" href="http://127.0.0.1:5000/name_maker">name maker</a>
                <a href="http://127.0.0.1:5000/contact">Contact</a>
                <a href="#about">About</a>
            </div>

            <div style="padding-left:16px">
                <h1 style= "text-align:center;">what is your name?</h1><br />
                <form action="/name_maker/" method="POST"><p style= "text-align:center;">
                    Your name : 
                    <input type="text" name="name"><br><br>
                    <label for="fonts">Choose a Font:</label>
                        <select name="font1">
                            <option value="'Hanna', sans-serif" style= "font-size:30px; font-family: 'Hanna', sans-serif"> 안녕하세요. </option>
                            <option value="'Jeju Gothic', sans-serif" style= "font-size:30px; font-family: 'Jeju Gothic', sans-serif"> 안녕하세요.</option>
                            <option value="'Jeju Hallasan', cursive" style= "font-size:30px; font-family: 'Jeju Hallasan', cursive"> 안녕하세요.</option>
                            <option value="'Jeju Myeongjo', serif" style= "font-size:30px; font-family: 'Jeju Myeongjo', serif"> 안녕하세요.</option>
                        </select>
                    <input type="submit" value="trans"></button>
                </p></form>
            </div>
        </body>
        </html>
        '''

@app.route('/')
def index():
    return nav_sty() + """<!DOCTYPE html>
        <html>
        <head>
        <meta charset="UTF-8">
        </head>
        <body>
            <!-- NavBar 해당페이지는 active class를 놓으면 된다.-->
            <div class="topnav">  
                <a class="active" href="http://127.0.0.1:5000">Home</a>
                <a href="http://127.0.0.1:5000/name_maker">name maker</a>
                <a href="http://127.0.0.1:5000/contact">Contact</a>
                <a href="#about">About</a>
            </div>
            <img src="https://cdn.pixabay.com/photo/2016/10/18/21/22/beach-1751455__340.jpg" style="width:100%">
            <p style="padding-left:16px; text-align:center; font-size:50px">안녕하세요. Two-seok's Homepage 입니다.</p>
        </body>
        </html>
    """


@app.route('/name_maker/', methods=['GET', 'POST'])
def name_maker():
    if request.method == 'GET':
        return nav_sty() + maker_form()
    elif request.method == 'POST':
        name = request.form['name']
        font = request.form['font1']        
        return nav_sty() + maker_form() + f"""<!DOCTYPE html>
        <html>
        <head>
        <meta charset="UTF-8">
        <style>
            @import url(//fonts.googleapis.com/earlyaccess/hanna.css);
            @import url(//fonts.googleapis.com/earlyaccess/jejugothic.css);
            @import url(//fonts.googleapis.com/earlyaccess/jejuhallasan.css);
            @import url(//fonts.googleapis.com/earlyaccess/jejumyeongjo.css);
            @import url(//fonts.googleapis.com/earlyaccess/kopubbatang.css);
        </style>
        </head>
        <body>
            <p style= "font-size:30px; font-family: {font}; text-align:center;">당신의 이름은 : {trans(name)}</p>
            <p style= "font-size:30px; font-family: {font}; text-align:center;"><a href = "http://127.0.0.1:5000/name_maker">초기화</a></p>
        </body>
        </html>
        """


@app.route('/contact/')
def contact():
    return nav_sty() + """<!DOCTYPE html>
        <html>
        <head>
        <meta charset="UTF-8">
        </head>
        <body>
            <!-- NavBar 해당페이지는 active class를 놓으면 된다.-->
            <div class="topnav">  
                <a href="#http://127.0.0.1:5000">Home</a>
                <a href="http://127.0.0.1:5000/name_maker">name maker</a>
                <a class="active" href="http://127.0.0.1:5000/contact">Contact</a>
                <a href="#about">About</a>
            </div>
            <p style="padding-left:16px">빅데이터 분석필요하시면 전화주세요.</p>
        </body>
        </html>
    """


app.run(port=5000, debug=True)





