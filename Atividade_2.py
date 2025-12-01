avaliacoes = [78, 55, 92, 40, 88, 61, 73]
i = 0
soma = 0
excelente = 0
bom = 0
insatisfeito = 0

print("\n\t\t ===== Relatório de Notas =====")
for ava in avaliacoes:
    i += 1

    if ava > 80:
        print(f"Funcionário {i} - Nota: {ava} = Excelente")
        excelente += 1
    elif ava <= 80 and ava >= 60:
        print(f"Funcionário {i} - Nota: {ava} = Bom")
        bom += 1
    elif ava < 60:
        print(f"Funcionário {i }- Nota: {ava} = Insatisfatório")
        insatisfeito += 1

    soma += ava

total_av = len(avaliacoes)
media = soma / total_av
print("\n\t\t\t  ===== Média =====")
print(f"Média das avaliações: {media:.2f} ")

print("\n\t\t ===== Porcentagem por categoria =====")
print(f"Excelente: {(excelente/total_av)*100:.1f}%")
print(f"Bom: {(bom/total_av)*100:.1f}%")
print(f"Insatisfatório: {(insatisfeito/total_av)*100:.1f}%")