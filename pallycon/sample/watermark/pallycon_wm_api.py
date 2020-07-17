import base64
import hashlib
from Crypto.Cipher import AES
import datetime
import json

"""
A simple note how this module works.
0. get `site_id`, `access_key`, `site_key`, and `json_req`
1. encrypt `json_req` with `_make_data()`.
2. make `timestamp` with `_make_timestamp()`.
3. make `hash` with `_make_hash()`.
4. return PallyCon HTTP API specification String
"""

AES_IV = '0123456789abcdef'


def execute(site_id, access_key, site_key, json_req):
    """
    The One And Only function to call.
    Generate an encrypted String for PallyCon Api (a.k.a PallyCon HTTP API specification).

    :Parameters:
      site_id, access_key, site_key :
         can get from the pallycon console - site settings - site credentials
      json_req :
        a json string to request.

    :Return: a String of PallyCon HTTP API specification
    """
    my_data = _make_data(json_req, site_key)
    timestamp = _make_timestamp()
    my_hash = _make_hash(access_key, site_id, my_data, timestamp)

    input_str = {
        "data": my_data,
        "timestamp": timestamp,
        "hash": my_hash
    }
    return base64.b64encode(json.dumps(input_str).encode('utf-8')).decode('utf-8')


def _pad(words):
    BS = 16
    return (words + (BS - len(words) % BS) * chr(BS - len(words) % BS)).encode('utf-8')


def _make_data(json_req, site_key):
    raw = _pad(json_req)
    cipher = AES.new(site_key, AES.MODE_CBC, AES_IV)
    return base64.b64encode(cipher.encrypt(raw)).decode('utf-8')


def _make_timestamp():
    return datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")


def _make_hash(access_key, site_id, enc_data, timestamp):
    hash_input = access_key + site_id + enc_data + timestamp
    hash_string = base64.b64encode(
        hashlib.sha256(bytes(hash_input, "utf-8")).digest()
    )
    return hash_string.decode("utf-8")
