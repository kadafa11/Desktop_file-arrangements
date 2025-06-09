import os
import collections

Download_path=os.path.join(
    os.path.expanduser("~"),
    "Downloads"
    )
Download_path=os.path.normpath("C:\Users\USER\Downloads")


file_mappings=collections.defaultdict()
for filename in os.listdir(Download_path):
    file_type=filename.split(".")[-1]
    file_mappings.setdefault(file_type, []).append(filename)

print(file_mappings)

