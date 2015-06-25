#/usr/bin/env python


# Basic log function, uses stdout
def log(level, *msgs, **vals) :
	level = "[{level}]".format(level = level)
	msgs = " ".join(msgs)
	vals = " ".join( "[{key}: {val}]".format(key = key, val = val) for key, val in vals.items() )
	print " ".join( part for part in (level, msgs, vals) if part )

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
	log(level, *msgs, **vals)
