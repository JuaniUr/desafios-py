print ('ingrese la fraze a encriptar')
cadena = input('')
def encript (cadena):
    cadena_encriptada = list (map(lambda x: chr(ord(x) +1), cadena))
    print (cadena_encriptada)
    print ('*' * 10)
    cadena_encriptada = ''.join (cadena_encriptada)
    print (cadena_encriptada)
    return(cadena_encriptada)
cadena_encriptada= encript (cadena)

print ('*' * 10)
def desencriptar (cadena_encriptada):
    cadena = list (map(lambda x: chr(ord(x)-1), cadena_encriptada))
    cadena = ''.join(cadena)
    print (cadena)
desencriptar (cadena_encriptada)