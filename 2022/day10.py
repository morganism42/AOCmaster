input = [['noop'], ['addx', 26], ['addx', -21], ['addx', 2], ['addx', 3], ['noop'], ['noop'], ['addx', 23],
         ['addx', -17], ['addx', -1], ['noop'], ['noop'], ['addx', 7], ['noop'], ['addx', 3], ['addx', 1], ['noop'],
         ['noop'], ['addx', 2], ['noop'], ['addx', 7], ['noop'], ['addx', -12], ['addx', 13], ['addx', -38],
         ['addx', 5], ['addx', 34], ['addx', -2], ['addx', -29], ['addx', 2], ['addx', 5], ['addx', 2], ['addx', 3],
         ['addx', -2], ['addx', -1], ['addx', 8], ['addx', 2], ['addx', 6], ['addx', -26], ['addx', 23], ['addx', -26],
         ['addx', 33], ['addx', 2], ['addx', -37], ['addx', -1], ['addx', 1], ['noop'], ['noop'], ['noop'], ['addx', 5],
         ['addx', 5], ['addx', 3], ['addx', -2], ['addx', 2], ['addx', 5], ['addx', 5], ['noop'], ['noop'],
         ['addx', -2], ['addx', 4], ['noop'], ['noop'], ['noop'], ['addx', 3], ['noop'], ['noop'], ['addx', 7],
         ['addx', -1], ['addx', -35], ['addx', -1], ['addx', 5], ['addx', 3], ['noop'], ['addx', 4], ['noop'], ['noop'],
         ['noop'], ['noop'], ['noop'], ['addx', 5], ['addx', 1], ['noop'], ['noop'], ['noop'], ['addx', -7],
         ['addx', 12], ['addx', 2], ['addx', 7], ['noop'], ['addx', -2], ['noop'], ['noop'], ['addx', 7], ['addx', 2],
         ['addx', -39], ['noop'], ['noop'], ['addx', 5], ['addx', 2], ['addx', -4], ['addx', 25], ['addx', -18],
         ['addx', 7], ['noop'], ['addx', -2], ['addx', 5], ['addx', 2], ['addx', 6], ['addx', -5], ['addx', 2],
         ['addx', -22], ['addx', 29], ['addx', -21], ['addx', -7], ['addx', 31], ['addx', 2], ['noop'], ['addx', -36],
         ['addx', 1], ['addx', 5], ['noop'], ['addx', 1], ['addx', 4], ['addx', 5], ['noop'], ['noop'], ['noop'],
         ['addx', 3], ['noop'], ['addx', -13], ['addx', 15], ['noop'], ['addx', 5], ['noop'], ['addx', 1], ['noop'],
         ['addx', 3], ['addx', 2], ['addx', 4], ['addx', 3], ['noop'], ['addx', -3], ['noop']]
tinput = [['addx', 15], ['addx', -11], ['addx', 6], ['addx', -3], ['addx', 5], ['addx', -1], ['addx', -8], ['addx', 13],
          ['addx', 4], ['noop'], ['addx', -1], ['addx', 5], ['addx', -1], ['addx', 5], ['addx', -1], ['addx', 5],
          ['addx', -1], ['addx', 5], ['addx', -1], ['addx', -35], ['addx', 1], ['addx', 24], ['addx', -19], ['addx', 1],
          ['addx', 16], ['addx', -11], ['noop'], ['noop'], ['addx', 21], ['addx', -15], ['noop'], ['noop'],
          ['addx', -3], ['addx', 9], ['addx', 1], ['addx', -3], ['addx', 8], ['addx', 1], ['addx', 5], ['noop'],
          ['noop'], ['noop'], ['noop'], ['noop'], ['addx', -36], ['noop'], ['addx', 1], ['addx', 7], ['noop'], ['noop'],
          ['noop'], ['addx', 2], ['addx', 6], ['noop'], ['noop'], ['noop'], ['noop'], ['noop'], ['addx', 1], ['noop'],
          ['noop'], ['addx', 7], ['addx', 1], ['noop'], ['addx', -13], ['addx', 13], ['addx', 7], ['noop'], ['addx', 1],
          ['addx', -33], ['noop'], ['noop'], ['noop'], ['addx', 2], ['noop'], ['noop'], ['noop'], ['addx', 8], ['noop'],
          ['addx', -1], ['addx', 2], ['addx', 1], ['noop'], ['addx', 17], ['addx', -9], ['addx', 1], ['addx', 1],
          ['addx', -3], ['addx', 11], ['noop'], ['noop'], ['addx', 1], ['noop'], ['addx', 1], ['noop'], ['noop'],
          ['addx', -13], ['addx', -19], ['addx', 1], ['addx', 3], ['addx', 26], ['addx', -30], ['addx', 12],
          ['addx', -1], ['addx', 3], ['addx', 1], ['noop'], ['noop'], ['noop'], ['addx', -9], ['addx', 18], ['addx', 1],
          ['addx', 2], ['noop'], ['noop'], ['addx', 9], ['noop'], ['noop'], ['noop'], ['addx', -1], ['addx', 2],
          ['addx', -37], ['addx', 1], ['addx', 3], ['noop'], ['addx', 15], ['addx', -21], ['addx', 22], ['addx', -6],
          ['addx', 1], ['noop'], ['addx', 2], ['addx', 1], ['noop'], ['addx', -10], ['noop'], ['noop'], ['addx', 20],
          ['addx', 1], ['addx', 2], ['addx', 2], ['addx', -6], ['addx', -11], ['noop'], ['noop'], ['noop']]
data = input
i = 0
j = 0
x = 2
count = 0
out = [[]]
while True:
    if 0 <= (x - i) <= 2:
        out[-1].append('#')
        i += 1
    else:
        out[-1].append('.')
        i += 1
    if i == 40:
        i = 0
        out.append([])
    if data[j][0] == 'addx':
        if 0 <= (x - i) <= 2:
            out[-1].append('#')
            i += 1
        else:
            out[-1].append('.')
            i += 1
        if i == 40:
            i = 0
            out.append([])
        x += data[j][1]
        j += 1

    else:
        j += 1
    if j == len(data):
        break

    if i == 40:
        i = 0
        out.append([])
for i in out:
    txt = ''
    for j in i:
        txt += j
    print(txt)
print(count)
