text = 'Ella sabe Python'
print(text[0]) # 0 es la 1ra posicion, retorna el caracter
print(text[1]) # la siguiente posicion
#print(text[999]) #lanza error xq la posicion no existe


# aber ultimo caracter del texto
size = len(text)
print('size => ', size)
print(text[size - 1])
print(text[-1])

# SLICING

print(text[0:5]) # se obtiene el subtexto de las posiciones mencionadas
print(text[10:16])
print(text[:10]) #si no se envia nada en automatico toma desde el inicio hasta el caracter
print(text[5:]) #desde el 1er punto hasta el final
print(text[:]) #el mismo string desde el inicio hasta el final
print(text[10:16:1]) #cuantos caracteres saltar hacia el siguiente
print(text[10:16:2])
print(text[::2]) #desde inicio hasta el final saltando dos elementos