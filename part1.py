import re
pattern = "(?<=:)\d+"
for i in open("part1.txt"):
    out = re.findall(pattern,i)
    for o in out:
        print(o)
