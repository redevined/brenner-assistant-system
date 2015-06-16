#/usr/bin/env python


# Easy accessable dict
class ConfigObject(dict) :

	# Enable item access with 'object.key' syntax
	def __getattribute__(self, attr) :
		if object.__getattribute__(self, "has_key")(attr) and attr != "getattribute" :
			return self[attr]
		return object.__getattribute__(self, attr)

	# Fallback to get attributes that are overriden with keys
	def getattribute(self, attr) :
		return object.__getattribute__(self, attr)


# Recursive factory function for creating nested ConfigObjects
def create(obj) :
	co = ConfigObject(obj)
	for key, value in co.items() :
		if isinstance(value, dict) :
			co[key] = create(value)
	return co