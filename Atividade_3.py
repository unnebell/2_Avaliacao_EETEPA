vendas = [850.0, 920.5, 780.0, 1025.0, 1100.0, 950.0, 500.0]
meta = 900.0
i = 0
soma = 0
soma_acima = 0
soma_abaixo = 0
acima = 0
abaixo = 0

print("\n\t\t ===== Relatório de Vendas por Dia =====")

for venda in vendas:
    i += 1
    if venda > 900:
        print(f"Dia {i} - R$ {venda} - Acima")
        acima += 1
        soma_acima += venda
    else:
        print(f"Dia {i} - R$ {venda} - Abaixo")
        abaixo += 1
        soma_abaixo += venda

    soma += venda

total = len(vendas)
media = soma / total

print("\n\t\t ===== Resumo de Totais =====")
print(f"Total geral da semana: R$ {soma:.2f}")
print(f"\nDias que alcançaram a meta: {acima} dias = R$ {soma_acima:.2f}")
print(f"\nDias que [NÃO] alcançaram a meta: {abaixo} dias = R$ {soma_abaixo:.2f}")
print(f"\nMédia da semana: R${media:.2f}")