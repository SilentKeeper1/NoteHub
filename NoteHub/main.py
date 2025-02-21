import os
import subprocess
from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/python/')
def python_page():
    return render_template('Python.html')

@app.route('/java/')
def java_page():
    return render_template('Java.html')

@app.route('/html/')
def html_page():
    return render_template('html.html')

@app.route('/javascript/')
def javascript_page():
    return render_template('javascript.html')

@app.route('/check/')
def check_server():
    try:
        flask_installed = subprocess.run(["python", "-c", "import flask"], capture_output=True, text=True)
        flask_version = subprocess.run(["python", "-m", "flask", "--version"], capture_output=True, text=True)
        templates_exist = os.path.exists("templates")
        index_exist = os.path.exists("templates/check.html")

        result = "=== Перевірка сервера ===\n"
        result += "Flask встановлено ✅\n" if flask_installed.returncode == 0 else "Flask НЕ встановлено ❌\n"
        result += f"Версія Flask: {flask_version.stdout.strip()}\n" if flask_version.returncode == 0 else "Не вдалося отримати версію Flask ❌\n"
        result += "Папка templates існує ✅\n" if templates_exist else "Папки templates немає ❌\n"
        result += "index.html існує ✅\n" if index_exist else "Файл index.html відсутній ❌\n"


        print(result)

        return jsonify({"status": "ok", "message": "Перевірка виконана! Дивись консоль PyCharm."})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
