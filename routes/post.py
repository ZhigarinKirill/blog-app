from flask import Blueprint, request, render_template, redirect, url_for
from forms import CreationForm
from models import Post


post_pages = Blueprint('posts', __name__)


@post_pages.route("/", methods=['GET'])
def home():
    return render_template('home.html')


@post_pages.route("/posts/", methods=['GET'])
def display_posts():
    author = request.args.get('author') or ''
    posts = Post.objects
    # return posts.title
    return render_template('post.html', author=author, posts=posts)


@post_pages.route("/posts/create", methods=['GET', 'POST'])
def create_post():
    if request.method == 'POST':
        creation_form = CreationForm(request.form)
        post = Post(title=creation_form.title.data, content=creation_form.content.data,
                    publish_date=creation_form.publish_date.data, author=creation_form.author.data)
        post.save()
        return redirect(url_for('posts.display_posts'))
    elif request.method == 'GET':
        return render_template('new_post.html')
