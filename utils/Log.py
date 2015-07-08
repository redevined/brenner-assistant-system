#/usr/bin/env python
# -*- coding: UTF-8 -*-

import inspect

from config import System


# Basic log function, uses stdout
def log(level, *msgs, **vals) :
	level = u"[{level}]".format(level = level)
	caller = u"{1}::{3}".format(*inspect.stack()[2])
	msgs = u" ".join(msgs)
	vals = u" ".join( u"[{key}: {val}]".format(key = key, val = val) for key, val in vals.items() )
	print u" ".join( part for part in (level, caller, msgs, vals) if part )

# Log function with loglevel INFO
def info(*msgs, **vals) :
	level = "INFO"
	log(level, *msgs, **vals)

# Log function with loglevel WARN
def warn(*msgs, **vals) :
	level = "WARN"
	log(level, *msgs, **vals)

# Log function with loglevel ERROR
def error(*msgs, **vals) :
	level = "ERROR"
	log(level, *msgs, **vals)

# Log function with loglevel DEBUG
def debug(*msgs, **vals) :
	level = "DEBUG"
	if System.debug :
		log(level, *msgs, **vals)
