def make_instance(cls):
	"""Return a new object instance, which is a dispatch dictionary."""
	def get_value(name):
		if name in attributes:
			return attributes[name]
		else:
			value = cls['get'](name)
			return bind_method(value, instance)
	def set_value(name, value):
		attributes[name] = value
	attributes = {}
	instance = {'get': get_value, 'set': set_value}
	return instance

def bind_method(value, instance):
	"""Return a bound method if value is callable, or value otherwise."""
	if callable(value):
		def method(*args):
			return value(instance, *args)
			return method
		else:
			return value
		