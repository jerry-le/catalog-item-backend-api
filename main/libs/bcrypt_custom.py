# -*- coding: utf-8 -*-
from sys import version_info

import bcrypt
from werkzeug.security import safe_str_cmp

PY3 = version_info[0] >= 3


def generate_password_hash(password, rounds=12):
    """Generates a password hash and password salt using bcrypt. Specifying
    `rounds` sets the log_rounds parameter of `bcrypt.gensalt()` which
    determines the complexity of the salt. 12 is the default value.

    Example usage of :class:`generate_password_hash` might look something
    like this::

        pw_hash, pw_salt = bcrypt.generate_password_hash('secret', 10)

    :param password: The password to be hashed.
    :param rounds: The optional number of rounds.
    """

    if not password:
        raise ValueError('Password must be non-empty.')

    # Python 3 unicode strings must be encoded as bytes before hashing.
    if PY3 and isinstance(password, str):
        password = bytes(password, 'utf-8')

    if not PY3 and isinstance(password, unicode):
        password = password.encode('utf-8')

    salt = bcrypt.gensalt(rounds)

    return bcrypt.hashpw(password, salt), salt


def check_password_hash(pw_hash, pw_salt, value):
    """Tests a password hash against a candidate password. The candidate
    password is first hashed and then subsequently compared in constant
    time to the existing hash. This will either return `True` or `False`.

    Example usage of :class:`check_password_hash` would look something
    like this::

        pw_hash = bcrypt.generate_password_hash('secret', 10)
        bcrypt.check_password_hash(pw_hash, 'secret') # returns True

    :param pw_salt: The salt
    :param pw_hash: The hash to be compared against.
    :param value: The password to compare.
    """

    # Python 3 unicode strings must be encoded as bytes before hashing.
    if PY3 and isinstance(pw_hash, str):
        pw_hash = bytes(pw_hash, 'utf-8')

    if PY3 and isinstance(pw_salt, str):
        pw_salt = bytes(pw_salt, 'utf-8')

    if PY3 and isinstance(value, str):
        value = bytes(value, 'utf-8')

    # Python 2 unicode strings must be decoded as str
    if not PY3 and isinstance(pw_hash, unicode):
        pw_hash = pw_hash.encode('utf-8')

    if not PY3 and isinstance(pw_salt, unicode):
        pw_salt = pw_salt.encode('utf-8')

    if not PY3 and isinstance(value, unicode):
        value = value.encode('utf-8')

    return safe_str_cmp(bcrypt.hashpw(value, pw_salt), pw_hash)
