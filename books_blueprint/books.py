from flask import Blueprint, render_template, url_for


books_blueprint = Blueprint(
    'books_bp', __name__
)


@books_blueprint.route('/')
def home():
    return render_template(
        'home.html'
    )

@books_blueprint.route('/book')
def list_book():
    return render_template(
        'simple_book.html',
        book=some_book
    )