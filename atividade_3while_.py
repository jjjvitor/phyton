import os 
os.system("cls")

#  definindo variaveis
menor_idade = 999
maior_idade = 0
soma_salario = 0 
quantidade_salarios = 0
mulheres5k = 0


while True:
    os.system("cls")
    print("""
codigo    !   descricao
  1       !   adicionar pessoa      
  2       !   exibir resultados
  3       !   sair
""")
    
    opcao = int(input("digite o codigo da opcao desejada: "))
    match opcao:
        case 1:
            # solicitando dados
            idade = int(input("digite sua idade: "))
            sexo = input("digte o seu sexo - use m ou f: ")
            salario = float(input("digite o seu salrio: "))
            
            #media de salarios
            quantidade_salarios += 1
            soma_salario += salario

            # maior e menor idades
            if idade < menor_idade:
                menor_idade = idade

            if idade > maior_idade:
                maior_idade = idade

            #quantidade de mulheres com salario >= 5k.
            if salario >= 5000 and sexo == "f":
                mulheres5k += 1

            os.system("cls")
        case 2:
            media_salarial = soma_salario / quantidade_salarios if quantidade_salarios != 0 else 0
            if menor_idade == 999:
                menor_idade = 0

            print("\n= exibindo resultados =")
            print(f"media de salarios fo grupo: {media_salarial}")
            print(f"menor idade do grupo: {menor_idade}")
            print(f"maior idade do grupo: {maior_idade}")
            print(f"quantidade de mulheres com salario acima de 5 mil: {mulheres5k}")
            input("pressione enter para continuar...")
        case 3:
            print("saindo do programa.")
            input("pressione enter para sair.")
            break
        case _:
            print("opcao invalida, tente novamente")
            input("pressione enter para continuar...")




            


    


