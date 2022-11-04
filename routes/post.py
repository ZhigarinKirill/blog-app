from flask import Blueprint, request, render_template, redirect, url_for
from forms import CreationForm
from models import Post


post_pages = Blueprint('posts', __name__)


# @post_pages.route("/", methods=['GET'])
# def home():
#     return render_template('home.html')


@post_pages.route("/", methods=['GET'])
def display_posts():
    author = request.args.get('author')
    if author is not None:
        posts = Post.objects(author='a1').first()
        return posts.author
    else:
        posts = Post.objects
    return render_template('post.html', posts=posts)


@ post_pages.route("/create", methods=['GET', 'POST'])
def create_post():
    form = CreationForm(request.form)
    if request.method == 'POST':
        post = Post(title=form.title.data, content=form.content.data,
                    publish_date=form.publish_date.data, author=form.author.data)
        post.save()
        return redirect(url_for('posts.display_posts'))
    return render_template('post_creating.html', form=form)
