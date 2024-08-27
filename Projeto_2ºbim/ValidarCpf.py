resp = "S"
total = 0
v = 0
s1 = 0
val = ""
lm1 = [10,9,8,7,6,5,4,3,2]
lm2 = [11,10,9,8,7,6,5,4,3,2]
cpf9 = list()
dic = dict()
banco = list()
teste = list()
while "S" == resp:
    total += 1
    s1 = 0
    cpf9.clear()
    cpf = input("Digite um CPF: EX(12345678910)")
    
    while not cpf.isnumeric() or len(cpf) != 11 :
        cpf = input("Siga o exemplo: EX(12345678910)")
        
    for x in range (0,9) :
        cpf9.append(int(cpf[x]))
        s1 = cpf9[x]*lm1[x]+s1
    if s1%11<2 :
        pg = 0
    else :
        pg = 11 - (s1%11)
    cpf9.append(pg)
    
    s1 = 0
    for x in range (0,10) :
        s1 = cpf9[x]*lm2[x]+s1
    if s1%11<2 :
        pg = 0
    else :
        pg = 11 - (s1%11)
    cpf9.append(pg)
   
    if int(cpf[9]) == cpf9[9] and int(cpf[10]) == cpf9[10]:
        val = "Valido"
        v += 1
    else :
        val  = "Invalido"
    teste.append(int(cpf)) 
    dic["CPF"] = teste [:]
    dic["Validação"] = val
    banco.append(dic.copy())
    teste.clear()
    resp = input("Deseja testar outro CPF ? (S/N)")
    while "S" != resp and "N" != resp :
        resp = input("Valor invalido!!!! Digite (S/N):")
    print("=================================================================")
print (banco)
print (f"Numero de CPFs testados : {total}")
print (f"Numero de CPFs validos : {v}")
print (f"Numero de CPFs invalidos : {total-v}")
pv = v*100/total
pi = (total-v)*100/total
print (f"Porcentagem de validos : {pv:.2f}%\nPorcentagem de invalidos : {pi:.2f}%")