# Sistema de Cálculo de Moedas 💰

Aplicação em Python para simular e comparar diferentes abordagens de resolução do problema do troco mínimo — encontrar o menor número de moedas necessário para somar um valor alvo.

O projeto demonstra a aplicação de estratégias algorítmicas (gulosa, recursiva, recursiva com memoização e programação dinâmica) de forma didática e testável via terminal.

## Integrantes

* Abner de Paiva Barbosa - RM558468
* Fernando Luiz S. Antonio - RM555201
* Thomas Reichmann - RM554812


## Requisitos

* Python 3.10 ou superior

## Funcionalidades

* **Estratégia Gulosa (Iterativa):**
    * Seleciona sempre a maior moeda possível até formar (ou não) o valor desejado.
    * Rápida, mas não garante a solução ótima para todos os conjuntos de moedas.

* **Recursiva Pura:**
    * Explora todas as combinações possíveis.
    * Implementação direta do raciocínio matemático, mas com custo exponencial de tempo.

* **Recursiva com Memoização (Top-Down):**
    * Mantém o raciocínio recursivo, mas armazena resultados intermediários.
    * Evita recomputações e reduz a complexidade para $O(N \cdot K)$, onde:
        * $N$ = valor alvo
        * $K$ = número de moedas

* **Programação Dinâmica (Bottom-Up):**
    * Constrói iterativamente soluções de 0 até o valor alvo.
    * Abordagem mais eficiente e previsível, usada em sistemas reais de otimização.
    * Trata impossibilidades, retornando -1 quando não há combinação possível.

    ## Estrutura do Projeto

```text
coin-change/
│
├── coin_change.py        # implementação principal com todas as funções
├── README.md             # documentação do projeto
└── .gitignore            # exclusões padrão (venv, cache, etc.)
```

## Como Executar 🚀

**1. Clonar o repositório:**

```bash
git clone [https://github.com/SEU-USUARIO/coin-change.git](https://github.com/SEU-USUARIO/coin-change.git)
cd coin-change
```
**2. Executar o programa:**
```bash
python coin_change.py
```

## Casos de Teste Simulados

```python
exemplos = [
    (6,  [1, 3, 4]),   # mínimo esperado: 2 (3+3)
    (7,  [2, 4]),      # impossível (-1)
    (11, [1, 5, 7]),   # mínimo esperado: 3 (5+5+1)
    (0,  [1, 3, 4]),   # 0
]

```
## Uso / Exemplo de Saída

```text
--------------------------------------------------
Caso 1
Valor alvo (M): 6
Moedas: [1, 3, 4]
  Guloso (não garante ótimo): 3 moeda(s)
  Recursiva pura (exponencial): 2 moeda(s)
  Recursiva c/ memo (Top-Down): 2 moeda(s)
  PD Bottom-Up (ótimo): 2 moeda(s)
  --> Mínimo encontrado: 2 moeda(s)
  ```

## Estrutura / Algoritmo

* **`_validate_inputs()`**
    * Garante entradas válidas e remove moedas duplicadas ou não positivas.
    * Retorna lista ordenada crescente.

* **`qtdeMoedas()` – Guloso**
    * Percorre as moedas do maior valor ao menor.
    * Divide o valor restante pelo valor da moeda atual.
    * Pode falhar em casos onde a combinação ótima não envolve as maiores moedas.

* **`qtdeMoedasRec()` – Recursiva Pura**
    * Resolve o problema por decomposição:
        * `min(qtdeMoedasRec(M - c) + 1)` para cada moeda `c`.
    * Simples conceitualmente, mas muito custosa.

* **`qtdeMoedasRecMemo()` – Recursiva com Dicionário**
    * Usa um dicionário (`memo`) para armazenar resultados já calculados.
    * Mantém a clareza da recursão, mas com desempenho quase linear.

* **`qtdeMoedasPD()` – Programação Dinâmica**
    * Cria vetor `dp` com tamanho `M + 1`.
    * Inicializa `dp[0] = 0` e `dp[i] = INF` para os demais.
    * Atualiza progressivamente:
        * `dp[i] = min(dp[i], dp[i - moeda] + 1)`
    * Retorna -1 se `dp[M]` permanece infinito (valor impossível).

## Bloco de Demonstração (Main)

* Itera sobre casos predefinidos e imprime resultados de cada abordagem.
* Rótulos explicativos indicam a natureza e desempenho de cada método.
* Indica o melhor resultado encontrado para cada caso.
* Utiliza apenas concatenação de strings (sem f-strings), mantendo compatibilidade total.

## Complexidade (Big O) por Abordagem

- **Guloso (`qtdeMoedas`)**
  - **Tempo:** O(k log k) para ordenar as moedas + O(k) na varredura ⇒ geralmente O(k log k)
  - **Espaço:** O(1) adicional
  - **Observação:** não garante ótimo em sistemas de moedas arbitrários (só em sistemas “canônicos”, ex.: {1,5,10,25}).

- **Recursiva Pura (`qtdeMoedasRec`)**
  - **Tempo:** Exponencial. No pior caso, O(k^(M/mín_moeda)) (explora quase todas as combinações)
  - **Espaço:** O(M) pela profundidade da pilha de recursão
  - **Observação:** didática, mas impraticável para M médio/grande.

- **Recursiva com Memoização / Top-Down (`qtdeMoedasRecMemo`)**
  - **Tempo:** O(M · k) — cada subproblema 0..M é resolvido no máx. uma vez, testando k moedas
  - **Espaço:** O(M) para o dicionário de memo + O(M) de pilha (na prática, O(M))
  - **Observação:** mantém o raciocínio recursivo com custo quase linear em M.

- **Programação Dinâmica Bottom-Up (`qtdeMoedasPD`)**
  - **Tempo:** O(M · k)
  - **Espaço:** O(M)
  - **Observação:** costuma ser a opção mais previsível/estável; fácil de justificar e testar.

## Conclusão

O projeto exemplifica a evolução de complexidade e eficiência entre métodos para o problema do troco mínimo:

* **Guloso** é rápido, mas não ótimo.
* **Recursiva pura** é conceitualmente simples, porém ineficiente.
* **Recursiva com memoização** traz eficiência sem perder clareza.
* **Programação Dinâmica** é a abordagem ideal para aplicações reais.

A saída organizada e descritiva permite ao usuário comparar os métodos e entender a diferença de desempenho de forma direta e visual.