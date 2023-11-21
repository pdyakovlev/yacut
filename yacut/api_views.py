from flask import jsonify, request

from . import app, db
from .constants import MATCH
from .error_handlers import InvalidAPIUsage
from .models import URLMap
from .utils import get_unique_short_id, check_original


@app.route("/api/id/<string:short_id>/", methods=("GET",))
def get_link(short_id):
    target: str = check_original(short_id)
    if not target:
        raise InvalidAPIUsage('Указанный id не найден', 404)
    return jsonify({"url": target}), 200


@app.route("/api/id/", methods=("POST",))
def push_link():
    data: dict[str, str] = request.get_json()
    if not data:
        raise InvalidAPIUsage('Отсутствует тело запроса')

    elif "url" not in data:
        raise InvalidAPIUsage('"url" является обязательным полем!')

    elif not data.get("custom_id"):
        data.update({"custom_id": get_unique_short_id()})

    elif not MATCH.search(data["custom_id"]):
        raise InvalidAPIUsage('Указано недопустимое имя для короткой ссылки')

    elif check_original(data["custom_id"]):
        raise InvalidAPIUsage('Предложенный вариант короткой ссылки уже существует.')

    short: URLMap = URLMap()
    short.from_dict(data)
    db.session.add(short)
    db.session.commit()
    return jsonify(short.to_dict()), 201
