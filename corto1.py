#Corto numero1
#Marco Vinicio Fuentes Colchaj 201503432
#numeros a evaluar seran 432

n = 432
primero = 0
segundo = 0
tercero = 0
lista_prim = []
lista_seg = []
lista_ter= []
par =0
impar=0

primero = n%10
print(primero)
    
segundo = n%100
segundo  = segundo//10
print(segundo)

tercero = n//100
print(tercero)
#---------------------------
if(primero%2==0):
    primero =primero/2
else:
    primero=primero*3+1
if(primero==1):
    lista_prim=[primero]
#---------------------------
if(segundo%2==0):
    segundo=segundo/2
else:
    segundo=segundo*3-1
if segundo==1:
    lista_seg=[segundo]

#------------------------------
if(tercero%2==0):
    tercero=tercero/2
else:
    tercero=tercero*3+1
if tercero ==1:
    lista_ter=[tercero]


file=open("listado.txt","w")
file.write(str(lista_prim))
file.write(str(lista_seg))
file.write(str(lista_ter))
file.close()
    



