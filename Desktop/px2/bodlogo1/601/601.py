ifile = open('input.txt', 'r', encoding = 'utf-8')
mylines = ifile.readlines()
teachers = []
salbar = {}
keys = ['ner','ovog','huis','salbar','tenhim','utas']
for line in mylines:
    values = line.split()
    rd = dict(zip(keys, values))
    if rd['salbar'] in salbar:
        salbar[rd['salbar']] += 1
    else:
        salbar[rd['salbar']] = 1
    teachers.append(rd)
ofile = open('output.txt', 'w', encoding = 'utf-8')
for row in sorted(salbar):
    ofile.write(row+' '+str(salbar[row])+'\n')
