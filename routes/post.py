from datetime import datetime
from flask import Blueprint, request, redirect, url_for, render_template


post_pages = Blueprint('posts', __name__)
