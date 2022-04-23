import os
import json
import sys

input_path = sys.argv[1]
read_files = os.listdir(input_path)
print(read_files)
with open (sys.argv[2], 'w', encoding='utf-8') as data:
  for f in read_files:
    file_name = os.path.join(input_path, f)
    with open (file_name, 'r', encoding='utf-8') as input:
      contents = input.read()
      record = [f, contents]
      fl = json.dumps(record, ensure_ascii=False).encode('utf-8')
      data.write(fl.decode() + '\n')
data.close()