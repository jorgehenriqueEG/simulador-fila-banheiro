import random

def simular_fila_banheiro(taxa_chegada, tempo_uso_medio, duracao_simulacao):
    chegada_proxima = 0
    tempo_atual = 0
    total_usuarios = 0
    soma_espera = 0
    
    while chegada_proxima < duracao_simulacao:
        tempo_espera = max(0, chegada_proxima - tempo_atual)
        soma_espera += tempo_espera
        total_usuarios += 1
        
        tempo_atual = chegada_proxima + tempo_uso_medio
        intervalo = random.randint(2, 8)
        chegada_proxima += intervalo
    
    if total_usuarios == 0:
        return 0, 0
    
    media_espera = soma_espera / total_usuarios
    return total_usuarios, media_espera

taxa_chegada = 12
tempo_uso = 5
duracao = 60

total, media = simular_fila_banheiro(taxa_chegada, tempo_uso, duracao)
print(f"Total usuários: {total}")
print(f"Tempo médio espera: {media:.1f} min")