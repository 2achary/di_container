from di_container import DiContainer
from my_class import MyClass, myfunc


di_container = DiContainer()
di_container.register('myfunc', [], lambda: myfunc)
di_container.register('MyClass', [], lambda: MyClass())
