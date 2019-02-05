import re

from django.core.exceptions import ValidationError

from system.utils import validate_text


def validate_only_letters(value):
    p = re.compile(u"[a-zA-ZñÑáéíóú_ ]+$")
    m = p.match(value)
    if not m:
        raise ValidationError(u'Admite solo caracteres alfabéticos.')
    words = validate_text(value)
    if words:
        raise ValidationError(u'Las siguientes palabras no están permitidas: ' + ', '.join(words) + '.')


def validate_only_numbers(value):
    p = re.compile(u"[0-9]+$")
    m = p.match(str(value))
    if not m:
        raise ValidationError(u'Introduzca un valor numérico.')


def validate_only_letters_numbers(value):
    p = re.compile(u"[a-zA-ZñÑáéíóú0-9_ ]+$")
    m = p.match(value)
    if not m:
        raise ValidationError(u'Admite solo caracteres alfanuméricos.')
    words = validate_text(value)
    if words:
        raise ValidationError(u'Las siguientes palabras no están permitidas: ' + ', '.join(words) + '.')


def validate_expression(expression):
    def innerfn(value):
        p = re.compile(u"" + expression + "$")
        m = p.match(value)
        if not m:
            raise ValidationError(u'Ajústese al siguiente formato: ' + expression)

    return innerfn


def validate(value):
    words = validate_text(value)
    if words:
        raise ValidationError(u'Las siguientes palabras no están permitidas: ' + ', '.join(words) + '.')
