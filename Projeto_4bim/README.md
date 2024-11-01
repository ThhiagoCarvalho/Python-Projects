# Projeto 4º Bimestre - POOI

Desenvolva um programa em Python que solicite os dados finais de 4 disciplinas do curso de Informática e gere uma planilha Excel com os dados.

## Estrutura do Programa

- **Dados a serem solicitados**:
  - Matrícula (máximo 6 dígitos)
  - Nome do aluno (apenas letras)
  - Nota de PVB, PAW, BD e POOI (numéricas entre 0 e 10, com um dígito após a vírgula)

- **Geração da Planilha**:
  - Nome do arquivo: `NOTASFINAISALUNOS.XLSX`
  - Calcule e adicione a média das notas.

- **Testes de consistência**:
  - Validar nomes e notas conforme as regras especificadas.

- **Geração de arquivos HTML**:
  - Pergunte ao usuário se deseja gerar um arquivo HTML para cada aluno.
  - Cada arquivo deve ser nomeado pelo número da matrícula (ex: `500600.HTML`).
  - Formatação:
    - Nome do aluno em fundo vermelho.
    - Tabela colorida:
      - Azul se aprovado (média ≥ 6)
      - Amarelo se em exame (média entre 3,75 e 5,9)
      - Vermelho se retido (média < 3,75)
    - A situação final deve ter a mesma cor de fundo da tabela.

## Regras Gerais

- Os arquivos devem ser gerados na pasta: `C:\PROJETO4BIMESTRE`.

