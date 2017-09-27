from flask import Flask, request, send_from_directory


app = Flask(__name__)

@app.route('/index')
def index():
	return "hello"
	
@app.route('/downloads/<path:path>')
def send_js(path):
    return send_from_directory('downloads', path)

if __name__ == '__main__':
	app.run(host='0.0.0.0')
