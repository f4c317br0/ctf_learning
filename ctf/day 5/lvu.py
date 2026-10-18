import os

folder = "traces"
files = sorted(os.listdir(folder))
print(len(files), "файлов")
print(files[:10])

with open(os.path.join(folder, files[0])) as f:
    content = f.read()
print(content[:1000])