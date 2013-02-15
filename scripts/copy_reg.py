# Helper to provide extensibility for pickle/cPickle.

dispatch_table = {}
safe_constructors = {}

def pickle(ob_type, pickle_function, constructor_ob = None):
    dispatch_table[ob_type] = pickle_function

    if constructor_ob is not None:
        constructor(constructor_ob)

def constructor(object):
    safe_constructors[object] = 1

# Example: provide pickling support for complex numbers.

def pickle_complex(c):
    return complex, (c.real, c.imag)

pickle(type(1j), pickle_complex, complex)

def pickle_type(s):
	print "Sorry unable to pickle this type(type()) - %s. Check copy_reg" % str(s)
	
	if s.__name__ == "list":
		return type, tuple(["list"])
	elif s.__name__ == "string":
		return type, tuple(" ")
	else:
		return type, tuple(" ")


pickle(type(type("")), pickle_type, type)
