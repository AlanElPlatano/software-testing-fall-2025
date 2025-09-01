def f1(input):
    if input < 0:
        return "Negativo"
    elif input == 0:
        return "Cero"
    elif input > 0:
        return "Positivo"
    
def f2(input):
    # Para que (no) pase el caso de ser solo un número
    input = str(input)
    if input.isnumeric() == True:
        return "La contraseña no puede ser solo números"
    elif (input[0] == ' ' or input[-1] == ' '):
        return "La contraseña no puede empezar o terminar con espacio"
    elif len(input) < 8:
        return "La contraseña debe ser de al menos 8 caracteres"
    
    # Recorrer toda la cadena, si llega al final sin encontrar mayusculas, marca error
    for i in range(len(input)):
        if input[i].isupper():
            break
        elif i == len(input) - 1:
            return "La contraseña debe contener al menos una mayúscula"
    
    # Recorrer toda la cadena, si llega al final sin encontrar minusculas, marca error
    for i in range(len(input)):
        if input[i].islower():
            break
        elif i == len(input) - 1:
            return "La contraseña debe contener al menos una minúscula"
        
    # Busca numeros en la cadena
    for i in range(len(input)):
        if input[i].isdigit():
            break
        elif i == len(input) - 1:
            return "La contraseña debe contener al menos un número"
        
    # Buscar caracteres especiales específicos
    special_characters = "!@#$%^&"
    for i in range (len(input)):
        if input[i] in special_characters:
            break
        elif i == len(input) -1:
            return "La contraseña debe contener al menos uno de los siguientes caracteres especiales (!, @, #, $, %, or &)"
        
    return "Contraseña válida"

def f3(input):
    if input < 100:
        return "No hay descuento para ti :("
    elif input >= 100 and input <= 500:
        return "Tienes un descuento del 10%"
    elif input > 500:
        return "Tienes un descuento del 20%"
    

var1 = 69
print(f1(var1))

var2 = "Password123!"
print(f2(var2))

var3 = 150
print(f3(var3))