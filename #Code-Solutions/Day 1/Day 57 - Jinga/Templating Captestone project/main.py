from flask import Flask, render_template
import requests
from post import Post

app = Flask(__name__)

@app.route('/')
def home():
    blog_posts_response = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
    return render_template("index.html", posts=blog_posts_response)

@app.route('/post/<num>')
def get_post(num):
    blog_posts_response = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
    blog_post_index = int(num) -1
    return render_template("post.html", post = Post(blog_posts_response[blog_post_index]))



if __name__ == "__main__":
    app.run(debug=True)
