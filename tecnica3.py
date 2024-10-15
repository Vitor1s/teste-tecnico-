import json

# Dados fictícios de faturamento diário em formato JSON
faturamento_json = '''
{
    "faturamento_diario": [
        {"dia": 1, "valor": 200},
        {"dia": 2, "valor": 0},
        {"dia": 3, "valor": 100},
        {"dia": 4, "valor": 500},
        {"dia": 5, "valor": 0},
        {"dia": 6, "valor": 0},
        {"dia": 7, "valor": 700},
        {"dia": 8, "valor": 100},
        {"dia": 9, "valor": 300},
        {"dia": 10, "valor": 0}
    ]
}
'''

# Carregar dados do JSON
dados = json.loads(faturamento_json)

# Extrair apenas os valores de faturamento > 0 dias com faturamento
faturamentos = [dia['valor'] for dia in dados['faturamento_diario'] if dia['valor'] > 0]

# Cálculos
menor_faturamento = min(faturamentos)
maior_faturamento = max(faturamentos)
media_mensal = sum(faturamentos) / len(faturamentos)

# Contar dias com faturamento superior à média mensal
dias_acima_da_media = len([valor for valor in faturamentos if valor > media_mensal])

# Resultados
print(f"Menor valor de faturamento: R$ {menor_faturamento:.2f}")
print(f"Maior valor de faturamento: R$ {maior_faturamento:.2f}")
print(f"Número de dias com faturamento superior à média: {dias_acima_da_media}")