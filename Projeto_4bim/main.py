from openpyxl import Workbook, load_workbook
import pandas as pd

alunos_lista = []

qtd = int(input("Deseja cadastrar quantos alunos na tabela Excel?: "))
for cont in range(qtd):
    print("=-"*60)
    rm = input(f"Digite o RM do {cont+1}º aluno: ")
    nome = input(f"Digite o nome do {cont+1}º aluno: ")
    notas_pvb = float(input(f"Digite a nota do aluno {nome} na matéria PVB: "))
    notas_pooi = float(input(f"Digite a nota do aluno {nome} na na matéria POOI: "))
    notas_paw = float(input(f"Digite a nota do aluno {nome} na na matéria PAW: "))
    notas_bd = float(input(f"Digite a nota do aluno {nome} na matéria BD: "))
    
    media = (notas_bd + notas_paw + notas_pooi + notas_pvb) / 4

    aluno = [rm, nome, notas_pvb, notas_pooi, notas_paw, notas_bd, media]
    print(aluno)

    alunos_lista.append(aluno) 
    print(alunos_lista)

caminho_arquivo = "C:/Users/PC/Documents/POOI_Projects/Python-Projects/Projeto_4bim/NOTASFINAISALUNOS.xlsx"

print("1- Adicionar os dados em uma planilha nova \n2- Adicionar os dados em planilha existente\n")
resp = input("Digite sua escolha (1 ou 2): ")

if resp == "1":
    wb = Workbook()
    ws = wb.active
    ws.title = "NOTASFINAISALUNOS"
    
    # Adiciona cabeçalho
    ws.append(["MATRICULA", "ALUNOS", "PVB", "PAW", "BD", "POOI", "MEDIA"])
    
    for aluno in alunos_lista:
        ws.append(aluno)  
    
    wb.save(caminho_arquivo)

    df = pd.read_excel(caminho_arquivo)
    print(df)

elif resp == "2":
    try:
        wb = load_workbook(caminho_arquivo)
        ws = wb["NOTASFINAISALUNOS"]
        
        for aluno in alunos_lista:
            ws.append(aluno)  
        
        wb.save(caminho_arquivo)
    
        df = pd.read_excel(caminho_arquivo)
        print(df)

    except FileNotFoundError:
        print("Erro: Arquivo não encontrado. Certifique-se de que o caminho está correto.")
