
valor = 1543

if valor > 1.000:
    
    t1= valor//1000
    valor = valor % 1000
    print(t1)
else:
    print("0")
    
if valor > 500:
    t2= valor//500
    valor = valor % 500
    print(t2)
else:
    print("0")
    
if valor > 200:
    t3= valor//200
    valor = valor % 200
    print(t3)
else:
    print("0")
    
if valor > 100:
    t4= valor//100
    valor = valor % 100
    print(t4)
else:
    print("0")
    
t5= valor//50
valor = valor % 50
print(t5)
print(valor)