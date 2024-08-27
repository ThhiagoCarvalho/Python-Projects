import mysql.connector
from mysql.connector import Error
from prettytable import PrettyTable

def abrirBancoDXP():
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


def ReadAll():
    grid= PrettyTable(["ID disciplinaxprofessor", "Curso", "Carga horaria", "ano Letivo ", "idProfessor", "idDisciplina"])
    try:
        cursor = connection.cursor()
        Sql_select_query = '''select * from disciplinasxprofessores'''
        cursor.execute(Sql_select_query)
        tabela = cursor.fetchall()
        if cursor.rowcount > 0:
            for registro in tabela:
                grid.add_row([registro[0],registro[1],registro[2],registro[3],registro[4],registro[5]])
            print(grid)
        else:
            print("Por enquanto, nao ha disciplinas/professores cadastradas!")
    except Exception as error:
        print(f"Ocorreu um erro! {error}")

def Readbyid(iddisciplinasxprofessores = 0):
    grid= PrettyTable(["ID professor", "Curso", "Carga horaria", "ano Letivo ", "idProfessor", "idDisciplina"])
    try:
        cursor = connection.cursor()
        Sql_select_query = f'''select * from disciplinasxprofessores where iddisciplinasxprofessores = {iddisciplinasxprofessores}'''
        cursor.execute(Sql_select_query)
        tabela = cursor.fetchall()
        if cursor.rowcount > 0:
            for registro in tabela:
                grid.add_row([registro[0],registro[1],registro[2],registro[3],registro[4],registro[5]])
            print(grid)
            return  "c"
        else:
            return "nc"
    except Exception as error:
        print(f"Ocorreu um erro! {error}")
def ISprofessordisciplina (idProfessor,idDisciplina):

    try:
        cursor = connection.cursor()
        Sql_select_query = f"""select count(*) from disciplinasxprofessores where ID_idprofessor = {idProfessor} and ID_iddisciplina = {idDisciplina} """
        cursor.execute(Sql_select_query)
        tabela = cursor.fetchall()

        if len(tabela) > 0:
            print("0")
            return 0
        else:
            print("1")

            return 1
    except Exception as error:
        print(f"Ocorreu um erro! {error}")
def cadastrarDXP (*x):
    if  verificarExistenciaProfessor(idProfessores) <1:
        return f"Erro: ID do professor {x[4]} não existe."
    if  verificarExistenciaDisciplina(idDisciplina) <1:
        return f"Erro: ID da disciplina {x[5]} não existe."
    if (ISprofessordisciplina(x[4],x[5]) == 1):
        try:
            cursor = connection.cursor()
            Sql_insert_query = f"""insert into disciplinasxprofessores (iddisciplinasxprofessores, curso, cargaHoraria, anoLetivo,ID_idProfessor,ID_idDisciplina) values (%s,%s,%s,%s,%s,%s)"""
            cursor.execute(Sql_insert_query,x)
            connection.commit()
            return"cadastramento feito com sucesso!"
        except Exception as error:
            print(f"erro = {error}")
            return "cadastro falhado!"
    else:
        print(f"ja existe uma combinacao! de {x[4]} e {x[5]}")

def updateDXP(iddisciplinasxprofessores = 0,curso= 0,cargaHoraria=0,anoLetivo=0):
    try:
        cursor = connection.cursor()
        Sql_update_query = f"""update disciplinasxprofessores set  curso={curso}, cargaHoraria={cargaHoraria}, anoLetivo = {anoLetivo},
        where iddisciplinasxprofessores = {iddisciplinasxprofessores}"""
        cursor.execute(Sql_update_query)
        connection.commit()
        return"alteraco feito com sucesso!"
    except Exception as error:
        print(f"erro = {error}")
        return "Nao foi possivel realizar a alteracao!"
def excluirDXP (iddisciplinasxprofessores = 0):
     try:
        cursor = connection.cursor()
        Sql_delete_query = f"""delete from disciplinasxprofessores where iddisciplinasxprofessores = {iddisciplinasxprofessores}"""
        cursor.execute(Sql_delete_query)
        connection.commit()
        return "Exclusao feita com sucesso!"
     except Exception as error:
         print(f"Erro = {error}")
         return "Falha ao excluir o professor!"
def listarProfessores():
    grid= PrettyTable(["ID professor", "Nome Professor", "telefone Professor", "salario Professor", "idade Professor"])
    try:
        cursor = connection.cursor()
        Sql_select_query = '''SELECT * FROM professores'''
        cursor.execute(Sql_select_query)
        professores = cursor.fetchall()
        if cursor.rowcount > 0:
            for registro in professores:
                grid.add_row([registro[0],registro[1],registro[2],registro[3],registro[4]])
            print(grid)
        else:
            print("Nenhum professor cadastrado!")
    except Exception as error:
        print(f"Ocorreu um erro ao listar os professores! {error}")

def listarDisciplinas():
    grid= PrettyTable(["ID disciplina", "nome Disciplina"])
    try:
        cursor = connection.cursor()
        Sql_select_query = '''SELECT idDisciplina, nomeDisciplina FROM disciplinas'''
        cursor.execute(Sql_select_query)
        disciplinas = cursor.fetchall()
        if cursor.rowcount > 0:
            for registro in disciplinas:
                grid.add_row([registro[0], registro[1]])
            print(grid)
        else:
            print("Nenhuma disciplina cadastrada!")
    except Exception as error:
        print(f"Ocorreu um erro ao listar as disciplinas! {error}")

def verificarExistenciaProfessor (idProfessor):
    try:
        cursor = connection.cursor()
        Sql_select_query = f"""select count(*) from professores where idProfessor = {idProfessor}"""
        cursor.execute(Sql_select_query)
        resultado = cursor.fetchone()
        if resultado[0] > 0:
            return 1
        else:
            return 0
    except Exception as error:
        print(f"Ocorreu um erro! {error}")
        return False
def verificarExistenciaDisciplina (idDisciplina):
    try:
        cursor = connection.cursor()
        Sql_select_query = f"""select count(*) from disciplinas where idDisciplina = {idDisciplina}"""
        cursor.execute(Sql_select_query)
        resultado = cursor.fetchone()
        if resultado[0] > 0:
            return 1
        else:
            return 0
    except Exception as error:
        print(f"Ocorreu um erro! {error}")
        return False



if abrirBancoDXP() == 1:
    listarDisciplinas()
    print()

    listarProfessores()
    print("\n\n")

    print("( 1-disciplinas | 2-professores | 3-disciplinasxprofessores | 4-sair)")
    print('=' * 100)
    resp = input("Digite conforme a consulta :")
    while not resp.isnumeric() or int(resp) < 1 or int(resp) > 4:
        resp = input("DIGITE CORRETAMENTE a consulta ( 1-disciplinas | 2-professores | 3-disciplinasxprofessores | 4-sair")
    while (True):
        if resp == '3':
                print('=' * 80)
                print('{:^80}'.format('SISTEMA UNIVAP - iddisciplinasxprofessores'))
                print('=' * 80)
                iddisciplinasxprofessores = input("Digite o codigo do curso que deseja ver | 0-- todos")
                while not iddisciplinasxprofessores.isnumeric():
                    iddisciplinasxprofessores = input("DIGITE CORRETAMENTE  o codigo do curso que deseja | 0-- todos")
                    break
                if (int(iddisciplinasxprofessores) == 0):
                    ReadAll()

                    resp = input("Deseja continuar o programa? 1- sim | 2-nao")
                    while int(resp) != 1 and int(resp) != 2:
                        resp = input("RESPOTSA INEXSISTENTE | Deseja continuar o programa? 1- sim | 2-nao")
                    if int(resp) == 1:
                        continue
                    elif int(resp) == 2:
                        resp = input(
                            "Deseja realmente finalizar o programa? (1-disciplinas | 2-professores | 3-disciplinasxprofessores | 4-FINALIZAR ")
                        while int(resp) < 1 or int(resp) > 4:
                            resp = input(
                                "DIGITE CORRETAMENTE!! |Deseja realmente finalizar o programa? (1-disciplinas | 2-professores | 3-disciplinasxprofessores | 4-FINALIZAR ")
                        if int(resp) != 4:
                            continue
                        elif int(resp) == 4:
                            break
                if(Readbyid(int(iddisciplinasxprofessores)) == "nc"):
                    curso = input("Digite o nome do curso:")
                    while not curso.isalpha():
                        curso = input("Digite CORRETAMENTE o nome do curso:")

                    cargaHoraria = input("Digite a cargaHoraria do curso:")
                    while not cargaHoraria.isnumeric():
                        cargaHoraria = input("Digite CORRETAMENTE a cargaHoraria do curso:")

                    anoLetivo = input("Digite a anoLetivo do curso:")
                    while not anoLetivo.isnumeric():
                        anoLetivo = input("Digite CORRETAMENTE a anoLetivo do curso:")

                    listarProfessores()
                    idProfessores = input("Digite o ID do professor: ")
                    while not idProfessores.isnumeric() or not verificarExistenciaProfessor(int(idProfessores)):
                        idProfessores = input(
                            "ID do professor não existe ou não é válido. Digite CORRETAMENTE o ID do professor: ")

                    listarDisciplinas()
                    idDisciplina = input("Digite o ID da disciplina: ")
                    while not idDisciplina.isnumeric() or  verificarExistenciaDisciplina(int(idDisciplina)) < 1:
                        idDisciplina = input("ID da disciplina não existe ou não é válido. Digite CORRETAMENTE o ID da disciplina: ")

                    resposta= cadastrarDXP(int(iddisciplinasxprofessores),curso,int(cargaHoraria),int(anoLetivo),idProfessores,idDisciplina)
                    print(resposta)
                else:
                    opcao = input("Escolha: [A]-Alterar [E]-Excluir [C]-Cancelar Operações ==> ")
                    while opcao not in "AEC":
                        opcao = input("ESCOLHA CORRETAMENTE: [A]-Alterar [E]-Excluir [C]-Cancelar Operações ==> ")
                    if opcao == "A":
                        print("'Atenção: Código da disciplina não pode ser alterado:")
                        curso = input("digite novamente o nome do professor:")
                        cargaHoraria = input("Digite novamente  o telefone do professor:")
                        idadeprof = input("Digite novamente  a idade do professor:")
                        anoLetivo = input("Digite novamente o salario do professor:")
                        ID_idprofessor = input("Digite CORRETAMENTE o id do professor:")
                        ID_iddisciplina = input("Digite CORRETAMENTE o id da disciplina:")

                        resposta = updateDXP(int(iddisciplinasxprofessores),curso,int(cargaHoraria),int(anoLetivo))
                        print(resposta)
                    elif opcao == "E":
                        confirma = input("Deseja mesmo exculuir?!! 1-sim | 2-nao")
                        while int(confirma) != 1 and int(confirma) != 2:
                            confirma = input("RESPOSTA INEXSISTENTE | Deseja mesmo exculuir?!! 1-sim | 2-nao")
                        if confirma == "1":
                            resposta = excluirDXP(int(iddisciplinasxprofessores))
                            print(resposta)
                    print('\n')
                    print('=' * 80)
                    resp = input("Deseja continuar o programa? 1- sim | 2-nao")
                    while int(resp) != 1 and int(resp) != 2:
                        resp = input("RESPOTSA INEXSISTENTE | Deseja continuar o programa? 1- sim | 2-nao")
                    if int(resp) == 1:
                        continue
                    else:
                        break
        elif resp == '1':
            import CRUD_Disciplina
            CRUD_Disciplina.main()
            break
        elif resp == '2':
           import CRUD_Professor
           CRUD_Professor.main()
        elif resp == '4':
            print('FIM DO PROGRAMA!!!')

else:
    print('FIM DO PROGRAMA!!! Algum problema existente na conexão com banco de dados.')