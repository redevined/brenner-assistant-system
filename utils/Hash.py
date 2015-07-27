#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import hashlib


ALGORITHMS = (
	hashlib.sha1,
	hashlib.sha512,
	hashlib.sha224,
	hashlib.sha512,
	hashlib.sha256,
	hashlib.sha512,
	hashlib.sha384,
	hashlib.sha512,
	hashlib.sha256
)


def hash(msg, funcs = ALGORITHMS) :
	if funcs :
		hashed = funcs[0](msg).hexdigest()
		return hash(hashed, funcs[1:])
	else :
		return msg
