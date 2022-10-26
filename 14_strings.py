text = 'Ella sabe programar en Python'

'''
print('JavaScript' in text) #busca la palabra si esta dentro del texto
print('Python' in text)

if 'Python' in text:
    print('Elegiste bien!!')
else:
    print('Tambien elegiste bien')
'''

size = len(text) #tamano del texto
print(size)

print(text)
print(text.upper()) #pasa el texto a Mayusculas
print(text.lower()) #pasa el texto a Minusculas
print(text.count('a')) #cuenta cuantas repeticiones hay de un caracter especifico
print(text.swapcase()) #revierte entre mayusculas y minusculas
print(text.startswith('Ella')) #si el texto inicia con algo especifico
print(text.endswith('Rust')) #si finaliza con algo especifico
print(text.replace('Python', 'Go')) #reemplaza

text_2 = 'este es un titulo'
print(text_2)
print(text_2.capitalize()) #pone el 1er caracter en Mayuscula
print(text_2.title()) #inicio de cada palabra en Mayuscula
print(text_2.isdigit()) #evalua si el texto es un digito
print("398".isdigit())


