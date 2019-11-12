def arabRomano(num):
    
    _MAX = 3999
    arabSep = []
    
    while int(num) > _MAX:
        num1 = num[-3:]
        arabSep.append(num1)        
        num2 = num[:-3]
        
        num = num2
    
    arabSep.append(num)
    arabSep.reverse()

    listNumRomano = []
    for numArab in arabSep:

        tipo1 = ('M','C','X','I')
        tipo5 = ('D','L','V')
        listRomano = []
        for j in range(-len(numArab), 0):
            if numArab[j] <= '3':
                listRomano.append(int(numArab[j]) * tipo1[j])
            elif numArab[j] == '4':
                listRomano.append(tipo1[j] + tipo5[j])
            elif numArab[j] >= '5' and numArab[j] <= '8' :
                listRomano.append(tipo5[j] + (int(numArab[j]) - 5) * tipo1[j])
            elif numArab[j] == '9':
                listRomano.append(tipo1[j] + tipo1[j-1])
            else:
                pass
        
        numRomano = ''
        for k in range(len(listRomano)):
            numRomano += listRomano[k]
            
        listNumRomano.append(numRomano)
        
        esRomano = ''
        for l in range(len(listNumRomano)-1):
            esRomano += listNumRomano[l]
        
        if len(listNumRomano) >= 2:
            romano = '(' + esRomano + ')' + listNumRomano[-1]
        else:
            romano = esRomano + listNumRomano[-1]

    return romano

def romanoArab(num):
    dict = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
    listArab = []
    numArab = 0
    for key in num:
        listArab.append(dict[key])

    i = -len(listArab)
    while i < -1:
        if listArab[i] >= listArab[i+1]:
            numArab += listArab[i]
            i += 1
        else:
            numArab += listArab[i+1] - listArab[i]
            i += 2
    if i == -1:
        numArab += listArab[i]
   
    return numArab       
