# Projeto de Cadastro de Professores e Disciplinas em Python

## Requisitos do Programa

1. **Cadastro de Professores**:
   - Crie um programa completo em Python para realizar operações de:
     - Cadastro
     - Alteração
     - Exclusão
     - Consulta a registros da tabela **professores**.
   - A tabela deve ser criada no banco de dados **univap**.

2. **Validações e Tratamento de Erros**:
   - O programa deve exigir a digitação correta dos seguintes dados:
     - Nome
     - Telefone
     - Idade
     - Salário
   - Trate erros comuns de banco de dados, especialmente:
     - Impedir a exclusão de professores que tenham registros na tabela **disciplinasxprofessores**.
   - Realize tratamento de erros de conexão com o banco de dados.

3. **Cadastro de Disciplinas**:
   - Crie um programa para cadastrar, alterar, excluir e consultar registros na tabela **disciplinasxprofessores**, que deve ser criada no banco de dados **univap**.
   - A tabela deve estar relacionada com as tabelas **disciplinas** e **professores**.
   - O programa deve prever testes de integridade de dados:
     - Informe ao usuário se tentar incluir professores ou disciplinas não cadastrados.

4. **Consultas e Visualização**:
   - Permita ao usuário visualizar quais disciplinas e professores estão cadastrados para uso nas relações de cadastro e alteração.

5. **Tratamento de Exclusão**:
   - Caso o usuário tente excluir um professor ou disciplina relacionados na tabela **disciplinasxprofessores**, exiba uma mensagem informando que a exclusão não é permitida. Utilize `try` ou consultas SQL para este tratamento.

## Observações Finais
- Melhore a aparência das telas para uma melhor experiência do usuário.
