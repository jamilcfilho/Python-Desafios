        ## Calculadora de médias finais de cursos a partir de 2023 da Universidade Paulista - UNIP EaD ##

nota_prova = int(input("\nDigite a nota da prova: "))
nota_pim = int(input("Digite a nota do PIM: "))
nota_ava = int(input("Digite a nota do AVA: "))
nota_minima = 6.75
nota_maxima = 6.9


calcular_media_final = (nota_prova * 7 + nota_pim * 2 + nota_ava * 1) / 10

print(f"\nA sua média final é de: {calcular_media_final}")

if calcular_media_final >= 6.75:
    print("\nParabéns, você foi aprovado com êxito!!!")
elif calcular_media_final < 6.7:
    print("\nVocê precisará realizar o exame dessa disciplina\n")
else:
    print("\nAlgum valor foi digitado incorreto, favor verificar\n")