dic = {'perro': 'ladra', 'gato': 'maulla'}

''' Obtener el valor de una clave '''
dic.get('perro') # ladra

''' Saber si una clave existe en el diccionario '''
'elefante' in dic # False

''' Obtener claves y valores '''
for clave, valor in dic.iteritems(): 
    print "El valor de la clave %s es %s" % (clave, valor)

''' Obtener las claves '''
dic.keys() # ['gato', 'perro']

''' Obtener los valores '''
dic.values() # ['maulla', 'ladra']

''' Obtener la cantidad de elementos '''
len(dic) # 2

''' Agregar un par clave-valor: '''
dic['gallina'] = 'cocotea'

''' Borrar un par clave-valor '''
del dic['gallina']

''' Imprimir de una forma legible en formato string '''
import json
print json.dumps(dic, indent=1)

