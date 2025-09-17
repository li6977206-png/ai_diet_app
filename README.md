# flask_app.py

from flask import Flask, render_template, request

# 创建 Flask 应用实例
app = Flask(__name__)

# 定义一个路由（Route），当用户访问网站根目录 '/' 时触发
@app.route('/')
def hello_world():
    """
    这是首页函数。
    它返回一个简单的字符串作为网页内容。
    """
    return '<h1>Hello from Flask! 这是一个基本的网页。</h1>'

# 定义一个带变量的路由，例如访问 /user/Alice
@app.route('/user/<username>')
def show_user_profile(username):
    """
    根据 URL 中的用户名显示欢迎信息。
    """
    return f'欢迎回来, 用户: {username}!'

# 运行应用
if __name__ == '__main__':
    # debug=True 会在代码更改时自动重启服务器
    # 在生产环境中应该设置为 False
    app.run(debug=True)
