#/usr/bin/env python
# -*- coding: UTF-8 -*-

import inspect

from config import Config


def _unify(s) :
	if not isinstance(s, unicode) :
		s = unicode(str(s), Config.coding)
	return s

# Basic log function, uses stdout
def log(level, *msgs, **vals) : # TODO: Fix unicode bullshit
	level = u"[{level}]".format(level = level)
	caller = u"({1}::{3})".format(*inspect.stack()[2])
	msgs = u" ".join( _unify(msg) for msg in msgs )
	vals = u" ".join( u"[{key}: {val}]".format(key = key, val = _unify(val)) for key, val in vals.items() )
	print u" ".join( part for part in (level, caller, msgs, vals) if part )

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
