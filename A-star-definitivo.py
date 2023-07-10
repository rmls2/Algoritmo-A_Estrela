from heapMinDefinitiva import HeapMin
from informacoes_problema import estacoes_linha, distancias_reais, distancias_heuristicas

# mude as variaveis end e start para realização dos testes 

heap = HeapMin()

def A_estrela(start, end, distancias_reais, distancias_heuristicas, estacoes_linha):
    # Inicialização da fila de prioridade heap
    heap.adiciona_no((0, start, []))
    # Inicialização do conjunto de nós visitados
    visitados = set()
    # Inicialização dos scores de "g" para todos os nós como infinito
    funcao_g = {node: float('inf') for node in distancias_reais.keys()}
    funcao_g[start] = 0
    # Variável que armazena o tempo de baldeação
    tempo_baldeacao = 0
    iteracoes = 0

    # Loop principal para busca do caminho
    while heap.heap:
        # Obtém o nó com o menor score "f" (soma de "g" e heurística) da fila de prioridade
        menor_no_atual = heap.remove_no()
        (funcao_f, no_atual, caminho) = menor_no_atual
        # Verifica se o nó já foi visitado
        aux_menor = menor_no_atual
        if (no_atual in visitados) and (funcao_f > aux_menor[0]):
            continue
        iteracoes += 1
        # Armazana o funcao_f do nó atual
        funcao_f_no_atual = funcao_f
        # Marca o nó como visitado
        if no_atual not in visitados:
            visitados.add(no_atual)
        # Adiciona o nó ao caminho
        caminho = caminho + [no_atual]
        # Verifica a linha atual percorrida entre as duas últimas estações do caminho
        if len(caminho) >= 2:
            estacao = caminho[-2]
            linha_em_comum = set(estacoes_linha[estacao]).intersection(
                estacoes_linha[no_atual])
        # Verifica todos os vizinhos do nó atual
        for no_vizinho in distancias_reais[no_atual].keys():
            # Verifica se o vizinho já foi visitado
            if no_vizinho in visitados:
                continue
            # Verifica se a estação atual e sua vizinha compartilham a linha atual
            if len(caminho) >= 2:
                if linha_em_comum == set(estacoes_linha[no_atual]).intersection(estacoes_linha[no_vizinho]):
                    tempo_baldeacao = 0
                else:
                    tempo_baldeacao = 4
            # Calcula o score "g" para o vizinho
            funcao_g[no_vizinho] = funcao_g[no_atual] + \
                distancias_reais[no_atual][no_vizinho] / 30 + tempo_baldeacao / 60
            # Atualiza o score "g" para o vizinho
           ## funcao_g[no_vizinho] = tentative_g_score
            # Calcula o score "f" (soma de "g" e heurística) para o vizinho
            funcao_f = funcao_g[no_vizinho] + \
                distancias_heuristicas[int(no_vizinho[1:]) -
                                    1][int(end[1:])-1] / 30  # km/h
            # Adiciona o vizinho à fila de prioridade
            ##heapq.heappush(heap, (funcao_f, no_vizinho, caminho))
            heap.adiciona_no((funcao_f, no_vizinho, caminho))

        ##menor = heapq.nsmallest(1, heap)
        menor = heap.menor_elemento()
        # Verifica se o nó é o destino
        if no_atual == end:
            if (menor[0] > funcao_f_no_atual):
                break
            else:
                heap.adiciona_no((funcao_f_no_atual, no_atual, caminho))

        # Printando as fronteiras
        fronteira_heap = heap.heap
        front = []
        front_dist = []

        for neigh in fronteira_heap:
            front.append(neigh[1])
            front_dist.append(neigh[0])

        print("Fronteira de ", no_atual, ": ", end="")
        for qt_neigh in range(len(front)):
            print(front[qt_neigh], f", {front_dist[qt_neigh]:.2f} || ", end="")

        print("")

    # Cálculo da distância
    distancia = 0
    for i in range(len(caminho) - 1):
        distancia += distancias_reais[caminho[i]][caminho[i + 1]]
    # Retorna as linhas percorridas entre cada estação do caminho
    linhas_percorridas = []
    for i in range(len(caminho) - 1):
        estacao = caminho[i]
        proxima_estacao = caminho[i + 1]
        linha_em_comums = set(estacoes_linha[estacao]).intersection(
            estacoes_linha[proxima_estacao])
        for linha in linha_em_comums:
            linhas_percorridas.append(linha)

    # Calcula o número de baldeações e o tempo do caminho
    contador = 0
    for i in range(len(linhas_percorridas) - 1):
        if linhas_percorridas[i] != linhas_percorridas[i + 1]:
            contador += 1
    ## tempo = distancia / 30 + contador * 4 / 60

    minutos = (distancia / 30 + contador * 4 / 60) * 60  # tempo
    minutos, segundos = divmod(minutos * 60, 60)
    horas, minutos = divmod(minutos, 60)
    tempo = "{:02d}:{:02d}:{:02d}".format(
        int(horas), int(minutos), int(segundos))

    return caminho, distancia, tempo, linhas_percorridas, contador



estacao_inicial = "E1"
estacao_final = "E13"

caminho, distancia, tempo, linhas_percorridas, contador = A_estrela(
    estacao_inicial, estacao_final, distancias_reais, distancias_heuristicas, estacoes_linha)
print("\n")
print("Caminho:", " -> ".join(caminho))
print("Linhas:", " -> ".join(linhas_percorridas))
print("Distancia:", distancia, "km")
print("Tempo:", tempo, "horas")
print("Baldeacoes:", contador)
