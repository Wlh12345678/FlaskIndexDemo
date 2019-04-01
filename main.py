from flask import Flask,render_template,request,redirect,make_response
from FlaskIndexDemo.orm import manage
import datetime
app = Flask(__name__)
# 缓存一秒刷新一次
app.send_file_max_age_default = datetime.timedelta(seconds = 1)
# 将http://127.0.0.01:5000/和index视图函数绑定
@app.route("/")
def index():
    # return "<h1>hellozwx</h1>"
    # 请求数据库
    user = None
    user = request.cookies.get("username")
    return render_template("index.html", userinfo=user)


@app.route("/regist",methods=["GET", "POST"])
def regist():
    if request.method == "GET":
        args = request.args
        name = args.get("name")
        value1 = args.get("value1")
        print(name,value1)
        return render_template("regist.html")
    elif request.method == "POST":
        username = request.form["username"]
        password = request.form["pwd"]
        print(username, password)
        print("收到post请求，可以提取表单参数")
        # 重定向
        try:
            manage.insterUser(username, password)
            return redirect("/login")
        except:
            redirect("/regist")

@app.route("/login", methods = ["GET","POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        try:
            username = request.form["username"]
            password = request.form["password"]
            result = manage.checkUser(username, password)
            res = make_response(redirect('/list'))
            res.set_cookie(key="username", value=str(result), expires=datetime.datetime.now() + datetime.timedelta(days=7))
            return res
        except:
            return redirect("/login")


@app.route("/list")
def list():
    # 请求数据库
    xh = manage.checkList()
    return render_template("list.html", liebiao=xh)

@app.route("/add",methods=["GET","POST"])
def add():
    if request.method == "GET":
        return render_template("add.html")
    elif request.method == "POST":
        name = request.form["name"]
        detail = request.form["detail"]
        print("收到post请求，可以提取表单参数")
        # 重定向
        try:
            manage.insterList(name, detail)
            return redirect("/list")
        except:
            return redirect("/add")



@app.route("/detail/<id>")
def detail(id):
    # 请求数据库
    res = manage.checkDetail(id)
    return render_template("detail.html",detail_list = res)



@app.route("/quit")
def quit():
    res = make_response(redirect('/'))
    res.delete_cookie('username')
    return res

if __name__ == "__main__":
    app.run(host="192.168.12.154",port=8888)
    # app.run()

