from flask import flash, render_template, redirect, url_for

from . import app, db
from .forms import ShortURLForm
from .models import URLMap
from .utils import get_unique_short_id, check_original


@app.route('/', methods=('GET', 'POST'))
def generate_url_page():
    form: ShortURLForm = ShortURLForm()
    if form.validate_on_submit():
        url: str = form.custom_id.data
        if not url or len(url) == 0 or url is None:
            url: str = get_unique_short_id()
        if check_original(url):
            flash('Предложенный вариант короткой ссылки уже существует.', category='fail')
        else:
            shorturl: URLMap = URLMap(
                original=form.original_link.data,
                short=url
            )
            db.session.add(shorturl)
            db.session.commit()
            flash(url_for('short_url', short=url, _external=True), 'link')
    return render_template('index.html', form=form)


@app.route('/<string:short>', methods=('GET',))
def short_url(short):
    return redirect(
        URLMap.query.filter_by(short=short).first_or_404().original
    )
