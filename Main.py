def media(lista):
    valor = 0
    index = 1
    for i in lista:
        idx = str(index) + ":"
        print("Nota",idx, i)
        valor += i
        index += 1
    print("Media:","{:.2f}".format(valor/len(lista)))

n = int(input())

lista = []
if not n == 0:
    for i in  range(n):
        lista.append(float(input()))
    media(lista)
else:
    print("Numero de notas invalido.")

