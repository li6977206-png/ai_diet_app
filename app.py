from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # ✅ 正確地渲染 HTML 模板

@app.route('/recognize', methods=['POST'])
def recognize():
    file = request.files['image']

    # 模擬結果（之後可接模型）
    result = {
        "food_name": "牛肉便當",
        "calories": 700,
        "protein": 25,
        "carbs": 80,
        "fat": 20
    }

    return render_template('index.html', result=result)  # ✅ 把結果傳給模板