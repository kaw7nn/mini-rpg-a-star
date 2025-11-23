# Mini RPG com Algoritmo A\* (Pathfinding)

Este projeto é uma simulação visual de um sistema de navegação para
jogos (Pathfinding) utilizando Python.\
Ele demonstra como um personagem pode encontrar o caminho mais curto
entre dois pontos em um mapa conectado, utilizando o algoritmo **A\***
(A-Star).

------------------------------------------------------------------------

## 📝 Descrição do Problema

Em jogos de RPG e estratégia, mover personagens de um ponto "A" para um
ponto "B" de forma inteligente é um desafio comum.\
O personagem não pode simplesmente andar em linha reta se houver
obstáculos ou se o terreno tiver custos diferentes (ex: é mais rápido
andar por uma estrada do que por um pântano).

Este projeto resolve esse problema modelando o mapa como um **Grafo
Ponderado**:

-   **Nós (Nodes):** Representam os locais (Vila, Castelo, Floresta,
    etc.).
-   **Arestas (Edges):** Representam os caminhos que ligam os locais.
-   **Pesos (Weights):** Representam o "custo" ou dificuldade de
    atravessar aquele caminho\
    (ex: Floresta custa 4, Planície custa 2).

O algoritmo **A**\* é utilizado para calcular a rota combinando dois
fatores:

-   **Custo Real (g):** A distância acumulada das arestas percorridas.
-   **Heurística (h):** A distância euclidiana (linha reta) entre o
    ponto atual e o destino final.

------------------------------------------------------------------------

## 🚀 Como Rodar Passo a Passo

Siga os passos abaixo para executar o projeto em sua máquina.

### 1. Pré-requisitos

Você precisa ter o **Python** instalado.

Além disso, o projeto utiliza: - `networkx` para cálculos de grafos\
- `tkinter` para a interface gráfica (já vem com Python na maioria das
instalações)

------------------------------------------------------------------------

### 2. Instalação das Dependências

No terminal:

``` bash
pip install networkx
```

> **Nota para Ubuntu/Debian**:\
> Caso ocorra erro relacionado ao tkinter, execute:
>
> ``` bash
> sudo apt-get install python3-tk
> ```

------------------------------------------------------------------------

### 3. Preparando o Arquivo

1.  Crie um arquivo chamado `rpg_mapa.py`.
2.  Cole o código Python fornecido.
3.  Salve o arquivo.

------------------------------------------------------------------------

### 4. Executando o Projeto

No terminal, navegue até a pasta onde o arquivo foi salvo e execute:

``` bash
python rpg_mapa.py
```

------------------------------------------------------------------------

## 5. Como Usar

-   Uma janela mostrará o mapa com os locais conectados.
-   O personagem (quadrado azul) começa na **Vila**.
-   Clique no botão **"Mover para..."**
-   Escolha um local (ex: *Castelo*).
-   O algoritmo A\* calculará automaticamente:
    -   O melhor caminho (destacado em **amarelo**)
    -   O personagem se moverá passo a passo até o destino.

------------------------------------------------------------------------

## 🛠️ Tecnologias Utilizadas

-   **Python 3**
-   **Tkinter** --- Interface gráfica (Canvas e UI)
-   **NetworkX** --- Criação do grafo e uso do algoritmo `astar_path`

------------------------------------------------------------------------
