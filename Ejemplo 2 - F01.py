# TEAM 

# ESTE CÓDIGO MUESTRA LA CREACION DE UNA LISTA A QUE LE SE AGREGARA UN NUEVO ELEMENTO Y POSTERIORMENTE
# SE IMPRIMIRA EL RESULTADO PARA COMPROBAR QUE SE LA ACCION REALIZADA SI SE EJECUTO

# 2025 / 03/ 03 - V. 1. 1. 2

# TRABAJARON: CESAR ARTURO / CesarDAlvin

frutas = ["Uvas", "Guanabana", "Piña", "Fresa"] # SE CREA UNA LISTA CON FRUTAS


frutas.append("Mandarina") #LA FUNCION APPEND AGREGA UN NUEVO ELEMENTO A LAS LISTA DEFINIDA ANTERIORMENTE


print("Lista de frutas:", frutas) #LA FUNCION PRINT IMRPIME EN LA TERMINAL. PRIMERO, LA CADENA DE TEXTO "Lista de frutas" Y POSTERIORMENTE EL CONTENIDO DE LA LISTA FRUTAS

for fruta in frutas: #OCUPAMOS LA FUNCION "for" PARA QUE REALICE UNA SERIE DE ACCIONES DONDE NOMBRA COMO "fruta" A CADA ELEMENTO DE LA LISTA
    print("Tengo una", fruta) #DADO EL CICLO "for" SE IMPRIME CON EL FORMATO DEFINIDO EN LA FUNCION "print" UNA SERIE DE ORACIONES EN LA QUE LA PARTE FRUTA DE CADA ORACION CAMBIA
