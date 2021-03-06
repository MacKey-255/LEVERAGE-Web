import json
import os
import re
import uuid
import time
from datetime import datetime
from django.core.files.storage import FileSystemStorage
from django.utils.functional import cached_property

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


class NULL_NAMESPACE:
    bytes = b''


def getUsernameToUUID(username):
    return str(uuid.uuid3(NULL_NAMESPACE, "OfflinePlayer:" + username))


def generateRandomString():
    return 'arc'


class OverwriteFile(FileSystemStorage):
    def get_available_name(self, name, max_length=None):
        if self.exists(name):
            os.remove(os.path.join(settings.MEDIA_ROOT, name))
        return name

    @cached_property
    def base_url(self):
        if self._base_url is not None and not self._base_url.endswith('/'):
            self._base_url += '/'
        return self._value_or_setting(self._base_url, settings.SKINS_DIRS)

    @cached_property
    def base_location(self):
        return self._value_or_setting(self._location, settings.SKINS_DIRS)


def is_cheat(word):
    word = str(word)
    word_keys = ('xray', 'Xray', 'XRAY', 'Wurst', 'wurst', 'WURST')
    for search in word_keys:
        if word.find(search) != -1:
            return True
    return False


def timestampToDatetime(timestamp):
    return datetime.fromtimestamp(timestamp)


def datetimeToTimestamp(datetime):
    return int(time.mktime(datetime.timetuple()))
