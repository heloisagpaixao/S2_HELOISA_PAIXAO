#-*-coding:UTF-8-*-
# Dicionários com os preços
sabores = {
    "chocolate": 10.0,
    "baunilha": 9.0,
    "morango": 11.0
}



print("Bem-vindo à confeitaria!")

# Escolha do sabor
print("\nSabores disponíveis:")
for sabor in sabores:
    print(f"- {sabor.capitalize()}")
sabor_escolhido = input("Escolha um sabor: ").lower()

# Verifica se o sabor existe
if sabor_escolhido in sabores:
    preco_base = sabores[sabor_escolhido]

    # Escolha do tamanho
    print("\nTamanhos disponíveis:")
    for tamanho in tamanhos:
        print(f"- {tamanho.capitalize()}")
    tamanho_escolhido = input("Escolha o tamanho (pequeno, médio, grande): ").lower()

    if tamanho_escolhido in tamanhos:
        multiplicador = tamanhos[tamanho_escolhido]

        # Escolha da cobertura
        print("\nCoberturas disponíveis:")
        for cobertura in coberturas:
            print(f"- {cobertura.capitalize()}")
        cobertura_escolhida = input("Escolha a cobertura: ").lower()

        if cobertura_escolhida in coberturas:
            preco_cobertura = coberturas[cobertura_escolhida]

            # Cálculo do preço final
            preco_total = (preco_base * multiplicador) + preco_cobertura
            print(f"\nResumo do pedido:")
            print(f"Sabor: {sabor_escolhido.capitalize()}")
            print(f"Tamanho: {tamanho_escolhido.capitalize()}")
            print(f"Cobertura: {cobertura_escolhida.capitalize()}")
            print(f"Preço total: R${preco_total:.2f}")
        else:
            print("Cobertura inválida.")
    else:
        print("Tamanho inválido.")
else:
    print("Sabor inválido.")
