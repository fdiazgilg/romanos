import conversion

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

decimal = InputUntil("Introduzca un número entero y positivo: ", lambda x: esEntero(x) and int(x) > 0 and int(x) < 4000000, 'Debe introducir un valor entero, mayor que cero y menor que 4000000.\n', lambda x: x.lstrip('0'))

if int(decimal) > 3999:
    decimal1 = decimal[0:-3]
    decimal2 = decimal[-3:]
    roman1 = conversion.arabRomano(decimal1)
    roman2 = conversion.arabRomano(decimal2)
    
    romano = '(' + roman1 + ')' + roman2
    
    romano1 = romano[1:romano.find(')')]
    romano2 = romano[(romano.find(')'))+1:]
    arab1 = conversion.romanoArab(romano1) * 1000
    arab2 = conversion.romanoArab(romano2)

    arabigo = arab1 + arab2
    
else:
    romano = conversion.arabRomano(decimal)
    arabigo = conversion.romanoArab(romano)

print("\nEl número romano correspondiente al número arábigo {} es {}.".format(int(decimal),romano))
print("El número arábigo correspondiente al número romano {} es {}.".format(romano,arabigo))
