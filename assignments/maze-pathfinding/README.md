# 📘 Assignment: Maze Pathfinding

## 🎯 Objective

Implemente algoritmos de busca em largura (BFS) e busca em profundidade (DFS) para percorrer um labirinto representado por uma grade. Compare os caminhos encontrados e identifique por que BFS encontra o menor caminho quando cada movimento tem o mesmo custo, enquanto DFS não oferece essa garantia.

## 📝 Tasks

### 🛠️ Representar o Labirinto

#### Descrição

Represente o labirinto como uma lista de strings. `#` representa uma parede, `.` representa um espaço livre, `S` marca o início e `E` marca o destino. Escreva uma função que localize as coordenadas de início e destino e liste os vizinhos livres de uma posição, considerando apenas movimentos para cima, baixo, esquerda e direita.

#### Requisitos

O programa concluído deve:

- Armazenar o labirinto em uma lista de strings retangulares.
- Encontrar exatamente uma posição `S` e uma posição `E`.
- Retornar apenas vizinhos dentro dos limites da grade que não sejam paredes.
- Informar claramente se o início ou o destino estiver ausente.

Exemplo de labirinto:

```text
########
#S...#E#
#.#....#
#......#
########
```

### 🛠️ Encontrar o Menor Caminho com BFS

#### Descrição

Implemente uma busca em largura usando uma fila de `collections.deque`. Explore o labirinto a partir de `S` e reconstrua o caminho até `E` usando um registro de predecessores.

#### Requisitos

O programa concluído deve:

- Visitar cada posição livre no máximo uma vez.
- Explorar vizinhos em quatro direções e não atravessar paredes.
- Retornar o caminho como uma lista de coordenadas, incluindo início e destino.
- Retornar um resultado claro quando não houver caminho.
- Garantir que o caminho encontrado tenha o menor número de movimentos.

### 🛠️ Comparar BFS e DFS

#### Descrição

Implemente busca em profundidade (DFS) iterativamente, usando uma pilha, e execute os dois algoritmos em labirintos com mais de uma rota possível. Compare o número de movimentos dos caminhos encontrados.

#### Requisitos

O programa concluído deve:

- Retornar um caminho válido de `S` até `E` com DFS quando houver uma rota.
- Indicar corretamente quando não existir rota.
- Mostrar o número de movimentos retornado por cada algoritmo.
- Usar um labirinto com várias rotas para demonstrar que DFS pode retornar um caminho maior que o de BFS.
- Explicar, em uma frase, por que BFS encontra o menor caminho neste problema e DFS não garante isso.