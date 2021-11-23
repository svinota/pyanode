import os
import io
import zipfile
from importlib import metadata


class Bundle(object):

    def __init__(self, package_name):
        self.package = package_name
        self.io = io.BytesIO()
        self.zip = zipfile.ZipFile(self.io, mode='w')
        with zipfile.ZipFile(self.io, mode='w') as self.zip:
            for file in metadata.files(self.package):
                if os.path.exists(file.locate()):
                    self.zip.write(file.locate(),
                                   file.joinpath())

    @property
    def data(self):
        return self.io.getvalue()
