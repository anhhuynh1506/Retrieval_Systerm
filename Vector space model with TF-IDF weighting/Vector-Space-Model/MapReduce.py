import json

class MapReduce:
    def __init__(self):
        self.intermediate = {}
        self.result = []

    def emit_intermediate(self, key, value):
        self.intermediate.setdefault(key, [])
        self.intermediate[key].append(value)

    def emit(self, value):
        self.result.append(value) 

    def execute(self, data, mapper, reducer, output):
      with open (output, 'w', encoding='utf-8') as f:
        for line in data:
            record = json.loads(line)
            mapper(record)
        for key in self.intermediate:
            reducer(key, self.intermediate[key])
        jenc = json.JSONEncoder(ensure_ascii=False)
        for item in self.result:
            f.write(jenc.encode(item) + '\n')
      f.close()    
