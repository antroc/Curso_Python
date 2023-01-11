##INTRODUCCIÓN A LA LISTAS##

# En python las listas van entre corchetes, y dentro los elementos individuales
bicicletas = ['trek', 'cannodale', 'redline', 'bmx']
print(bicicletas)

# Acceder a los elemntos de una lista
print(bicicletas[0])

# Tambien se pueden usar métodos de la cadena
print(bicicletas[0].title())

# Las posiciones empiezanen 0 y no en 1
print(bicicletas[1])  # devuelve el segundo elemento
print(bicicletas[2])  # devuelve el tercer elemento
print(bicicletas[-1])  # devuelve el último elemento de la lista
print(bicicletas[-2])  # devuelve el penúltimo elemento de la lista

# Usar los elementos de la lista
mensaje = f"Mi primera bicicleta fue un {bicicletas[3].upper()}"
print(mensaje)

# modificar elementos de una lista
marcasMoto = ['Honda', 'Yamaha', 'Vespa']
print(marcasMoto)
marcasMoto[0] = 'Ducati'
print(marcasMoto)

# Para adjuntar elementos al final una lista utlizaremos la funcion "append"

print(marcasMoto)
marcasMoto.append('Suzuki')
print(marcasMoto)

# Para insertar elemento a una lista en cualquier posición utilizaremos la funcion insert()
marcasMoto.insert(1, 'Harley Davidson')
print(marcasMoto)

# Para eliminar el elemento de una lista

del marcasMoto[0]  # Si conoces la posición podemos usar la funcion del
print(marcasMoto)

# Podemos usar la funcion pop() para sacar el ultimo elemento de la lista.
# La diferencia de del es que ese elemento que hemos sacadao de la lista se puede seguir usando
objetoAppend = marcasMoto.pop()
print(marcasMoto)
print(objetoAppend)
