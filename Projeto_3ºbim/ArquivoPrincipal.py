import importlib
try:
  
   while True:
      print("\n")
      print('=' * 80)
      print('{:^80}'.format('SISTEMA UNIVAP - MAIN'))
      print('=' * 80)
      escolha = input("( 1-disciplinas | 2-professores | 3-disciplinasxprofessores | 4-sair):")
      while not escolha.isnumeric() or (int(escolha) < 1 or int(escolha) > 4):
         escolha = input("DIGITE CORRETAMENTE a consulta ( 1-disciplinas | 2-professores | 3-disciplinasxprofessores | 4-sair):")
      if escolha == '4':
         break
      elif escolha == '1':
         importlib.import_module('disciplina')
         print("voce finalizou as acoes nesta tabela disciplina")

      elif escolha == '2':
         importlib.import_module('professor')
         print("voce ja finalizou acoes nesta tabela professor")

      elif escolha == '3':
         importlib.import_module('disciplinaxprofessor')
         print("voce ja finalizou acoes nesta tabela disciplinaxprofessor")
except Exception as erro :
    print(f" Erro {erro}")
