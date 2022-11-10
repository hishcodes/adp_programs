tableData = [['apples', 'oranges', 'cherries', 'banana'],
            ['Alice', 'Bob', 'Carol', 'David'],
            ['dogs', 'cats', 'moose', 'goose']]
def printTable(l):
    cwidth = [len(max(col, key=len)) for col in l]
    for rownum in range(len(max(l))):
        row = ''
        for col in range(len(l)):
            row += l[col][rownum].rjust(cwidth[col]) + ' '
        print(row)
printTable(tableData)