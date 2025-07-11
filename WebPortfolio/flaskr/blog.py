from flask import (
    Blueprint, flash, g, redirect, render_template, session, request, url_for, current_app
)
from werkzeug.exceptions import abort
from werkzeug.utils import secure_filename
from flaskr.auth import login_required
from flaskr.db import get_db
import os
from io import BytesIO

bp = Blueprint('blog', __name__)


def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}


def get_post(id, check_author=True):
    db = get_db()
    post = db.execute(
        'SELECT p.id, title, body, created, author_id, username'
        ' FROM post p JOIN user u on p.author_id = u.id'
        ' WHERE p.id = ?',
        (id,)
    ).fetchone()

    if post is None:
        abort(404, f"Post id {id} doesn´t exist.")

    if check_author and post['author_id'] != g.user['id']:
        abort(403)
    return post


def get_image(post_id):
    """Fetches image BLOB from database by ID"""
    db = get_db()
    data = db.execute("SELECT bytes FROM post_images WHERE post_id =?", (post_id,)).fetchone()
    print(data)
    if data:
        return data[0]
    return None


@bp.route('/')
def index():
    db = get_db()
    posts = db.execute(
        'SELECT p.id, title, body, created, author_id, username, img_path, img_path'
        ' FROM post p '
        'JOIN user u ON p.author_id = u.id'
        ' ORDER BY created DESC'
    ).fetchall()

    return render_template('blog/index.html', posts=posts,)


@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            cursor = db.cursor()
            if 'image_file' in request.files:
                file = request.files['image_file']
                filename = secure_filename(file.filename)
                filepath = os.path.join(current_app.config["UPLOAD_FOLDER"], filename)
                file.save(filepath)
                cursor.execute(
                    'INSERT INTO post (title, body, author_id, img_path)'
                    ' VALUES (?, ?, ?, ?)',
                    (title, body, g.user['id'], f'Images/{filename}')
                )
            else:
                cursor.execute(
                    'INSERT INTO post (title, body, author_id)'
                    ' VALUES (?, ?, ?, ?)',
                    (title, body, g.user['id'])
                )

            db.commit()

            return redirect(url_for('blog.index'))
    return render_template('blog/create.html')


@bp.route('/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):
    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            print('nao entrei')

            if 'image_file' in request.files:
                print('entrei')
                existing_image = db.execute('SELECT img_path FROM post WHERE id = ?',
                    (id, )
                ).fetchone()
                hallow = str(existing_image['img_path']).replace("Images/", "")
                print(hallow)
                pathito = str(os.path.join(current_app.config["UPLOAD_FOLDER"], hallow)).replace("\\", "/")
                os.remove(pathito)

                file = request.files['image_file']
                filename = secure_filename(file.filename)
                filepath = os.path.join(current_app.config["UPLOAD_FOLDER"], filename)
                file.save(filepath)
                db.execute(
                    'UPDATE post SET title = ?, body = ?, img_path = ?'
                    'WHERE id = ?',
                    (title, body, f'Images/{filename}', id)
                )
            else:
                db.execute(
                    'UPDATE post SET title = ?, body = ?'
                    'WHERE id = ?',
                    (title, body, id)
                )

            db.commit()
            return redirect(url_for('blog.index'))
    return render_template('blog/update.html', post=post)


@bp.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    get_post(id)
    db = get_db()
    db.execute('DELETE FROM post WHERE id = ?', (id,))
    db.commit()
    return redirect(url_for('blog.index'))
