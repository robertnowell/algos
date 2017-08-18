import fileinput
lastAnswer = 0
n = 0
for line in fileinput.input():
    if fileinput.isfirstline():
        n = int(line.split()[0])
        seq = [[] for x in xrange(n)]
        continue
    queryType = line.split()[0]
    x = int(line.split()[1])
    y = int(line.split()[2])
    i = (x ^ lastAnswer) % n
    if queryType == '1':
        seq[i] += [y]
    if queryType == '2':
        size = len(seq[i])
        lastAnswer = seq[i][y % size]
        print lastAnswer