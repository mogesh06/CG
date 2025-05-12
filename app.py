from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    target = 7700
    achieved = 6900
    balance = target - achieved
    days_left = 8
    goal_deadline = datetime(2025, 5, 19, 23, 59, 0).isoformat()

    return render_template("index.html",
                           target=target,
                           achieved=achieved,
                           balance=balance,
                           days_left=days_left,
                           goal_deadline=goal_deadline)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
