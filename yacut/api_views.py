from http import HTTPStatus

from flask import jsonify, request

from . import app, db
from .constants import MATCH
from .error_handlers import InvalidAPIUsage
from .models import URLMap
from .utils import check_original, get_unique_short_id


@app.route('/api/id/<string:short_id>/', methods=('GET',))
def get_link(short_id):
    """Получает оригинальную ссылку по короткой ссылке."""
    target: str = check_original(short_id)
    if not target:
        raise InvalidAPIUsage('Указанный id не найден', HTTPStatus.NOT_FOUND)
    return jsonify({'url': target}), HTTPStatus.OK


@app.route('/api/id/', methods=('POST',))
def push_link():
    """Создаёт новую ссылку."""
    data: dict[str, str] = request.get_json()
    if not data:
        raise InvalidAPIUsage('Отсутствует тело запроса')

    if 'url' not in data:
        raise InvalidAPIUsage('"url" является обязательным полем!')

    if not data.get('custom_id'):
        data.update({'custom_id': get_unique_short_id()})

    if not MATCH.search(data['custom_id']):
        raise InvalidAPIUsage('Указано недопустимое имя для короткой ссылки')

    if check_original(data['custom_id']):
        raise InvalidAPIUsage('Предложенный вариант короткой ссылки уже существует.')

    short: URLMap = URLMap()
    short.from_dict(data)
    db.session.add(short)
    db.session.commit()
    return jsonify(short.to_dict()), HTTPStatus.CREATED
