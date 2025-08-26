#!/usr/bin/env python3
"""
Exemplo de código para demonstração em slides
curtoLab Template - Snippets externos
"""

# #region conceito-basico
def exemplo_conceito(dados):
    """
    Demonstra o conceito fundamental apresentado no curso.
    
    Args:
        dados (list): Lista de elementos para processar
        
    Returns:
        list: Dados processados conforme regras do conceito
    """
    resultado = []
    
    for item in dados:
        # Aplicar transformação conforme conceito
        item_processado = aplicar_conceito(item)
        resultado.append(item_processado)
    
    return resultado
# #endregion conceito-basico

# #region implementacao-avancada
def aplicar_conceito(item):
    """Implementação específica do conceito"""
    if isinstance(item, str):
        # Processamento para strings
        return item.strip().upper()
    elif isinstance(item, (int, float)):
        # Processamento para números
        return item * 2
    else:
        # Processamento genérico
        return str(item)

def exemplo_avancado(dados, opcoes=None):
    """
    Versão avançada com configurações personalizáveis.
    """
    if opcoes is None:
        opcoes = {'modo': 'padrão', 'verbose': False}
    
    if opcoes.get('verbose'):
        print(f"Processando {len(dados)} itens...")
    
    if opcoes['modo'] == 'otimizado':
        # Implementação otimizada
        return [aplicar_conceito(item) for item in dados]
    else:
        # Implementação padrão
        return exemplo_conceito(dados)
# #endregion implementacao-avancada

# #region exemplo-uso
if __name__ == "__main__":
    # Dados de exemplo
    dados_teste = ["hello", "world", 42, 3.14, None]
    
    print("=== Exemplo Básico ===")
    resultado_basico = exemplo_conceito(dados_teste)
    print(f"Entrada: {dados_teste}")
    print(f"Saída: {resultado_basico}")
    
    print("\n=== Exemplo Avançado ===")
    opcoes = {'modo': 'otimizado', 'verbose': True}
    resultado_avancado = exemplo_avancado(dados_teste, opcoes)
    print(f"Saída otimizada: {resultado_avancado}")
# #endregion exemplo-uso
