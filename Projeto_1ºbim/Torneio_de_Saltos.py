iniciar = input("Deseja iniciar o programa?(S/N)")
while iniciar != "S" and iniciar != "N" :
    iniciar = input("\nResposta INVALIDA:(Digite S/N)")
qtd = 0
media = 0
teste = 0
while iniciar == "S" :
    teste = teste+1
    media = 0
    nome = input("\nDigite o nome do atleta:")
    for x in range (1,6):
        salto = float(input(f"\nDigite o valor do salto de numero {x}:"))
        if x == 1 :
            maior = salto
            menor = salto
        else:
            if salto > maior :
                maior = salto;
            elif salto < menor :
                menor = salto
        media = media + salto
    media = (media-maior-menor)/3
    print (f"\n\nMelhor Salto {maior:.1f}\n")
    print (f"Pior Salto {menor:.1f}\n\n")
    print (f"Resultado Final:\nAtleta:  {nome}\nMedia dos Saltos:{media:.1f}\n\n")

    qtd = qtd+1
    if qtd == 1 :
        cnome = nome
        cnumero = media;
    elif cnumero < media or cnumero == media:
        cnome = nome
        cnumero = media
        
    
    iniciar = input("Gostaria de continuar?(S/N)")
    while iniciar != "S" and iniciar != "N" :
        iniciar = input("\nResposta INVALIDA:(Digite S/N)")
    print("---------------------------------------------------------------------------------------------------------------------")
if teste >= 1 :
    cnome = cnome.upper()
    print (f"Atleta Campeão : {cnome}\nPontuação : {cnumero:.1f}")