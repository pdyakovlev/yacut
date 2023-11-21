from flask_wtf import FlaskForm
from wtforms import URLField, StringField, SubmitField
from wtforms.validators import DataRequired, Length, URL, Optional, Regexp


class ShortURLForm(FlaskForm):
    original_link: URLField = URLField(
        "Вставьте URL",
        validators=(
            DataRequired(message="Обязательное поле"),
            URL(require_tld=True, message="Некорректная ссылка")
        )
    )
    custom_id: StringField = StringField(
        validators=(
            Length(1, 16),
            Regexp(
                regex=r"[A-Za-z0-9]+",
                message="В сокращенние присутствуют недопустимые символы"
            ),
            Optional()
        )
    )
    submit: SubmitField = SubmitField("Создать")
