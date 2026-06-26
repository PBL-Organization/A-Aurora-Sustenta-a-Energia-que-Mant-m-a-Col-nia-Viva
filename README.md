# A-Aurora-Sustenta-a-Energia-que-Mantém-a-Colônia-Viva
# 🚀 SIGIC - Sistema Inteligente de Gerenciamento da Infraestrutura da Colônia

O **SIGIC** é uma aplicação em terminal desenvolvida para modelar, simular e otimizar a infraestrutura operacional e a rede energética da colônia marciana **Aurora Siger**. 

O projeto utiliza conceitos avançados de **Teoria dos Grafos**, **Algoritmos de Busca**, **Estruturas de Dados Otimizadas** e **Modelagem Matemática Continua** com foco em governança tecnológica e sustentabilidade (**ESG**).

---

## 🛠️ Funcionalidades Principais

* **Gestão de Módulos (Vértices):** Cadastro detalhado dos 8 módulos críticos da colônia (Habitação, Oxigênio, Centro de Controle, etc.), monitorando consumo, prioridade, status e coordenadas espaciais imutáveis.
* **Representação Dupla da Rede (Arestas):** * *Lista de Adjacência:* Para otimização de memória RAM em mapas expansíveis.
    * *Matriz de Adjacência:* Tabela bidimensional cruzada para consultas instantâneas de conectividade.
* **Algoritmos de Varredura e Inspeção:** * *BFS (Busca em Largura):* Varredura concêntrica em ondas utilizando filas estruturadas (`deque`).
    * *DFS (Busca em Profundidade):* Exploração profunda de caminhos via recursão estrutural.
* **Otimização de Rotas (Algoritmo de Dijkstra):** Navegação inteligente (estilo GPS) utilizando fila de prioridades (`heapq`), calculando o caminho mínimo exato e reconstruindo a rota passo a passo entre os módulos.
* **Modelagem Matemática Computacional:** Simulação de crescimento de consumo contínuo com base em cálculo diferencial.
* **Trava de Segurança ESG:** Sistema de governança que prevê sobrecarga na matriz de energia limpa e emite alertas automáticos de mitigação de riscos.
* **Design Defensivo (UX):** Menus dinâmicos 100% numéricos que eliminam erros de digitação e impedem operações inválidas (como rotas repetidas).

---

## 🚀 Como Executar o Projeto

O projeto foi construído utilizando exclusivamente a biblioteca padrão do Python, sem necessidade de instalar frameworks ou dependências externas.

1. Certifique-se de ter o Python 3.x instalado em sua máquina.
2. Baixe o arquivo `codigo_fonte.py`.
3. Abra o terminal na pasta do arquivo e execute:


python codigo_fonte.py
📈 Modelagem Matemática e ESGPara prever o impacto da expansão da infraestrutura marciana, o sistema aplica a fórmula de Crescimento Exponencial Contínuo:$$C(t) = C_0 \cdot e^{rt}$$Onde:C(t): Consumo energético total projetado.C₀: Consumo base atual da colônia (305 kW).e: Constante matemática de Euler.r: Taxa de expansão diária da colônia (fixada em 5%).t: Tempo em dias.Ação de Governança: Caso a simulação matemática preveja que o consumo ultrapassará o limite sustentável de 400 kW, o sistema dispara um bloqueio de segurança e emite um alerta em tela, auxiliando os gestores da colônia na tomada de decisão responsável.💻 Tecnologias e Conceitos UtilizadosLinguagem: Python 3Estruturas de Dados: Dicionários aninhados, Matrizes 2D, Listas de Adjacência e Tuplas Imutáveis.Módulos Nativos: collections.deque (Varredura BFS com performance $O(1)$), heapq (Fila de Prioridade para o Dijkstra) e math.👥 Autores (Desenvolvedores)Allan Victor Santos de Almeida Jesus - RM573218Gustavo Veloso Marchese dos Santos - RM568930José Elias Aleixo Lopes - RM568858Sarah Mendes Machado de Oliveira - RM570514Projeto desenvolvido como Atividade Integradora para a FIAP - 2026.
