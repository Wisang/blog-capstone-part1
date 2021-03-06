import requests
from flask import Flask, render_template
from post import Post


app = Flask(__name__)
response = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

post_list = []

for post in response:
    post_list.append(Post(post["id"], post["title"], post["subtitle"], post["body"]))


@app.route('/')
def get_blog():
    return render_template("index.html", posts=post_list)


@app.route('/post/<int:index>')
def get_post(index):
    # requested_post = None
    # for blog_post in post_list:
    #     if blog_post.id == index:
    #         requested_post = blog_post
    return render_template("post.html", post=post_list[index-1])


if __name__ == "__main__":
    app.run(debug=True)
