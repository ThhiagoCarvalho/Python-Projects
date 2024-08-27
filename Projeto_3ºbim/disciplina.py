import mysql.connector
from mysql.connector import Error
from prettytable import PrettyTable



def openBanco():
   try:
       global connection
       connection = mysql.connector.connect(host='localhost', database='BancoUnivap', user='root', password='root123')
       if connection.is_connected():
           cursor = connection.cursor()
           Sql_select_query = """select database() """
           cursor.execute(Sql_select_query)
           nomeBanco = cursor.fetchone()
           print(f"Banco acesado {nomeBanco}")
           return 1
       else:
           print("Conexao falhada!")
           return 0


   except Exception as erro:
       print(f" Erro {erro}")
       return 0


def ReadALL():
   grid = PrettyTable(["ID disciplinas ", "Nome Disciplina"])
   try:
       cursor = connection.cursor()
       Sql_select_quey = "select * from disciplinas"
       cursor.execute(Sql_select_quey)
       tabela = cursor.fetchall()
       if cursor.rowcount > 0:
           for registro in tabela:
               grid.add_row([registro[0],registro[1]])
           print(grid)
       else:
           print("Por enquanto, nao ha disciplinas cadastradas!")
   except Exception as error:
       print(f"Ocorreu um erro! {error}")


def ReadbyID (idDisciplina = 0):
   grid = PrettyTable(["ID disciplinas ", "Nome Disciplina"])
   try:
       cursor = connection.cursor()
       Sql_select_quey = f"""select * from disciplinas where idDisciplina = {idDisciplina}"""
       cursor.execute(Sql_select_quey)
       tabela = cursor.fetchall()
       if cursor.rowcount > 0:
           for registro in tabela:
               grid.add_row([registro[0],registro[1]])
           print(grid)
           return  "c"
       else:
           return "nc"
   except Exception as error:
       print(f"Ocorreu um erro! {error}")


def cadastrarDisciplina(idDisciplina = 0 , nomeDisciplina=''):
   try:
       cursor = connection.cursor()
       Sql_insert_query = f"""insert into disciplinas (idDisciplina , nomeDisciplina) values ({idDisciplina},'{nomeDisciplina}')"""
       cursor.execute(Sql_insert_query)
       connection.commit()
       return "Cadastro da disciplina feito com sucesso!"
   except Exception as error:
       print(f"erro ao cadastrar {error}")
       return "Nao foi possivel realizar o cadastro!"


def alterarDisciplina(idDisciplina = 0 , nomeDisciplina=''):
   try:
       cursor = connection.cursor()
       Sql_insert_query = f"""update disciplinas set nomeDisciplina='{nomeDisciplina}' where idDisciplina = {idDisciplina}"""
       cursor.execute(Sql_insert_query)
       connection.commit()
       return "Disciplina alterada com sucesso!"
   except Exception as error:
       print(f"erro ao cadastrar {error}")
       return "Nao foi possivel realizar a alteracao!"


def excluirDisciplina (idDisciplina = 0):
   try:
       cursor = connection.cursor()
       Sql_delete_query = f"""delete from disciplinas where idDisciplina = {idDisciplina}"""
       cursor.execute(Sql_delete_query)
       connection.commit()
       return "Exclusao feita com sucesso!"
   except Exception as error:
       print(f"erro = {error}")
       return "Nao foi possivel realizar a exclusao!"




if openBanco() == 1:
    resp = input("Digite conforme a consulta ( 1-disciplinas | 2-professores | 3-disciplinasxprofessores | 4-sair )")
    while not resp.isnumeric() or int(resp) < 1 or int(resp) > 4:
        resp = input(
            "DIGITE CORRETAMENTE a consulta ( 1-disciplinas | 2-professores | 3-disciplinasxprofessores | 4-sair")

    while(True):
       if resp == '1':
           print('=' * 80)
           print('{:^80}'.format('SISTEMA UNIVAP - DISCIPLINAS'))
           print('=' * 80)
           codigoDisc = input("Digite o codigo da disciplina que deseja ver | 0-- todas")
           while not codigoDisc.isnumeric():
               codigoDisc = input("DIGITE CORRETAMENTE  o codigo da disciplina que deseja | 0-- todas")
               break
           if int(codigoDisc)== 0:
               ReadALL()

               resp = input("Deseja continuar o programa? 1- sim | 2-nao")
               while int(resp)!= 1 and int(resp)!=2:
                   resp = input("RESPOTSA INEXSISTENTE | Deseja continuar o programa? 1- sim | 2-nao")
               if int(resp) == 1:
                   continue
               elif int(resp) ==2 :
                   resp = input("Deseja realmente finalizar o programa? (1-disciplinas | 2-professores | 3-disciplinasxprofessores | 4-FINALIZAR ")
                   while int(resp) <1 or int(resp) >4:
                       resp = input ("DIGITE CORRETAMENTE!! |Deseja realmente finalizar o programa? (1-disciplinas | 2-professores | 3-disciplinasxprofessores | 4-FINALIZAR ")
                   if int(resp)!=4:
                       continue
                   elif int(resp) == 4:
                       print('FIM DO PROGRAMA!!!')
                       break
           if ReadbyID(int(codigoDisc)) == 'nc':
               nomeDisciplina = input("Digite o nome da disciplina")
               resposta = cadastrarDisciplina(int(codigoDisc),nomeDisciplina)
               print(resposta)
           else:
               opcao = input("Escolha: [A]-Alterar [E]-Excluir [C]-Cancelar Operações ==> ")
               while opcao not in "AEC":
                   opcao = input("ESCOLHA CORRETAMENTE: [A]-Alterar [E]-Excluir [C]-Cancelar Operações ==> ")
               if opcao == "A":
                   print("'Atenção: Código da disciplina não pode ser alterado:")
                   nomeDisciplina = input("digite novamente o nome da disciplina:")
                   resposta = alterarDisciplina(int(codigoDisc),nomeDisciplina)
                   print(resposta)
               elif opcao == "E":
                   confirma = input("Deseja mesmo exculuir?!! 1-sim | 2-nao")
                   while int(confirma) != 1  and int(confirma)!=2:
                       confirma = input("RESPOSTA INEXSISTENTE | Deseja mesmo exculuir?!! 1-sim | 2-nao")
                   if confirma == "1":
                       resposta = excluirDisciplina(int(codigoDisc))
                       print(resposta)
               print('\n\n')
               print('=' * 80)

       elif resp == '2':
           import CRUD_Professor
           CRUD_Professor.main()
       elif resp == '3':
           import CRUD_ProfessorXDisciplina
           CRUD_ProfessorXDisciplina.main()
       else:
            print('FIM DO PROGRAMA!!!')
            break

else:
   print('FIM DO PROGRAMA!!! Algum problema existente na conexão com banco de dados.')
