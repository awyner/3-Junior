class FileSystem:
    def __init__(self):
        self.pwd = Directory()


class Directory:
    def __init__(self, parent=None):
        self.parent = parent
        self.contents = {}
        self.size = 0
    
    def search(self):
        count = 0
        for item in self.contents.values():
            if isinstance(item, Directory):
                temp = item.search()
                self.size += temp[0]
                count += temp[1]
            else:
                self.size += item
        if self.size < 100_000:
            count += self.size
        return self.size, count
    
    def search2(self, min):
        for item in self.contents.values():
            if isinstance(item, Directory):
                item.search2(min)
        min.append(self.size)
        return min
    
    def addFile(self, file, size):
        self.contents[file] = int(size)

    def addDir(self, dir, parent=None):
        self.contents[dir] = Directory(parent)


def main():
    fs = FileSystem()
    with open("day7\\input.txt") as f:
        for line in f:
            line = line.strip().split()
            if line[0] == '$':
                cmd = line[1]
                if cmd == 'cd' and line[2] == '..':
                    fs.pwd = fs.pwd.parent
                elif cmd == 'cd' and line[2] != '/':
                    fs.pwd = fs.pwd.contents[line[2]]
                elif cmd == 'ls':
                    pass
            elif line[0] == 'dir':
                fs.pwd.addDir(line[1], fs.pwd)
            else:
                fs.pwd.addFile(line[1], line[0])
    while fs.pwd.parent:
        fs.pwd = fs.pwd.parent
    fs.pwd.search()

    space = 30_000_000 - (70_000_000-fs.pwd.size)
    min = fs.pwd.search2([])
    min.sort()
    for x in min:
        if x > space:
            print(x)
            break
main()