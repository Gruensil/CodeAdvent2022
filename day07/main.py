import time

class Directory():
    def __init__(self, name, parent=None) -> None:
        self.name = name
        self.parent = parent
        self.children = {}
        self.content = []
        self.size = 0

def get_dir_size(curr_dir, special_dir=[], magic_size=0):
    total_size = curr_dir.size
    for child in curr_dir.children.values():
        total_size += get_dir_size(child, special_dir, magic_size)

    if total_size >= magic_size:
        special_dir.append(curr_dir)
    return total_size


system_size = 70000000
needed_size = 30000000

with open('C:\\Users\\gruen\\Documents\\CodeAdvent2022\\day07\\input.txt') as f:
    file = f.readlines()
    tic = time.perf_counter()

    root = Directory('/')
    current_dir = root
    for line in file:
        line = line.strip()
        if '$ ls' in line or '$ cd /' in line:
            continue
        if 'dir ' in line:
            current_dir.children[line[4:]] = Directory(line[4:], parent=current_dir)
            continue
        if '$ cd ..' in line:
            current_dir = current_dir.parent
            continue
        if '$ cd ' in line:
            current_dir = current_dir.children[line[5:]]
            continue
        file = line.split()
        current_dir.size += int(file[0])
        current_dir.content.append(file)

    larger_dirs = []
    get_dir_size(root, larger_dirs, 8281165)
    smallest_size = 9999999999999999999999999
    smallest_dir = None
    for dir in larger_dirs:
        curr_size = get_dir_size(dir)
        if curr_size < smallest_size:
            smallest_size = curr_size
            smallest_dir = dir

    toc = time.perf_counter()
    print(f"Size is {smallest_size}")
    print(f"Found solution in {toc - tic:0.4f} seconds") # 0.0012s

