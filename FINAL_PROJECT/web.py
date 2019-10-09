from flask import Flask, render_template, request
import search
app = Flask(__name__)
search.data_base()

@app.route('/', methods=['GET', 'POST'])
def index():
    errors = []
    results = {}
    if request.method == "POST":
        words = request.form['url']
        winner = search.bd_parse(words)
        result = winner
        results.update({result: winner})

    return render_template('index.html', errors=errors, results=results)


if __name__ == '__main__':
    app.run()