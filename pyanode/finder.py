import importlib


class ModuleFinder(importlib.abc.MetaPathFinder):

    def load_module(self, fullname):
        pass
