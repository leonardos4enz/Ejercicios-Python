crypt=["A", 
 "A", 
 "A"]

solutionn = [["A","0"]]

def solution(crypt, solution):
    diccionario = {}
    for i in range(len(solution)):
        diccionario[solution[i][0]]=solution[i][1]
    #print(diccionario)
    #print(diccionario.get(crypt[0][0]))
    suma = []
    numero = ""
    for i in range (len(crypt)):
        for j in range (len(crypt[i])):
            numero = numero + diccionario.get(crypt[i][j])
        #print(numero)
        suma.append(numero)
        if(numero.startswith("0") and len(numero)>1):
            #print("no da")
            return False
        numero = ""
    #print(suma)
    suma_numeros = 0
    for i in range(len(suma)-1):
        suma_numeros = suma_numeros + int(suma[i])
    #print(suma_numeros)
    if(suma_numeros == int(suma[len(suma)-1])):
        #print("si da")
        return True
    else:
        #print("no da")
        return False
solution(crypt,solutionn)
    