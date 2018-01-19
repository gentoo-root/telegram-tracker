telegram-tracker
================

This script allows to track your friend's online status changes.

Example output:

    =2018-01-19 @ 00:48:23: User went offline.
    ~2018-01-19 @ 01:46:18: User went online.
    =2018-01-19 @ 01:46:29: User went offline.
    =2018-01-19 @ 01:46:39: User went offline after being online for short time.

= means that the time is exact as returned by the Telegram server, and ~ means that the time is measured locally and can be inexact.

How to run
----------

First install the dependencies. You'll need Python 3 (at least 3.6) and [Telethon](https://github.com/LonamiWebs/Telethon) package.

Telethon can be installed with pip:

    $ pip install --user telethon

...or possibly from your distribution repositories.

To begin tracking someone, start the script like this (the current working directory needs to be this repository root):

    $ python3 -m track '+380991234567'

Use the real phone number or a nickname. The special string "me" can be used to track yourself (it can be useful if e.g. you suffer from [dissociative identity disorder](https://en.wikipedia.org/wiki/Dissociative_identity_disorder) or if you're just doing some testing).

How it works
------------

The script polls the user status every 15 seconds. If the status switches to online, it can't determine the exact time of the transition and shows the time when it found out this information. On the other hand, offline transitions are measured exactly as the Telegram server returns the exact time of going offline. The script may not detect short (less than 15 seconds) transitions to offline and back online. It can, however, detect that the user was online for short time (last online time returned by the server changes).

License
-------

The software is licensed under MIT License. The full text and the copyright notice is in LICENSE file.

Copyright (c) 2018 Maxim Mikityanskiy
