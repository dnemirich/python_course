import os


class FileSystemError(Exception):
    ''' Class for errors in filesystem module '''

    pass


class FSItem(object):

    def __init__(self, path):
        self.path = path

    def rename(self, newname):
        pass

    def create(self):
        pass

    def getname(self):
        return os.path.basename(self.path)

    def isfile(self):
        return os.path.isfile(self.path)

    def isdirectory(self):
        return os.path.isdir(self.path)


class File(FSItem):

    def __init__(self, path):
        if os.path.exists(self.path):
            raise FileSystemError("{0} file with the same path already exists".
                                  format(self.path))
        else:
            super(File, self).__init__(path)

    def __len__(self):
        if os.path.exists(self.path):
            return os.path.getsize(self.path)
        else:
            raise FileSystemError("{0} file doesn't exist".format(self.path))

    def getcontent(self):
        if os.path.exists(self.path):
            return open(self.path, "r").read().splitlines()
        else:
            raise FileSystemError("{0} file doesn't exist".format(self.path))

    def __iter__(self):
        if os.path.exists(self.path):
            return iter(self.getcontent())
        else:
            raise FileSystemError("{0} file doesn't exist".format(self.path))


class Directory(FSItem):

    def __init__(self, path):
        if os.path.exists(self.path):
            raise FileSystemError("""{0} directory with the same path already
                                  exists""".format(self.path))
        else:
            super(Directory, self).__init__(path)

    def items(self):
        if os.path.exists(self.path):
            yield from self.files()
            yield from self.subdirectories()
        else:
            raise FileSystemError("{0} directory doesn't exist".
                                  format(self.path))

    def files(self):
        if os.path.exists(self.path):
            for item in os.listdir(self.path):
                item_path = os.path.join(self.path, item)
                if os.path.isfile(self.item_path):
                    yield File(item_path)
        else:
            raise FileSystemError("{0} directory doesn't exist".
                                  format(self.path))

    def subdirectories(self):
        if os.path.exists(self.path):
            for item in os.listdir(self.path):
                item_path = os.path.join(self.path, item)
                if os.path.isdir(self.item_path):
                    yield Directory(item_path)

        else:
            raise FileSystemError("{0} directory doesn't exist".
                                  format(self.path))

    def filesrecursive(self):
        if os.path.exists(self.path):
            for file in self.files():
                yield file
            for directory in self.subdirectories():
                yield from directory.filesrecursive

        else:
            raise FileSystemError("{0} directory doesn't exist".
                                  format(self.path))

    def getsubdirectory(self, name):
        new = os.path.join(self.path, name)
        global new
        if os.path.exists(self.new) and not os.path.isdir(self.new):
            raise FileSystemError("""{0} directory already exists and is not a
                                  directory""".format(self.new))
        else:
            return Directory(self.new)
