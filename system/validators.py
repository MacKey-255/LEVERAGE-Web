import re

from django.core.exceptions import ValidationError

from system.utils import validate_text


def validate_only_letters(value):
    p = re.compile(u"[a-zA-Z�������_ ]+$")
    m = p.match(value)
    if not m:
        raise ValidationError(u'Admite solo caracteres alfab�ticos.')
    words = validate_text(value)
    if words:
        raise ValidationError(u'Las siguientes palabras no est�n permitidas: ' + ', '.join(words) + '.')


def validate_only_numbers(value):
    p = re.compile(u"[0-9]+$")
    m = p.match(str(value))
    if not m:
        raise ValidationError(u'Introduzca un valor num�rico.')


def validate_only_letters_numbers(value):
    p = re.compile(u"[a-zA-Z�������0-9_ ]+$")
    m = p.match(value)
    if not m:
        raise ValidationError(u'Admite solo caracteres alfanum�ricos.')
    words = validate_text(value)
    if words:
        raise ValidationError(u'Las siguientes palabras no est�n permitidas: ' + ', '.join(words) + '.')


def validate_expression(expression):
    def innerfn(value):
        p = re.compile(u"" + expression + "$")
        m = p.match(value)
        if not m:
            raise ValidationError(u'Aj�stese al siguiente formato: ' + expression)

    return innerfn


def validate(value):
    words = validate_text(value)
    if words:
        raise ValidationError(u'Las siguientes palabras no est�n permitidas: ' + ', '.join(words) + '.')
