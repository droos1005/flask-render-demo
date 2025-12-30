from flask import Flask
app=Flask(__name__) # __name__代表目前執行的模組

@app.route("/") # 函式的裝飾 (Decotate): 以函式為基礎, 附加提供的功能
def home():
    return "Hello FLask2"

@app.route("/test") # 網址後加上 /test
def test():
    return "This is test"

if __name__=="__main__": # 如果以主程式運作
    app.run() # 立刻啟動伺服器w