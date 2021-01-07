import os
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    rave_public_key = os.environ.get('RAVE_PUBLIC_KEY')
    return render_template('homepage.html', rave_public_key=rave_public_key)


if __name__ == '__main__':
    app.run(debug=True)
