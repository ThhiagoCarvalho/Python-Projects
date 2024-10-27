from openpyxl import Workbook, load_workbook
import pandas as pd
situcao = "REPROVADO"
alunos_lista = []
situcao = ""
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
    if (media > 3.75 and media <=5.9):
        situcao = "EXAME FINAL"
    elif(media >= 6):
        situcao = "APROVADO"
        
    aluno = [rm, nome, notas_pvb, notas_pooi, notas_paw, notas_bd, media,situcao]
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


resp_html= input("deseja criar uma pagina html para demonstrar as notas? (s/n)")



if ( resp_html == 's') : 
    nomeArquivo = rm + ".html"
    arquivo = open(f'C:/Users/PC/Documents/POOI_Projects/Python-Projects/Projeto_4bim/{nomeArquivo}', 'w' , encoding='utf-8')
    body = ''

    background = "rgb(29, 99, 192)"
    if (media > 3.75 and media <=5,9):
        background = "yellow"
    elif(media < 3.75):
        background = "red"

    html = f"""
    <!DOCTYPE html>
    <html lang="UTF-8">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Notas Finais</title>

        <style>
        body{{    
            text-align: center;
            display: block;
            justify-content: center;
            align-items: center;
        }}
        p{{margin-bottom : 40px}}

        table{{
            margin: auto;
            background-color: {background};
            border-collapse:collapse;

        }}
        tr{{
            border: 1px solid;
        }}

        #red {{
            background-color: red
        }}
            #situacao {{
            background-color: {background};
        }}
        </style>
    </head>
    <body>
       <p> MATRICULA  : {rm}</p>
       <p>ALUNO: <span id="red">{nome}</span></p>

       
       <table>
       <theads>
        <th>PVB</th>
        <th>PAW</th>
        <th>BD</th>
        <th>POOI</th>
        <th>MEDIA</th>
        </theads>
        <tr>
        <td> {notas_pvb} </td>
        <td> {notas_paw} </td>
        <td> {notas_bd}</td>
        <td> {notas_pooi}</td>
        <td> {media}</td>
        </tr>
       </table>

       <p> SITUACAO FINAL  <span id="situacao">{situcao}</span> </p>

    </body>

    </html>"""


    arquivo.write(html)
    print(f"Arquivo '{nomeArquivo}' criado com sucesso!")
    arquivo.close()
