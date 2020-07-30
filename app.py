from flask import Flask
from flask import send_file
import json
import os
app = Flask(__name__)

@app.route('/')
def index():
    os.remove("items.json")
    os.system("cd quotetutorial")
    os.system('scrapy crawl quotes -o items.json')
    return "<h1>Welcome to our server !!</h1>"

@app.route('/extract/', methods=['POST'])
def respond():
    try:
        os.system('scrapy crawl quotes -o items.json')
        return
    except:
        return
@app.route('/extract/')
def respond2():
    try:
        with open('items.json') as f:
            data = json.load(f)
            print(data)
        return send_file('items.json', attachment_filename='items.json')
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
