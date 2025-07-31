from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def index():
    with open('reddit_content_2025-07-31_1557.json') as f:
        posts = json.load(f)
    return render_template('index.html', posts=posts)

if __name__ == '__main__':
    app.run(debug=True)
