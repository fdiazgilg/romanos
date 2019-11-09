def arabRomano(num):    
    tipo1 = ('M','C','X','I')
    tipo5 = ('D','L','V')
    listRomano = []
    
    for i in range(-len(num), 0):
        if num[i] <= '3':
            listRomano.append(int(num[i]) * tipo1[i])
        elif num[i] == '4':
            listRomano.append(tipo1[i] + tipo5[i])
        elif num[i] >= '5' and num[i] <= '8' :
            listRomano.append(tipo5[i] + (int(num[i]) - 5) * tipo1[i])
        elif num[i] == '9':
            listRomano.append(tipo1[i] + tipo1[i-1])
        else:
            pass
    
    numRomano = ''
    for j in range(len(listRomano)):
        numRomano += listRomano[j]
    return numRomano

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
