# Arquivo referente ao Requisito 1 (R1) - Listagem de vagas

# Arquivo referente ao Requisito 1 (R1) - Listagem de vagas

def obter_vagas_mock():
    """Gera a lista exata de vagas por categoria."""
    vagas = []
    
    # Configuração das quantidades de vagas por categoria
    configuracao = [
        ("pcd", 5, "Bloco M"),
        ("idoso", 5, "Bloco M"),
        ("derac", 5, "Bloco do DERAC"),
        ("ru", 10, "Restaurante Universitário"),
        ("geral", 20, "Estacionamento"),
        ("coberta", 15, "Estacionamento")
    ]
    
    for categoria, quantidade, local in configuracao:
        for i in range(1, quantidade + 1):
            # Alterna o status entre LIVRE e OCUPADA para simular dados reais
            status = "LIVRE" if i % 2 != 0 else "OCUPADA"
            
            vagas.append({
                "id": f"{categoria.upper()}-{i:02d}",
                "local": local,
                "status": status,
                "categoria": categoria
            })
            
    return vagas

def listar_vagas():
    """Retorna todas as vagas cadastradas no sistema."""
    return obter_vagas_mock()