from flask import Flask, request, render_template
from lib.srv import main, main_for_html

APP = Flask(__name__)

def init():
    user_agent = request.headers.get('User-Agent', '').lower()
    if 'curl' in user_agent:
        return main()
    else:
        return render_template('index.html', content=main_for_html())
@APP.route('/')
def home():
    return init()

if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=5001, debug=False)
    APP.debug = True