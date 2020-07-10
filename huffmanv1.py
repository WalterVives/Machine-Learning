import pprint
from collections import Counter
"""
This version of huffman coding was made with lists, list of tuples and dictionaries.
"""


def frequency(string):
    """
                        parametro    : un string
                        return       : frecuencia de cada char ordenado (lista de tuplas).
    """
    total_char = []
    lista = list(string)
    counter = Counter(lista)
    for i in counter.items():
        total_char.append(i)
    total_char.sort(key=lambda x: x[1])

    return total_char


def nodes(base):

    """
                        parametro    : una lista de tuplas otrdenadas por frecuencia.
                        return       : diccionario con el valor de cada nodo y lista del arbol, (tupla)s
    """

    # inicializando el dic con las letras totales.
    letras = list(map(lambda w: w[0], base))
    letras_totales = "".join(letras)
    #print("letras totales: ", letras_totales)
    dic = dict.fromkeys(letras_totales, "")
    contador = len(base)
    lista_arbol = []

    # agregando los dos primeros valores al diccionario.
    if base[0][0] in dic:
        dic[base[0][0]] +="0"
    if base[1][0] in dic:
        dic[base[1][0]] += "1"

    # lugar 0 y 1 de cada iteración, esto corresponde a
    # el recorrido del arbol.
    lista_arbol.append(base[0])
    lista_arbol.append(base[1])

    for i in range(contador-2):
        if base[0][1] <= base[1][1]:
            letras = base[0][0] + base[1][0]
            numeros = base[0][1] + base[1][1]
            nuevos = tuple([letras, numeros])
            base.insert(0,nuevos)
            base.pop(1)
            base.pop(1)

            # ordenando de nuevo
            base.sort(key=lambda x: x[1])    
            #print(base)

            # lugar 0 y 1 de cada iteración, esto corresponde a
            # el recorrido del arbol.
            lista_arbol.append(base[0])
            lista_arbol.append(base[1])
            
            # asignar los 0's y 1's acorde a su aparición.
            if base[0][0] in dic:
                dic[base[0][0]] += "0"
            else:
                dic[base[0][0]] = "0"
                
            if base[1][0] in dic:
                dic[base[1][0]] += "1" 
            else:
                dic[base[1][0]] = "1"


        else:
            print("F")
    #print("lista_arbol: ", lista_arbol)
    return (dic,lista_arbol)


def leaf_value(base, letras):

    """
                         parametro   : un diccionario con los valores de cada nodo, un string. 
                         return      : diccionario de codificación de cada letra.
    """

    counter = 0 
    s = frequency(letras)
    total_hojas = list(map(lambda x: x[0], s))
    node = list(map(lambda x: x[0], nodes(frequency(letras))[1]))
    #print("Node", node)
    #print("t", total_hojas)
    for i in range(len(node)):
        if len(node) != len(total_hojas):
            counter += 1 
            total_hojas.append(i)

    #print("Total hojas:", total_hojas)
    # diccionario que tendrá el valor de cada letra.
    diccionario = dict.fromkeys(total_hojas, "")

    for i in range(len(node)):
        for k in range(len(total_hojas)):
            #print(k, leaf[k])
            if type(total_hojas[i]) == type("a"):
                if total_hojas[i] in (node[k]):
                    #print(total_hojas[i],node[k])
                    diccionario[total_hojas[i]] += ((nodes(frequency(letras))[0])).get(node[k])

    keys = list(diccionario.keys())
    values = list(diccionario.values())

    # Eliminando las llaves extras tipo int.
    for i in range(counter):
        keys.pop()
        values.pop()

    # creando el diccionario final.
    values_reverse = list(map(lambda x: x[::-1], values))
    diccionario_final = dict(zip(keys, values_reverse))

    return diccionario_final
    

def huffman(diccionario, string):


    code = []
    for i in range(len(string)):
        if string[i] in diccionario:
            #print(diccionario[string[i]], end= " ")
            code.append(diccionario[string[i]])
    
    return code


def huffmanDecoding(dic, encoding):
    
    keys = list(dic.keys())
    values = list(dic.values())
    result = []

    for i in range(len(encoding)):
        for k in range(len(values)):
            if encoding[i] == values[k]:
                #print(list(dic.keys())[list(dic.values()).index(encoding[i])], end="")
                result.append(list(dic.keys())[list(dic.values()).index(encoding[i])])
    final = "".join(result)

    return final


def main():

    """
    ###################################################################################################################

                                    ############funciones############
    - frequency(string)
                        parametro    : un string
                        return       : frecuencia de cada char ordenado (lista de tuplas).
    
    - nodes(base)
                        parametro    : una lista de tuplas otrdenadas por frecuencia.
                        return       : diccionario con el valor de cada nodo y lista del arbol, (tupla)s


    - leaf_value(base)
                         parametro   : un diccionario con los valores de cada nodo, un string. 
                         return      : diccionario de codificación de cada letra.

    - huffman(diccionario,string)
                        parametro    : diccionario de valores y un string.
                        return       : una lista con la codificación de cada letra del string.

    - uffmanDecoding(dic, encoding)
                        parametro    : diccionario de los valores y la lista de valores codificados.
                        return       :

    ###################################################################################################################              
    """

    #string = "ASDF"
    #string = "BCCABBDDAECCBBAEDDCC"
    string = """Empty spaces, what are we living for?
Abandoned places, I guess we know the score, on and on
Does anybody know what we are looking for?
Another hero, another mindless crime
Behind the curtain, in the pantomime
Hold the line
Does anybody want to take it anymore?
The show must go on
The show must go on, yeah
Inside my heart is breaking
My makeup may be flaking
But my smile, still, stays on
Whatever happens, I'll leave it all to chance
Another heartache, another failed romance, on and on
Does anybody know what we are living for?
I guess I'm learning
I must be warmer now
I'll soon be turning, round the corner now
Outside the dawn is breaking
But inside in the dark I'm aching to be free
The show must go on
The show must go on
Inside my heart is breaking
My makeup may be flaking
But my smile, still, stays on
My soul is painted like the wings of butterflies
Fairy tales of yesterday, grow but never die
I can fly, my friends
The show must go on
The show must go on
I'll face it with a grin
I'm never giving in
On with the show
I'll top the bill
I'll overkill
I have to find the will to carry on
On with the show
Show
Show must go on, go on, go on, go on, go on, go on, go on, go on"""
    
    #print("diccionario de nodos:", nodes(frequency(letras))[0])
    diccionario = leaf_value((nodes(frequency(string))[0]), string)
    huffman_coding = huffman(diccionario, string)
    huffman_decoding = huffmanDecoding(diccionario, huffman(diccionario, string))

    print("\t\nHuffman coding\n\n")

    print("string: ", string)
    print("\n")
    print("diccionary of values: ", diccionario)
    print("\n")
    print("encoding: ", huffman_coding)
    print("\n")
    print("Huffman decoding:")
    print("\n")
    print(huffman_decoding)

if __name__ == "__main__":
    main()

