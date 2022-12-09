class Folder:
    def __init__(self, name, parent=None):
        self.name = name
        self.children = {}
        self.files = {}
        self.parent = parent

    def make_file(self, size, name):
        self.files[name] = int(size)

    def make_folder(self, name):
        return self.children.setdefault(name, Folder(name, parent=self))

    @property
    def root(self):
        return self if self.parent is None else self.parent.root

    @property
    def size(self):
        return sum(self.files.values()) + sum(c.size for c in self.children.values())

    def __iter__(self):
        for child in self.children.values():
            yield child
            yield from child


def traverse_files(file, part1=True):
    data = open(file).read().strip().split("\n")
    cwd = Folder("/")
    for line in data[1:]:
        if line.startswith("dir") or line.startswith("$ ls"):
            continue
        elif line.startswith("$ cd"):
            d = line[5:]
            cwd = cwd.parent if d == ".." else cwd.make_folder(d)
        else:
            cwd.make_file(*line.split())
    if part1:
        return sum(c.size for c in cwd.root if c.size < 100000)
    else:
        return min(c.size for c in cwd.root if 40000000 + c.size > cwd.root.size)
