# Validação de CPF: Funcionamento

## Introdução
O programa permite que o usuário digite um número de CPF com 11 dígitos. O objetivo é verificar a validade do CPF gerando os dois últimos dígitos com base nos nove primeiros. 

## Passo a Passo da Validação

1. **Entrada do CPF**:
   - O usuário informa o CPF no formato `123.456.789-10`.
   - Armazena-se cada dígito do CPF em uma lista.

2. **Cálculo do 1º Dígito Verificador**:
   - Cria-se duas listas:
     - Lista 1: 9 primeiros dígitos do CPF.
     - Lista 2: Números de 10 a 2.
   - Multiplicação dos dígitos da Lista 1 pelos da Lista 2 e soma dos produtos:
     ```
     10 * 1 + 9 * 2 + 8 * 3 + 7 * 4 + 6 * 5 + 5 * 6 + 4 * 7 + 3 * 8 + 2 * 9 = 210
     ```
   - Resto da divisão de 210 por 11:
     - Se o resto for menor que 2, o 1º dígito gerado é 0.
     - Caso contrário, 1º dígito = 11 - resto.

3. **Cálculo do 2º Dígito Verificador**:
   - Insere o 1º dígito na lista de CPF:
     ```
     Lista 1: [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
     Lista 2: [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
     ```
   - Multiplicação e soma:
     ```
     11 * 1 + 10 * 2 + ... + 0 * 0 = 255
     ```
   - Resto da divisão de 255 por 11:
     - Se o resto for menor que 2, o 2º dígito gerado é 0.
     - Caso contrário, 2º dígito = 11 - resto.

4. **Comparação dos Dígitos**:
   - Os dois últimos dígitos gerados são comparados com os fornecidos pelo usuário:
     - Se forem iguais, o CPF é **VÁLIDO**; caso contrário, é **INVÁLIDO**.

## Implementação em POO

- Construa uma lista contendo vários dicionários. Cada dicionário deve ter:
  - **'CPF'**: uma lista com os 11 dígitos do CPF testado.
  - **'VALIDACAO'**: valor `'VÁLIDO'` ou `'INVÁLIDO'`.

### Exemplo de Estrutura
```python
[
    {'CPF': [12345678910], 'VALIDACAO': 'INVÁLIDO'},
    {'CPF': [12345678911], 'VALIDACAO': 'VÁLIDO'},
    # ...
]
