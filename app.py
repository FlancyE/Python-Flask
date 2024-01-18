from flask import Flask
app=Flask(__name__)     #建立 Application 物件

#建立網站首頁回應的方式
@app.route("/")     
def index():    #用來回應網站首頁連線的函式
    return "Hello Flask"    #回傳網站首頁的內容

#啟動網站伺服器
app.run(port=3000)  # 可以使用 port 參數去指定埠號