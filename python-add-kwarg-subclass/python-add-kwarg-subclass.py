#!/usr/bin/python

class Top(object):
    def __init__(self, first, second=None):
        self.first = first
        self.second = second

class Bottom(Top):
    #def __init__(self, third=None, *args, **kwargs): No! TypeError: __init__() got multiple values for keyword argument 'third'
    #def __init__(self, *args, third=None, **kwargs): No! SyntaxError on 'third='.
    #def __init__(self, *args, **kwargs, third=None): No! 'third' can't follow **
    # Conculsion, unless I'm missing something: I have to repeat the parent signature explicitly instead of using kwargs
    def __init__(self, first, second=None, third=None):
        super(Bottom, self).__init__(first, second=second)
        self.third = third

    def __str__(self):
        return "first: %s\nsecond: %s\nthird: %s" % (self.first, self.second, self.third)


if __name__ == '__main__':
    b = Bottom("a", second="b", third="c")
    print(b)