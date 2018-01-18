try:
    from .keys import API_ID, API_HASH
except ImportError:
    print('Put API_ID and API_HASH into settings/keys.py')
    print()
    raise IOError('Missing API_ID and API_HASH in settings/keys.py')
