import mysql.connector
from mysql.connector import Error
from prettytable import PrettyTable




def abrirBancoProfessor():
   try:
       global connection
       connection = mysql.connector.connect(host='localhost', database='BancoUnivap', user='root', password='root123')
       if connection.is_connected():
           global cursor
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




def ReadAll():
   grid = PrettyTable(["ID professor", "Nome Professor", "telefone Professor", "salario Professor", "idade Professor"])
   try:
       cursor = connection.cursor()
       Sql_select_query = '''select * from professores'''
       cursor.execute(Sql_select_query)
       tabela = cursor.fetchall()
       if cursor.rowcount > 0:
           for registro in tabela:
               grid.add_row([registro[0], registro[1], registro[2], registro[3], registro[4]])
           print(grid)
       else:
           print("Por enquanto, nao ha professores cadastrados!")
   except Exception as error:
       print(f"Ocorreu um erro! {error}")




def Readbyid(idProfessor=0):
   grid = PrettyTable(["ID professor", "Nome Professor", "telefone Professor", "salario Professor", "idade Professor"])
   try:
       cursor = connection.cursor()
       Sql_select_query = f'''select * from professores where idProfessor = {idProfessor}'''
       cursor.execute(Sql_select_query)
       tabela = cursor.fetchall()
       if cursor.rowcount > 0:
           for registro in tabela:
               grid.add_row([registro[0], registro[1], registro[2], registro[3], registro[4]])
           print(grid)
           return "c"
       else:
           return "nc"
   except Exception as error:
       print(f"Ocorreu um erro! {error}")




def cadastrarProfessor(*x):
   try:
       cursor = connection.cursor()
       Sql_insert_query = f"""insert into professores (idProfessor, nomeProfessor, telefoneProfessor, idadeProfessor, salarioProfessor) values (%s,%s,%s,%s,%s)"""
       cursor.execute(Sql_insert_query, x)
       connection.commit()
       return "cadastramento feito com sucesso!"
   except Exception as error:
       print(f"erro = {error}")
       return "cadastro falhado!"




def updateProfessor(idprof=0, nomeprof='', telProf='', idadeProf=0, salProf=0):
   try:
       cursor = connection.cursor()
       Sql_update_query = f"""update professores set  nomeProfessor='{nomeprof}', telefoneProfessor='{telProf}', idadeProfessor = {idadeProf}, salarioProfessor = {salProf} where idProfessor = {idprof}"""
       cursor.execute(Sql_update_query)
       connection.commit()
       return "alteraco feito com sucesso!"
   except Exception as error:
       print(f"erro = {error}")
       return "Nao foi possivel realizar a alteracao!"




def excluirProfessor(idProfessor=0):
   try:
       cursor = connection.cursor()
       Sql_delete_query = f"""delete from professores where idProfessor = {idProfessor}"""
       cursor.execute(Sql_delete_query)
       connection.commit()
       return "Exclusao feita com sucesso!"
   except Exception as error:
       print("\n")
       print('=' * 80)

       print(f"Erro = {error}")
       return "Falha ao excluir o professor!"
       print('=' * 80)




if abrirBancoProfessor() == 1:
    print("\n")
    print('=' * 80)
    print('{:^80}'.format('SISTEMA UNIVAP - PROFESSORES'))
    print('=' * 80)
    while (True):
        codigoProf = input("Digite o codigo do professor que deseja ver | 0-- todos:")
        while not codigoProf.isnumeric():
           codigoProf = input("DIGITE CORRETAMENTE  o codigo da professor que deseja | 0-- todos:")
           break

        if (int(codigoProf) == 0):
            ReadAll()
            resp = input("Deseja continuar o programa? (1-sim | 2-nao):")
            while int(resp) != 1 and int(resp) != 2:
               resp = input("RESPOTSA INEXSISTENTE | Deseja continuar o programa? (1-sim | 2-nao):")
            if int(resp) == 1:
                print('=' * 80)
                print('\n')
                continue
            elif int(resp) == 2:
                break

        if (Readbyid(int(codigoProf)) == "nc"):
            nomeProf = input("Digite o nome do professor:")
            while not nomeProf.isalpha():
               nomeProf = input("Digite CORRETAMENTE o nome do professor:")

            telprof = input("Digite o telefone do professor:")
            while not telprof.isnumeric():
               telprof = input("Digite CORRETAMENTE o telefone do professor:")

            idadeprof = input("Digite a idade do professor:")
            while not idadeprof.isnumeric():
               idadeprof = input("Digite CORRETAMENTE o idade do professor:")


            sal = input("Digite o salario do professor:")
            while not sal.isnumeric():
               sal = input("Digite CORRETAMENTE o salario do professor:")


            resposta = cadastrarProfessor(int(codigoProf), nomeProf, telprof, int(idadeprof), float(sal))
            print('\n')
            print(resposta)
            print('=' * 80)
        else:
            opcao = input("Escolha: [A]-Alterar [E]-Excluir [C]-Cancelar Operações ==> ")
            while opcao not in "AEC":
                opcao = input("ESCOLHA CORRETAMENTE: [A]-Alterar [E]-Excluir [C]-Cancelar Operações ==> ")
            if opcao == "A":
                print("'Atenção: Código da disciplina não pode ser alterado:")
                nomeProf = input("digite novamente o nome do professor:")
                telprof = input("Digite novamente  o telefone do professor:")
                idadeprof = input("Digite novamente  a idade do professor:")
                sal = input("Digite novamente o salario do professor:")
                resposta = updateProfessor(int(codigoProf), nomeProf, telprof, int(idadeprof), int(sal))
                print('\n')
                print(resposta)
                print('=' * 80)
                
            elif opcao == "E":
                confirma = input("Deseja mesmo exculuir?!! (1-sim | 2-nao):")
                while int(confirma) != 1 and int(confirma) != 2:
                    confirma = input("RESPOSTA INEXSISTENTE | Deseja mesmo exculuir?!! (1-sim | 2-nao):")
                if confirma == "1":
                    resposta = excluirProfessor(int(codigoProf))
                    print(resposta)
                print('\n')
                print('='*80)
                resp = input("Deseja continuar o programa? (1-sim | 2-nao):")
                while int(resp)!= 1 and int(resp)!=2:
                    resp = input("RESPOTSA INEXSISTENTE | Deseja continuar o programa? (1-sim | 2-nao):")
                if int(resp) == 1:
                    continue
                elif int(resp) ==2 :
                    connection.close() 
                    cursor.close()
                    break
else:
   print('FIM DO PROGRAMA!!! Algum problema existente na conexão com banco de dados.')
