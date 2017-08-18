import fileinput
d = {}
n = -1
for line in fileinput.input():
    if fileinput.isfirstline():
        n = int(line.split()[0])
        continue
    line_no = fileinput.lineno()
    line = line.splitlines()[0]
    if line_no < n + 2:
        try:
            d[line] += 1
        except:
            d[line] = 1
    if line_no > n+2:
        try:
            print d[line]
        except:
            print 0

