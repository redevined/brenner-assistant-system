#/usr/bin/env python
# -*- coding: UTF-8 -*-

import inspect

from config import System


# Basic log function, uses stdout
def log(caller, level, *msgs, **vals) :
	head = u"[{level}] {caller}".format(caller = caller, level = level)
	msgs = u" ".join(msgs)
	vals = u" ".join( u"[{key}: {val}]".format(key = key, val = val) for key, val in vals.items() )
	print u" ".join( part for part in (head, msgs, vals) if part )

# Log function with loglevel INFO
def info(*msgs, **vals) :
	caller = inspect.stack()[1][3]
	level = "INFO"
	log(level, caller, *msgs, **vals)

# Log function with loglevel WARN
def warn(*msgs, **vals) :
	caller = inspect.stack()[1][3]
	level = "WARN"
	log(level, caller, *msgs, **vals)

# Log function with loglevel ERROR
def error(*msgs, **vals) :
	caller = " :: ".join(st[3] for st in inspect.stack())
	level = "ERROR"
	log(level, caller, *msgs, **vals)

# Log function with loglevel DEBUG
def debug(*msgs, **vals) :
	caller = inspect.stack()[1][3]
	level = "DEBUG"
	if System.debug :
		log(level, caller, *msgs, **vals)
