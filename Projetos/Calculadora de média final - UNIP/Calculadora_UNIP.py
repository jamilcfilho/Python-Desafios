        ## Calculadora de médias finais de cursos a partir de 2023 da Universidade Paulista - UNIP EaD ##
while True:
    nota_prova = int(input("\nDigite a nota da prova: "))
    nota_pim = int(input("Digite a nota do PIM: "))
    nota_ava = int(input("Digite a nota do AVA: "))
    nota_minima = 6.75


    calcular_media_final = (nota_prova * 7 + nota_pim * 2 + nota_ava * 1) / 10

    print(f"\nA sua média final é de: {calcular_media_final}\n")

    if calcular_media_final == 0:
        break

    elif calcular_media_final >= nota_minima:
        print("--- Parabéns, você foi aprovado com êxito!!! ---\n")
        print("=" * 50)
    
    elif calcular_media_final < 6.74:
        print("--- Você precisará realizar o exame dessa disciplina ---\n")
        print("=" * 50)

    else:
        print("Algum valor foi digitado incorreto, favor verificar\n")