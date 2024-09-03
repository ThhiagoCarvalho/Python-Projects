try:
   print('=' * 80)
   print('{:^80}'.format('SISTEMA UNIVAP - MAIN'))
   print('=' * 80)
   while True:
       escolha = input("( 1-disciplinas | 2-professores | 3-disciplinasxprofessores | 4-sair):")
       while not escolha.isnumeric() or int(escolha) < 1 or int(escolha) > 4:
          resp = input(
              "DIGITE CORRETAMENTE a consulta ( 1-disciplinas | 2-professores | 3-disciplinasxprofessores | 4-sair):")
       if escolha == '1':
          import disciplina
          break

       elif escolha == '2':
          import professor
          break

       elif escolha == '3':
          import disciplinaxprofessor
          break

       elif escolha =='4':
           break
except Exception as erro :
    print(f" Erro {erro}")
