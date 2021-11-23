import io
import zipfile
import pathlib


class Bundle(object):

    def __init__(self, package):
        assert getattr(package, '__package__', None)
        assert getattr(package, '__path__', None)
        assert getattr(package, '__name__', None)
        self.package = package
        self.io = io.BytesIO()
        self.zip = zipfile.ZipFile(self.io, mode='w')
        self.path = [pathlib.Path(x) for x in package.__path__]
        with zipfile.ZipFile(self.io, mode='w') as self.zip:
            for path in self.path:
                for file in path.rglob('*'):
                    self.zip.write(file, file.relative_to(path.parent))

    @property
    def data(self):
        return self.io.getvalue()
