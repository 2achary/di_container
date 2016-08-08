class DiContainer(object):
    def __init__(self):
        self.registrations = {}
        self.messages = {
            'registerRequiresArgs': 'The register function requires three arguments: a string, a list of strings, and a function.'
        }

    def register(self, name, dependencies, func):
        if (type(name) != str
                or type(dependencies) != list
                or not callable(func)):
            raise ValueError(self.messages['registerRequiresArgs'])

        for dependency in dependencies:
            if type(dependency) != str:
                raise ValueError(self.messages['registerRequiresArgs'])

        self.registrations[name] = {'func': func, 'dependencies': dependencies}

    def get(self, name):
        registration = self.registrations.get(name)
        dependencies = []

        if not registration:
            return

        for dependency_name in registration['dependencies']:
            dependency = self.get(dependency_name)
            dependencies.append(dependency if dependency else None)

        return registration['func'](*dependencies)

