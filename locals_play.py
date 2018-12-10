from __future__ import print_function
import types
import inspect
import sys


if sys.version_info[0] < 3:
    def class_of(object):
        return object.im_class

else:
    def class_of(object):
        return object.__self__.__class__



def get_methods_of(object):
    self = object
    results = {}
    for attr in dir(self):
        method = getattr(self, attr)
        if type(method) == types.MethodType and \
                        method.__name__ not in ('__init__') and \
                        method.__func__ in class_of(method).__dict__.values():
            args = inspect.getargspec(method)[0][1:]
            results[method.__name__] = args
    return results



class C(object):
    def c1(self): pass
    def c2(self, bar): pass


class D(C):
    def d1(self): pass
    def d2(self, bar, baz): pass


print("local methods of a C instance: {}".format(get_methods_of(C())))
print()
print()
print("local methods of a D instance: {}".format(get_methods_of(D())))
