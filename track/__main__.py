# telegram-tracker
# Copyright (c) 2018 Maxim Mikityanskiy
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from datetime import datetime
from settings import API_ID, API_HASH
from sys import argv, exit
from telethon import TelegramClient
from telethon.tl.types import UserStatusOnline, UserStatusOffline
from time import mktime, sleep


DATETIME_FORMAT = '%Y-%m-%d @ %H:%M:%S'


def utc2localtime(utc):
    pivot = mktime(utc.timetuple())
    offset = datetime.fromtimestamp(pivot) - datetime.utcfromtimestamp(pivot)
    return utc + offset


if len(argv) < 2:
    print(f'usage: {argv[0]} <contact id>')
    exit(1)
contact_id = argv[1]

client = TelegramClient('tracker', API_ID, API_HASH)
client.start()

online = None
last_offline = None
while True:
    contact = client.get_entity(contact_id)
    if isinstance(contact.status, UserStatusOffline):
        if online != False:
            online = False
            print(f'={utc2localtime(contact.status.was_online).strftime(DATETIME_FORMAT)}: User went offline.')
        elif last_offline != contact.status.was_online:
            if last_offline is not None:
                print(f'={utc2localtime(contact.status.was_online).strftime(DATETIME_FORMAT)}: User went offline after being online for short time.')
            else:
                print(f'={utc2localtime(contact.status.was_online).strftime(DATETIME_FORMAT)}: User went offline.')
        last_offline = contact.status.was_online
    elif isinstance(contact.status, UserStatusOnline):
        if online != True:
            online = True
            print(f'~{datetime.now().strftime(DATETIME_FORMAT)}: User went online.')
    else:
        if online != False:
            online = False
            print(f'~{datetime.now().strftime(DATETIME_FORMAT)}: User went offline.')
        last_offline = None
    sleep(15)
