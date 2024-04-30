ifile = open('input.txt','r',encoding="utf-8")
mylines = ifile.readlines()
teachers = []
utass = {
    'Мобиком': 0,
    'Скайтел': 0,
    'Юнител': 0,
    'Жимобайл': 0

}
keys = ['ner','ovog','huis','salbar','tenhim','utas']
for line in mylines:
    values = line.split()
    rd = dict(zip(keys,values))
    utas = rd['utas']
    if utas[0:2] == '96' or utas[0:2] == '90'or utas[0:2] == '91':
        utass['Скайтел'] +=1
    elif utas[0:2] == '99':
        utass['Мобиком'] +=1
    elif utas[0:2] == '88'or utas[0:2] == '80'or utas[0:2] == '86':
        utass['Юнител'] +=1
    elif utas[0:2] == '98'or utas[0:2] == '93'or utas[0:2] == '97':
        utass['Жимобайл'] +=1
    teachers.append(rd)
ofile = open('output.txt','w',encoding="utf-8")
for row in sorted(utass):
    ofile.write(row+' '+str(utass[row])+'\n')