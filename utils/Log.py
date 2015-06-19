#/usr/bin/env python


# Basic log function, uses stdout
def log(level, msg, *args, **kwargs) :
	print "[{level}] {msg} {objs} {nobjs}".format(
		level = level,
		msg = msg,
		objs = " ".join(
			"[{arg}]".format(arg = arg) for arg in args
		),
		nobjs = " ".join(
			"[{name}: {arg}]".format(name = name, arg = arg) for name, arg in kwargs.items()
		)
	)

# Log function with loglevel INFO
def info(msg, *args, **kwargs) :
	level = "INFO"
	log(level, msg, *args, **kwargs)

# Log function with loglevel WARN
def warn(msg, *args, **kwargs) :
	level = "WARN"
	log(level, msg, *args, **kwargs)

# Log function with loglevel ERROR
def error(msg, *args, **kwargs) :
	level = "ERROR"
	log(level, msg, *args, **kwargs)

# Log function with loglevel DEBUG
def debug(msg, *args, **kwargs) :
	level = "DEBUG"
	log(level, msg, *args, **kwargs)
