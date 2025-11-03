# CP5-Checkpoint-5---DYNAMIC-PROGRAMMING

- Implementação de Programação Dinâmica Bottom-Up para Troco Mínimo (`qtdeMoedasPD`)

* **Objetivo do Código**
  - Calcular a quantidade mínima de moedas para alcançar M com moedas ilimitadas; retornar -1 se impossível.

* **Escopo**
  - Validação/normalização de entradas
  - Checagem de impossibilidade via MDC
  - DP Bottom-Up com INF = M + 1
  - Testes de casos típicos e de borda

* **Funções Principais**
  - _validar_normalizar(M, moedas): filtra, deduplica e ordena moedas; trata M < 0
  - _gcd_lista(nums): calcula MDC do conjunto de moedas
  - qtdeMoedasPD(M, moedas): resolve com DP e retorna mín. moedas ou -1

* **Ideia do Problema Resolvido**
  - Minimizar a contagem de moedas para somar exatamente M (combinação, não permutação)

* **Validação e Normalização**
  - Garante M inteiro; remove não-positivas; deduplica; ordena crescente

* **Checagem de Impossibilidade (MDC)**
  - Se M % gcd(moedas) != 0, retornar -1 sem montar a tabela

* **Estratégia de Programação Dinâmica**
  - *Estado*: dp[i] = mín. moedas para i
  - *Base*: dp[0] = 0
  - *Transição*: dp[i] = min(dp[i], dp[i - c] + 1), para cada moeda c e i >= c
  - *Infinito*: INF = M + 1

* **Retorno**
  - Se dp[M] == INF ⇒ -1; caso contrário ⇒ dp[M]

* **Complexidade**
  - Tempo: O(M · k), k = quantidade de moedas
  - Espaço: O(M)

* **Casos Especiais**
  - M == 0 ⇒ 0
  - M < 0 ⇒ -1
  - Lista de moedas vazia/ inválida ⇒-1

* **Testes Base**
  - (6, [1, 3, 4]) ⇒ 2
  - (7, [2, 4]) ⇒ -1
  - (11, [1, 5, 7]) ⇒ 3
  - (0, [2, 4]) ⇒ 0
  - (-5, [1, 2, 5]) ⇒ -1
  - (14, [4, 6, 8]) ⇒ possível (mdc = 2)

* **Conclusão**
  - Solução correta, eficiente e clara; robustez adicional com validação e MDC
