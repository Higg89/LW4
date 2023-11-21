import json

b = []
l = []

f = open("InputData.txt", "r", encoding = 'UTF-8')
lines = f.readlines()
for line in lines:
  l = (line.split('\n'))
  b.append(l[0])
f.close()
output = open("OutputData.json", 'w', encoding = 'UTF-8')
for i in b:
  json.dump(i, output, ensure_ascii=False)
