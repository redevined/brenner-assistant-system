#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from inspect import stack as getSysStack
from config import Config


# Cast strings to unicode
def _unify(s) :
	if not isinstance(s, unicode) :
		s = unicode(str(s), Config.encoding)
	return s

# Basic log function, uses stdout
def log(level, *msgs, **vals) :
	level = u"[{level}]".format(level = level)
	caller = u"({1}::{3})".format(*getSysStack()[2])
	msgs = u" ".join( _unify(msg) for msg in msgs )
	vals = u" ".join( u"[{key}: {val}]".format(key = key, val = _unify(val)) for key, val in vals.items() )
	out = u" ".join( part for part in (level, caller, msgs, vals) if part )
	print out.encode("ascii", "ignore")

# Log function with loglevel INFO
def info(*msgs, **vals) :
	level = Config.Log.info
	log(level, *msgs, **vals)

# Log function with loglevel WARN
def warn(*msgs, **vals) :
	level = Config.Log.warn
	log(level, *msgs, **vals)

# Log function with loglevel ERROR
def error(*msgs, **vals) :
	level = Config.Log.error
	log(level, *msgs, **vals)

# Log function with loglevel DEBUG
def debug(*msgs, **vals) :
	level = Config.Log.debug
	if Config.debug :
		log(level, *msgs, **vals)

# Debug function that prints all attributes of an object
def inspect(obj) :
	level = Config.Log.debug
	if Config.debug :
		indent = max(map(len, dir(obj)))
		for attr in dir(obj) :
			val = getattr(obj, attr)
			attr = attr.ljust(indent) + " :"
			log(level, attr, val) 