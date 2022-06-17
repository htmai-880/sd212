import subprocess
import os
from sys import argv

def file_count(dir_path = r'./ratings'):
    count = 0
    # Iterate directory
    for path in os.listdir(dir_path):
        # check if current path is a file
        if os.path.isfile(os.path.join(dir_path, path)):
            count += 1
    print('Started getting user ratings from rank {}'.format(count))
    return count

limit = int(argv[1])
print("Limit: ", limit)

while file_count() <= limit:
    subprocess.call("python userrating.py")