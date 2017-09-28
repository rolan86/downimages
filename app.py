import os

from flask import Flask, request, send_from_directory, render_template
#from flask import send_static_file


app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
	files = os.listdir('downloads')
	if not os.path.exists('downloads'):
		files = []
	return render_template('index.html', files=files)
	
@app.route('/downloads/<path:path>')
def send_js(path):
    return send_from_directory('downloads', path)

"""
@app.route('/<path:path>')
def static_file(path):
    return send_static_file(path)
"""

if __name__ == '__main__':
	app.run(host='0.0.0.0')
