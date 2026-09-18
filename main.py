# ==============================================================================
# PLANO (Critério 1 / Passo 1)
# Requisitos a implementar:
# 1. R1 - Visualização de vagas disponíveis no estacionamento.
#       - Como aluno eu quero saber aonde tem vagas disponíveis no horário de pico da manhã para estacionar meu carro
# 2. R2 - Filtragem de vagas reservadas para funcionários/biblioteca.
#       - Como aluno eu quero saber as vagas disponíveis em tempo real para poder estacionar meu carro
#
# Ordem e Tempo: R1 -> R2 -> README e ajustes .
# ==============================================================================

from vagas import listar_vagas
from filtro_vagas import filtrar_vagas

def main():
    print("--- PROTÓTIPO: SISTEMA DE ESTACIONAMENTO DO CAMPUS ---")
    
    # Execução R1
    todas_vagas = listar_vagas()
    print(f"\n[Executando R1] Total de vagas cadastradas no sistema: {len(todas_vagas)}")
    
    # Resumo por categoria
    for cat in ["pcd", "idoso", "derac", "ru", "geral", "coberta"]:
        qtd = len([v for v in todas_vagas if v["categoria"] == cat])
        print(f" - Categoria {cat.upper()}: {qtd} vagas")
        
    # Execução R2 - Exemplo de filtro DERAC Livres
    print("\n[Executando R2] Filtrando vagas LIVRES da categoria DERAC:")
    derac_livres = filtrar_vagas(todas_vagas, apenas_livres=True, categoria="derac")
    for v in derac_livres:
        print(f"-> Disponível: Vaga {v['id']} ({v['local']})")

    # Execução R2 - Exemplo de filtro Cobertas Livres
    print("\n[Executando R2] Filtrando vagas LIVRES da categoria COBERTA:")
    cobertas_livres = filtrar_vagas(todas_vagas, apenas_livres=True, categoria="coberta")
    for v in cobertas_livres:
        print(f"-> Disponível: Vaga {v['id']} ({v['local']})")

if __name__ == "__main__":
    main()
    
# ==============================================================================
# AUTOAVALIAÇÃO
# Creio ter cumprido os critérios 1, 2, 3, 4, 5 e 6.
# Requisito mais difícil foi R2, pois exigiu lógica para separar regras de alunos e funcionários.
# Resolvi implementando validação condicional simples comparando a categoria.
# Uso de IA: Ajudou a acelerar a escrita dos laços e formatação de saída.
# ==============================================================================
