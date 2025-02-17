from flask import Flask, render_template

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

if __name__ == '__main__':
    app.run(debug=True)
