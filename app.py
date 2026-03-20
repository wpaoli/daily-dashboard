from flask import Flask, render_template
from datetime import date

app = Flask(__name__)


@app.route("/")
def index():
    today = date.today()
    start_of_year = date(today.year, 1, 1)
    day_of_year = (today - start_of_year).days + 1
    days_in_year = 366 if (today.year % 4 == 0 and today.year % 100 != 0) or today.year % 400 == 0 else 365
    days_remaining = days_in_year - day_of_year

    return render_template("index.html",
        full_date=today.strftime("%A, %B %-d, %Y"),
        day_of_year=day_of_year,
        days_remaining=days_remaining,
        year=today.year,
    )


if __name__ == "__main__":
    app.run(debug=True, port=5000)
