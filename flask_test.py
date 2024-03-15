import pandas as pd
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def start():
    return render_template("index.html")

@app.route("/currency")
def currency():
    currency1 = request.args.get("currency1", "USD")
    currency2 = request.args.get("currency2", "EUR")
    rate = float(request.args.get("rate", "0.9635"))

    table1 = []
    for x in range(1, 50):
        table1.append((x, round(x * rate, 2)))

    table2 = []
    for x in range(1, 50):
        table2.append((x, round(x / rate, 2)))

    return render_template("currency.html",
                           rate=rate,
                           currency1=currency1,
                           currency2=currency2,
                           table1=table1,
                           table2=table2
                           )

if __name__ == "__main__":
    app.run(port=1338, debug=True, threaded=True) 