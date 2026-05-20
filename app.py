from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_URL = "https://api.quotable.io/random"

@app.route('/', methods=['GET', 'POST'])
def home():
    bot_reply = ""

    if request.method == 'POST':
        user_message = request.form['message']

        response = requests.get(API_URL,verify=False)

        if response.status_code == 200:
            data = response.json()
            bot_reply = data['content']
        else:
            bot_reply = "Sorry, API error!"

    return render_template('index.html', reply=bot_reply)

if __name__ == '__main__':
    app.run(debug=True)