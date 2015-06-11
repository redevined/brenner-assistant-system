#/usr/bin/env python

import hashlib
from pickle import dumps, loads
from base64 import b64encode, b64decode


def hash(obj) :
	hashed = hashlib.sha1(obj)
	return hashed.hexdigest()

def encode(obj) :
	dump = dumps(obj)
	return b64encode(dump)

def decode(obj) :
	decoded = b64decode(obj)
	return loads(decoded)