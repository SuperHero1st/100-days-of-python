from flask import Flask, render_template
import random, requests
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def hello_world():
    random_num = random.randint(1, 10)
    current_year = datetime.now().year
    return render_template("index.html", num=random_num, year = current_year)

@app.route('/guess/<name>')
def guess(name):
    gender_guess = requests.get(f"https://api.genderize.io?name={name}").json()["gender"]
    age_guess = requests.get(f"https://api.agify.io?name={name}").json()["age"]
    return render_template("guess.html", name=name, gender = gender_guess, age = age_guess)

@app.route('/blog')
def get_blog():
    all_posts_response = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
    return render_template("blog.html", posts = all_posts_response)

if __name__ == "__main__":
    app.run(debug=True)