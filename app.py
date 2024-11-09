from flask import Flask, render_template, request, redirect, url_for
import os
from scripts.downloader import baixar_video

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        format = request.form['format']
        baixar_video(url, format)
        return redirect(url_for('success'))
    return render_template('index.html')

@app.route('/success')
def success():
    return "Download concluído com sucesso! Verifique a pasta de Downloads."

if __name__ == '__main__':
    app.run(debug=True)
