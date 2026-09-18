# Arquivo referente ao Requisito 2 (R2) - Filtragem por categoria

def filtrar_vagas(lista_vagas, apenas_livres=True, categoria=None):
    """
    Filtra as vagas por status e por categoria exclusiva 
    (pcd, idoso, ru, derac, coberta ou geral).
    """
    vagas_filtradas = []
    
    for vaga in lista_vagas:
        # Filtro por ocupacao
        if apenas_livres and vaga["status"] != "LIVRE":
            continue
            
        # Filtro por categoria especifica
        if categoria and vaga["categoria"] != categoria:
            continue
            
        vagas_filtradas.append(vaga)
            
    return vagas_filtradas