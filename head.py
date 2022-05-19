def get_int():
    try:
        try:
            integer = sys.argv[2]
            integer = int(integer)
            return integer 
             
        except:
            print("",end="")                
    except:
        pass

import sys; lenght = len(sys.argv)-1
filename = ""
if lenght == 1:
    filename = sys.argv[1]

elif lenght == 3:
    filename = sys.argv[3]
    if sys.argv[1] == "-n":
        pass

    else:
        sys.exit("use a opcao -n (lines number)")
else:
    sys.exit(f"use: python3 {sys.argv[0]} file")

numero, n = 0, get_int();
if n == None: n = 10; 
try:
    file = open(filename,"rb")
except FileNotFoundError:
    sys.exit("File not found")

y, dd = 0,0; d=[]; fileread = file.read(); fileread = fileread.decode("ascii"); x=[0]
while fileread.count("\n") > y:
    vari = fileread[dd:]
    a=vari.find("\n")
    k = x[-1]
    x.append(k+a+1)
    d.append(a)
    dd = dd + a+1
    y+=1

x = x[1:]; lista = fileread; tamanho = len(d); print(lista[:-1]) if tamanho <= 10 else print(lista[:x[n-1]],end="")
