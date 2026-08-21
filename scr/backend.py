from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('body.html')

# ВОТ ЭТИ СТРОЧКИ ОБЯЗАТЕЛЬНЫ ДЛЯ ЗАПУСКА СЕРВЕРА:
if __name__ == '__main__':
    app.run(debug=True)