import flask
from flask import Blueprint, render_template, url_for, request
import library.adapters.repository as repo
from library.domain.model import Book
books_blueprint = Blueprint(
    'books_bp', __name__
)


@books_blueprint.route('/')
def home():
    return render_template(
        'home.html',
        home_url = url_for('books_bp.home'),
        list_url = url_for('books_bp.list_book'),
        book_url = url_for('books_bp.book_info')
    )

@books_blueprint.route('/book')
def list_book():
    return render_template(
        'list_of_book.html',
        books = repo.repo_instance,
        home_url = url_for('books_bp.home'),
        list_url = url_for('books_bp.list_book'),
        book_url=url_for('books_bp.book_info')
    )
@books_blueprint.route('/book_info', methods=['GET'])
def book_info():
    book_id = int(request.args.get('book_id'))
    return render_template(
        'book_info.html',
        book = repo.repo_instance.get_book(book_id),
        home_url = url_for('books_bp.home'),
        list_url = url_for('books_bp.list_book'),
        book_url=url_for('books_bp.book_info')
    )

