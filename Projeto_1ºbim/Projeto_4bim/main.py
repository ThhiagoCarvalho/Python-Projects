qtd = input ("deseja de cadastrar quantos alunos na tabela excel ?:")
rm = input("Digite seu rm")
nome = input("digite seu nome")
notas_pvb = input("digite sua nota na materia pvb:")
notas_pooi = input("digite sua nota na materia pooi:")
notas_paw = input("digite sua nota na materia paw:")
notas_bd= input("digite sua nota na materia bd:") 

media = int (notas_bd + notas_paw + notas_pooi + notas_pvb) /4
aluno = {"MATRICULA" : rm , "ALUNOS":nome , "PVB": notas_pvb , "PAW":notas_paw,"BD":notas_bd, "POOI":notas_pooi}
arquivo = open(f"C:/")
open(f&#39;C:/Users/PC/Desktop/python-
projects/Listas/{nomeArquivo}&#39;, &#39;w&#39; , encoding=&#39;utf-8&#39;)