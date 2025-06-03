import csv
import os

from collections import defaultdict
import re
from pprint import pprint

spec_list = defaultdict(set)

file_path = "assets/specs.csv"  # 改成你的檔案路徑

if os.path.exists(file_path):
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:     
            for val in row:
                inch = val.split('-')[-1]
                if re.search(r"-\d{2}$", val):
                    spec_list[inch].add(val)             
else:
    spec_list = ''