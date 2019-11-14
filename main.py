import conversion

def esRomano(num):
    tipo1 = ('M','C','X','I')
    tipo5 = ('D','L','V')
    romans = ('M','D','C','L','X','V','I')
    
    resultado = True
    
    for i in range(len(num)):
        if num[i] not in romans:
            resultado = False

    for i in tipo1:
        if 4*i in num:
            resultado = False
        
    for j in tipo5:
        if 2*j in num:
            resultado = False
            
    for k in range(len(num)-1):
        if num[k] == 'V' and num[k+1] in ('M','C','X'):
            resultado = False
        elif num[k] == 'L' and num[k+1]  in ('M','C'):
            resultado = False
        elif num[k] == 'D' and num[k+1]  in ('M'):
            resultado = False
    
    for l in range(len(num)-1):
        if num[l] == 'I' and num[l+1] in ('M','D','C','L'):
            resultado = False
        elif num[l] == 'X' and num[l+1] in ('M','D'):
            resultado = False

    return resultado

def esEntero(x):
    try:
        int(x)
        return True
    except:
        return False

def InputUntil(msg, validation = None, error_msg = 'Se ha producido un error', transformation = None):
    _input_value = input(msg)
    while validation and not validation(_input_value):
        print(error_msg)
        _input_value = input(msg)
    if transformation:
        return transformation(_input_value)

    return _input_value

decimal = InputUntil("Introduzca un número entero y positivo: ", lambda x: esEntero(x) and int(x) > 0, 'Debe introducir un valor entero y mayor que cero.\n', lambda x: x.lstrip('0'))
romano = conversion.arabRomano(decimal)
print("El número romano correspondiente al número arábigo {} es {}.".format(int(decimal),romano))

roman = InputUntil("\nIntroduzca un número romano válido: ", esRomano, 'Este número romano no es válido.')
arabigo = conversion.romanoArab(roman)
print("El número arábigo correspondiente al número romano {} es {}.".format(roman,arabigo))
