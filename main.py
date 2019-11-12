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

decimal = InputUntil("Introduzca un número entero y positivo: ", lambda x: esEntero(x) and int(x) > 0, 'Debe introducir un valor entero y mayor que cero.\n', lambda x: x.lstrip('0'))

romano = conversion.arabRomano(decimal)

print("\nEl número romano correspondiente al número arábigo {} es {}.".format(int(decimal),romano))
