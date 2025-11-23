import tkinter as tk
import networkx as nx
import math
import time


# =====================================================
# CONFIGURAÇÃO DO GRAFO DO MAPA
# =====================================================

mapa = nx.Graph()

locais = [
    "Vila", "Planície", "Floresta", "Lago", "Caverna",
    "Montanha", "Castelo", "Fazenda", "Ponte Antiga",
    "Torre do Mago", "Pântano", "Acampamento Orc"
]

mapa.add_nodes_from(locais)

mapa.add_weighted_edges_from([
    ("Vila", "Planície", 2),
    ("Vila", "Floresta", 4),
    ("Planície", "Lago", 3),
    ("Floresta", "Lago", 2),
    ("Floresta", "Caverna", 5),
    ("Lago", "Montanha", 6),
    ("Caverna", "Montanha", 3),
    ("Montanha", "Castelo", 4),
    ("Vila", "Fazenda", 3),
    ("Fazenda", "Ponte Antiga", 4),
    ("Ponte Antiga", "Torre do Mago", 7),
    ("Torre do Mago", "Castelo", 5),
    ("Planície", "Pântano", 6),
    ("Pântano", "Acampamento Orc", 4),
    ("Acampamento Orc", "Caverna", 7),
    ("Torre do Mago", "Montanha", 6)
])

# Coordenadas visuais
pos = {
    "Vila": (80, 250),
    "Planície": (180, 350),
    "Floresta": (180, 150),
    "Lago": (330, 250),
    "Caverna": (470, 120),
    "Montanha": (600, 180),
    "Castelo": (760, 120),

    "Fazenda": (80, 100),
    "Ponte Antiga": (230, 60),
    "Torre do Mago": (420, 40),
    "Pântano": (300, 380),
    "Acampamento Orc": (500, 350),
}

def heuristica(atual, objetivo):
    (x1, y1) = pos[atual]
    (x2, y2) = pos[objetivo]
    return math.dist([x1, y1], [x2, y2])


# =====================================================
# INTERFACE TKINTER REINFORÇADA
# =====================================================

class RPGMap:
    def __init__(self, root):
        self.root = root
        self.root.title("Mini RPG com Algoritmo A*")

        self.canvas = tk.Canvas(root, width=900, height=500, bg="#1e1e1e")
        self.canvas.pack()

        self.personagem_local = "Vila"

        self.desenhar_mapa()
        self.desenhar_personagem()

        btn = tk.Button(
            root,
            text="Mover para...",
            command=self.janela_destino,
            font=("Arial", 12, "bold"),
            bg="#333",
            fg="white"
        )
        btn.pack(pady=8)

    # ------------------------------------------
    # Desenhar mapa (nós + arestas)
    # ------------------------------------------
    def desenhar_mapa(self):
        # Desenhar arestas
        for a, b in mapa.edges():
            x1, y1 = pos[a]
            x2, y2 = pos[b]
            self.canvas.create_line(
                x1, y1, x2, y2,
                fill="#777",
                width=2
            )

        # Desenhar locais
        for local, (x, y) in pos.items():
            self.canvas.create_oval(
                x-18, y-18, x+18, y+18,
                fill="#444",
                outline="white",
                width=2
            )
            self.canvas.create_text(
                x, y + 28,
                text=local,
                fill="white",
                font=("Arial", 10, "bold")
            )

    # ------------------------------------------
    # Bonequinho customizado
    # ------------------------------------------
    def desenhar_personagem(self):
        x, y = pos[self.personagem_local]

        # Corpo
        self.personagem = self.canvas.create_rectangle(
            x-12, y-12, x+12, y+12,
            fill="#4dc2ff",
            outline="white",
            width=2
        )

        # Olhos
        self.eye1 = self.canvas.create_oval(x-6, y-4, x-2, y, fill="black")
        self.eye2 = self.canvas.create_oval(x+2, y-4, x+6, y, fill="black")

    # ------------------------------------------
    # Movimento animado
    # ------------------------------------------
    def mover_personagem(self, caminho):

        # Destacar caminho
        self.destacar_caminho(caminho)

        # Pular o primeiro item pois já está na posição inicial
        for i in range(1, len(caminho)):
            local_atual = caminho[i-1] if i > 0 else self.personagem_local
            local_destino = caminho[i]
            
            x_origem, y_origem = pos[local_atual]
            x_dest, y_dest = pos[local_destino]

            # Calcular diferença total
            dx_total = x_dest - x_origem
            dy_total = y_dest - y_origem

            # Mover suavemente de um ponto ao outro
            passos = 30
            for passo in range(passos + 1):
                # Calcular posição interpolada
                progresso = passo / passos
                x_atual = x_origem + (dx_total * progresso)
                y_atual = y_origem + (dy_total * progresso)

                # Reposicionar personagem na posição calculada
                self.canvas.coords(self.personagem, 
                                   x_atual-12, y_atual-12, 
                                   x_atual+12, y_atual+12)
                
                # Reposicionar olhos
                self.canvas.coords(self.eye1, 
                                   x_atual-6, y_atual-4, 
                                   x_atual-2, y_atual)
                self.canvas.coords(self.eye2, 
                                   x_atual+2, y_atual-4, 
                                   x_atual+6, y_atual)

                self.canvas.update()
                time.sleep(0.02)

            self.personagem_local = local_destino

        # ao final remove o destaque
        self.limpar_destaques()

    # ------------------------------------------
    # Janela para escolher destino
    # ------------------------------------------
    def janela_destino(self):
        win = tk.Toplevel(self.root)
        win.title("Selecione o destino")
        win.config(bg="#222")

        tk.Label(win, text="Escolha o destino:", bg="#222", fg="white", font=("Arial", 12)).pack(pady=10)

        for local in locais:
            if local != self.personagem_local:
                tk.Button(
                    win, text=local, font=("Arial", 11),
                    bg="#444", fg="white",
                    command=lambda l=local: self.iniciar_movimento(l, win)
                ).pack(pady=5, fill="x")

    # ------------------------------------------
    # Executa o A*
    # ------------------------------------------
    def iniciar_movimento(self, destino, janela):
        janela.destroy()

        caminho = nx.astar_path(
            mapa,
            self.personagem_local,
            destino,
            heuristic=lambda n, goal=destino: heuristica(n, goal),
            weight="weight"
        )

        print("\nCaminho encontrado:", caminho)
        self.mover_personagem(caminho)

    # ------------------------------------------
    # Destacar visualmente o caminho
    # ------------------------------------------
    def destacar_caminho(self, caminho):
        self.destaques = []
        for i in range(len(caminho) - 1):
            a = caminho[i]
            b = caminho[i+1]
            x1, y1 = pos[a]
            x2, y2 = pos[b]

            line = self.canvas.create_line(x1, y1, x2, y2, fill="yellow", width=4)
            self.destaques.append(line)

    def limpar_destaques(self):
        for d in self.destaques:
            self.canvas.delete(d)

# =====================================================
# EXECUÇÃO
# =====================================================

root = tk.Tk()
app = RPGMap(root)
root.mainloop()