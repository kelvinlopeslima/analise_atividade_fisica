from analise_atividade_fisica_bykelvin.loader import load_data
from analise_atividade_fisica_bykelvin.analysis import total_by_week, atividade_mais_frequente, dias_mais_ativos

df = load_data('dados/atividade.csv')

print("Resumo por semana:")
print(total_by_week(df))

print("\nAtividade mais praticada:")
print(atividade_mais_frequente(df))

print("\nDias mais ativos:")
print(dias_mais_ativos(df))