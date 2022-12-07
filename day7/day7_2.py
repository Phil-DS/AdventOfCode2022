from data import data

sizes = {}
dupes = {}
current_path = []

for row in data.strip().split('\n'):
    if row == '$ ls':
        continue
    if row == '$ cd ..':
        current_path.pop()
        continue
    if row.startswith('$ cd '):
        name = row[5:]
        if name in sizes:
            ith = dupes.get(name,0) + 1
            dupes[name] = ith
            name += f'({ith})'
        current_path.append(name)
        sizes[name] = 0
        continue

    size_type, name = tuple(row.strip().split(' '))
    if not size_type == 'dir':
        for path in current_path:
            sizes[path] = sizes.get(path,0) + int(size_type)
    
total_size = sizes['/']
needed_size = 30000000 - (70000000 - total_size)

l = min([k for k in sorted(sizes.values()) if k >= needed_size])
print(l)
