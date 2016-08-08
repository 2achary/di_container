from registrations import di_container


class TestThis(object):
    def __init__(self):
        self.myclass = di_container.get('MyClass')
        self.myfunc = di_container.get('myfunc')
        # print(self.myclass)

    def foo(self):
        return self.myfunc()

t = TestThis()
print(t.myclass)
