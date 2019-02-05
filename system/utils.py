import json
import os
import re

from mine import settings


def get_equivalent_char(char):
    char = str(char).lower()
    if char == '@' or char == '4' or char == 'á':
        return 'a'
    elif char == '3' or char == '€' or char == 'é':
        return 'e'
    elif char == '1' or char == '&' or char == 'í':
        return 'i'
    elif char == '0' or char == 'ó':
        return 'o'
    elif char == 'ú':
        return 'u'
    elif char == '$':
        return 's'
    elif not char.isalpha() and not char.isnumeric():
        return ' '
    else:
        return char


def validate_text(text):
    text = str(text).lower()
    content = open(os.path.join(settings.BASE_DIR, 'system', 'json', 'denied_words.json')).read()
    words = json.loads(content)
    found = []
    new_text = ''
    for char in text:
        new_text += get_equivalent_char(char)
    new_text = re.sub(r'\s\s+', ' ', new_text)
    split = new_text.split(' ')
    for word in split:
        if word in words:
            found.append(word)
    return found
