from flask import Flask, render_template
import os

app = Flask(__name__, static_folder='static', template_folder='.')

@app.route("/")
def home():
    return render_template('index.html')

if __name__ == "__main__":
    debug = os.environ.get('FLASK_ENV') == 'development'
    app.run(host="0.0.0.0", port=5000, debug=debug)
