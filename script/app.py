from flask import Flask, render_template, request, send_file
from pytube import YouTube
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    url = request.form['url']
    yt = YouTube(url)

    if request.form['type'] == 'video':
        stream = yt.streams.get_highest_resolution()
    elif request.form['type'] == 'audio':
        stream = yt.streams.filter(only_audio=True).first()

    stream.download(output_path='downloads', filename='downloaded')
    return send_file('downloads/downloaded', as_attachment=True)

@app.errorhandler(405)
def method_not_allowed(e):
    return render_template('405.html'), 405

if __name__ == "__main__":
    if not os.path.exists('downloads'):
        os.makedirs('downloads')
    app.run(debug=True)
