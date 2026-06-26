from collections import deque
import heapq
import math

# ==========================
# 1. DADOS DOS MÓDULOS (Base de Dados)
# ==========================
# Utilizamos um dicionário principal onde cada chave é um módulo.
# Dentro de cada módulo, usamos sub-dicionários e tuplas para organizar 
# os requisitos de capacidade, consumo e coordenadas fixas (X,Y).

modulos = {
    "Habitacao": {
        "consumo": 50,
        "prioridade": 5,
        "status": "Ativo",
        "capacidade_armazenamento": 100,
        "necessidade_comunicacao": "Média",
        "coordenadas_fixas": (10, 20)  # Tupla garantindo que o local é imutável
    },
    "Centro de Controle": {
        "consumo": 40,
        "prioridade": 5,
        "status": "Ativo",
        "capacidade_armazenamento": 50,
        "necessidade_comunicacao": "Alta",
        "coordenadas_fixas": (15, 25)
    },
    "Armazenamento de Energia": {
        "consumo": 20,
        "prioridade": 5,
        "status": "Ativo",
        "capacidade_armazenamento": 5000,
        "necessidade_comunicacao": "Baixa",
        "coordenadas_fixas": (5, 5)
    },
    "Agricultura": {
        "consumo": 35,
        "prioridade": 4,
        "status": "Ativo",
        "capacidade_armazenamento": 200,
        "necessidade_comunicacao": "Baixa",
        "coordenadas_fixas": (30, 40)
    },
    "Laboratorio Cientifico": {
        "consumo": 30,
        "prioridade": 3,
        "status": "Ativo",
        "capacidade_armazenamento": 150,
        "necessidade_comunicacao": "Alta",
        "coordenadas_fixas": (40, 50)
    },
    "Comunicacao": {
        "consumo": 25,
        "prioridade": 4,
        "status": "Ativo",
        "capacidade_armazenamento": 10,
        "necessidade_comunicacao": "Extrema",
        "coordenadas_fixas": (50, 60)
    },
    "Suporte Medico": {
        "consumo": 45,
        "prioridade": 5,
        "status": "Ativo",
        "capacidade_armazenamento": 300,
        "necessidade_comunicacao": "Alta",
        "coordenadas_fixas": (20, 10)
    },
    "Producao de Oxigenio": {
        "consumo": 60,
        "prioridade": 5,
        "status": "Ativo",
        "capacidade_armazenamento": 1000,
        "necessidade_comunicacao": "Média",
        "coordenadas_fixas": (25, 15)
    }
}

# ==========================
# 2. GRAFO DA COLÔNIA (Rede Física)
# ==========================
# Representação da rede usando Lista de Adjacência.
# Os números representam o peso (distância ou custo) entre os módulos.

grafo = {
    "Habitacao": {"Centro de Controle": 5, "Suporte Medico": 3},
    "Centro de Controle": {"Habitacao": 5, "Comunicacao": 4, "Laboratorio Cientifico": 6},
    "Suporte Medico": {"Habitacao": 3, "Producao de Oxigenio": 4},
    "Comunicacao": {"Centro de Controle": 4, "Laboratorio Cientifico": 2},
    "Laboratorio Cientifico": {"Centro de Controle": 6, "Comunicacao": 2, "Agricultura": 5},
    "Agricultura": {"Laboratorio Cientifico": 5, "Producao de Oxigenio": 3},
    "Producao de Oxigenio": {"Agricultura": 3, "Suporte Medico": 4, "Armazenamento de Energia": 2},
    "Armazenamento de Energia": {"Producao de Oxigenio": 2}
}

# ==========================
# 3. ALGORITMOS DE BUSCA (BFS e DFS)
# ==========================

# O BFS faz uma varredura em "ondas" (níveis). Ideal para achar vizinhos próximos.
def bfs(inicio):
    visitados = []
    fila = deque([inicio]) # Usamos deque para otimizar a remoção do primeiro item (O(1))
    
    while fila:
        atual = fila.popleft()
        if atual not in visitados:
            visitados.append(atual)
            # Adiciona todos os vizinhos do nó atual na fila de verificação
            for vizinho in grafo[atual]:
                fila.append(vizinho)
    return visitados

# O DFS faz uma exploração profunda até achar um beco sem saída, depois retorna (recursão).
def dfs(no, visitados=None):
    if visitados is None:
        visitados = []
        
    visitados.append(no)
    
    for vizinho in grafo[no]:
        if vizinho not in visitados:
            dfs(vizinho, visitados) # A função chama a si mesma para continuar descendo
            
    return visitados

# ==========================
# 4. ALGORITMO DE DIJKSTRA (Otimização de Rota)
# ==========================
# Calcula o caminho mais "barato" entre dois pontos avaliando o peso das arestas.

def dijkstra_com_rota(inicio, destino):
    # Inicia todas as distâncias como infinito, exceto o ponto de partida
    distancias = {vertice: float("inf") for vertice in grafo}
    predecessores = {vertice: None for vertice in grafo} # Usado para rastrear o caminho feito
    distancias[inicio] = 0
    
    # Fila de prioridade (heapq) para sempre pegar o caminho de menor custo disponível
    fila = [(0, inicio)]

    while fila:
        dist_atual, atual = heapq.heappop(fila)

        # Otimização: se já chegamos no destino, não precisa calcular o resto do mapa
        if atual == destino:
            break

        if dist_atual > distancias[atual]:
            continue

        # Avalia os vizinhos e atualiza se o novo caminho for mais barato
        for vizinho, peso in grafo[atual].items():
            nova_distancia = dist_atual + peso
            if nova_distancia < distancias[vizinho]:
                distancias[vizinho] = nova_distancia
                predecessores[vizinho] = atual
                heapq.heappush(fila, (nova_distancia, vizinho))

    # Reconstrói a rota andando de trás para frente (do destino até a origem)
    caminho = []
    passo_atual = destino
    while passo_atual is not None:
        caminho.append(passo_atual)
        passo_atual = predecessores[passo_atual]
    
    caminho.reverse() # Inverte para mostrar da origem pro destino
    
    # Trava de segurança caso os módulos estejam isolados sem conexão
    if distancias[destino] == float("inf") or caminho[0] != inicio:
        return None, float("inf")
        
    return caminho, distancias[destino]

# ==========================
# 5. UTILITÁRIOS E EXIBIÇÃO DE DADOS
# ==========================

def mostrar_modulos():
    print("\n=== MÓDULOS ===")
    for nome, dados in modulos.items():
        print(f"\n{nome}")
        print(f"Consumo: {dados['consumo']} kW")
        print(f"Prioridade: {dados['prioridade']}")
        print(f"Armazenamento: {dados['capacidade_armazenamento']} un")
        print(f"Coordenadas: {dados['coordenadas_fixas']}")

def mostrar_rede():
    print("\n=== REDE DA COLÔNIA (LISTA DE ADJACÊNCIA) ===")
    for modulo, conexoes in grafo.items():
        print(f"{modulo} -> {conexoes}")

def mostrar_matriz_adjacencia():
    print("\n=== MATRIZ DE ADJACÊNCIA ===")
    lista_modulos = list(grafo.keys())
    tamanho = len(lista_modulos)
    
    # Cria uma matriz 2D (tabela) preenchida com zeros
    matriz = [[0 for _ in range(tamanho)] for _ in range(tamanho)]
    
    # Substitui os zeros pelos pesos reais onde existe conexão no grafo
    for i, origem in enumerate(lista_modulos):
        for j, destino in enumerate(lista_modulos):
            if destino in grafo[origem]:
                matriz[i][j] = grafo[origem][destino]
                
    # Imprime formatado (Cabeçalho e linhas)
    print(f"{'':<25} " + " ".join([f"{m[:3]:>4}" for m in lista_modulos]))
    for i, linha in enumerate(matriz):
        print(f"{lista_modulos[i]:<25} " + " ".join([f"{v:>4}" for v in linha]))

# ==========================
# 6. MODELAGEM MATEMÁTICA E GOVERNANÇA ESG
# ==========================

def simulacao_crescimento_consumo(dias):
    consumo_base = sum(m["consumo"] for m in modulos.values())
    taxa_crescimento_diaria = 0.05 # Taxa fixada em 5% ao dia
    
    print(f"\n=== SIMULAÇÃO DE CONSUMO (MODELAGEM MATEMÁTICA) ===")
    print(f"Função: C(t) = C0 * e^(rt)")
    print(f"Consumo Base Atual (C0): {consumo_base} kW")
    
    # Aplicação de cálculo diferencial (Crescimento exponencial contínuo)
    consumo_futuro = consumo_base * math.exp(taxa_crescimento_diaria * dias)
    
    print(f"Consumo projetado para {dias} dias: {consumo_futuro:.2f} kW")
    
    # Trava ESG: Se estourar 400kW, a rede limpa não suporta e exige expansão
    if consumo_futuro > 400:
        print("[ALERTA ESG CRÍTICO] A PROJEÇÃO EXCEDE A CAPACIDADE SUSTENTÁVEL! Necessário expandir matriz energética limpa.")

# ==========================
# 7. SISTEMA DE MENUS E VALIDAÇÃO (UX/UI)
# ==========================

# Função auxiliar criada para evitar erros de digitação (Design Defensivo)
def selecionar_modulo(mensagem, modulo_origem=None):
    lista_modulos = list(grafo.keys())
    
    while True:
        print(f"\n{mensagem}")
        for indice, nome_modulo in enumerate(lista_modulos, 1):
            # Identificador visual para impedir seleção do próprio local no Dijkstra
            if nome_modulo == modulo_origem:
                print(f"{indice} - {nome_modulo} (Você está aqui 📍)")
            else:
                print(f"{indice} - {nome_modulo}")
        
        try:
            escolha = int(input("\nDigite o número da opção: "))
            
            if 1 <= escolha <= len(lista_modulos):
                modulo_selecionado = lista_modulos[escolha - 1]
                
                # Bloqueia rotas inúteis (de um ponto para ele mesmo)
                if modulo_selecionado == modulo_origem:
                    print(f"\n[ERRO] Operação inválida! Você já está em '{modulo_origem}'. Escolha outro destino.")
                    continue
                    
                return modulo_selecionado
            else:
                print(f"\n[ERRO] Opção inválida. Digite um número entre 1 e {len(lista_modulos)}.")
        except ValueError:
            print("\n[ERRO] Entrada inválida. Por favor, digite um número inteiro.")

# ==========================
# 8. LOOP PRINCIPAL (Execução do SIGIC)
# ==========================

while True:
    print("\n" + "="*30)
    print(" SIGIC - AURORA SIGER ".center(30))
    print("="*30)
    print("1 - Ver dados dos Módulos")
    print("2 - Ver Rede (Lista de Adjacência)")
    print("3 - Ver Rede (Matriz de Adjacência)")
    print("4 - Executar Busca em Largura (BFS)")
    print("5 - Executar Busca em Profundidade (DFS)")
    print("6 - Otimização de Rota (Dijkstra)")
    print("7 - Simulação Matemática de Consumo")
    print("0 - Sair")

    opcao = input("\nEscolha uma operação: ")

    if opcao == "1":
        mostrar_modulos()
    elif opcao == "2":
        mostrar_rede()
    elif opcao == "3":
        mostrar_matriz_adjacencia()
        
    elif opcao == "4":
        print("\n" + "="*30)
        print(" BUSCA EM LARGURA (BFS) ".center(30))
        print("="*30)
        
        inicio = selecionar_modulo("Selecione o módulo INICIAL para a varredura (BFS):")
        resultado_bfs = bfs(inicio)
        
        print("\n" + "-"*30)
        print(f"📌 Ordem de visitação (BFS) a partir de '{inicio}':")
        print(f" ➔ {' ➔ '.join(resultado_bfs)}")
        print("-"*30)

    elif opcao == "5":
        print("\n" + "="*30)
        print(" BUSCA EM PROFUNDIDADE (DFS) ".center(30))
        print("="*30)
        
        inicio = selecionar_modulo("Selecione o módulo INICIAL para a exploração (DFS):")
        resultado_dfs = dfs(inicio)
        
        print("\n" + "-"*30)
        print(f"📌 Ordem de visitação (DFS) a partir de '{inicio}':")
        print(f" ➔ {' ➔ '.join(resultado_dfs)}")
        print("-"*30)

    elif opcao == "6":
        print("\n" + "="*30)
        print(" OTIMIZAÇÃO DE ROTA (DIJKSTRA) ".center(30))
        print("="*30)
        
        inicio = selecionar_modulo("Selecione o módulo de ORIGEM:")
        destino = selecionar_modulo("Selecione o módulo de DESTINO:", modulo_origem=inicio)
        
        caminho, custo = dijkstra_com_rota(inicio, destino)
        if caminho:
            print("\n" + "-"*30)
            print(f"📌 Rota mais eficiente encontrada:")
            print(f" ➔ {' ➔ '.join(caminho)}")
            print(f"⚡ Custo total do trajeto (Distância/Energia): {custo} km/kW")
            print("-"*30)
        else:
            print("\nNão há caminho disponível entre estes módulos.")

    elif opcao == "7":
        try:
            dias = int(input("Informe a quantidade de dias para projeção: "))
            simulacao_crescimento_consumo(dias)
        except ValueError:
            print("Por favor, digite um número inteiro.")
            
    elif opcao == "0":
        print("Encerrando o SIGIC... Colônia operando em modo autônomo.")
        break
    else:
        print("Opção inválida.")
