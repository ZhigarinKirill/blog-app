from flask import Blueprint, request, render_template, redirect, url_for
from forms import CreationForm
from models import Post


index_pages = Blueprint('', __name__)


@index_pages.route("/", methods=['GET'])
def home():
    return render_template('home.html')


@index_pages.route("/about", methods=['GET'])
def about():
    return render_template('about.html')
