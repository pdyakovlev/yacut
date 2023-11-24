from flask_wtf import FlaskForm
from wtforms import URLField, StringField, SubmitField
from wtforms.validators import DataRequired, Length, URL, Optional, Regexp
from .constants import MIN_SHORT_URL_LEN, MAX_SHORT_URL_LEN


class ShortURLForm(FlaskForm):
    original_link: URLField = URLField(
        'Вставьте URL',
        validators=(
            DataRequired(message='Обязательное поле'),
            URL(require_tld=True, message='Некорректная ссылка')
        )
    )
    custom_id: StringField = StringField(
        validators=(
            Length(MIN_SHORT_URL_LEN, MAX_SHORT_URL_LEN),
            Regexp(
                regex=r'[A-Za-z0-9]+',
                message='В сокращенние присутствуют недопустимые символы'
            ),
            Optional()
        )
    )
    submit: SubmitField = SubmitField('Создать')
