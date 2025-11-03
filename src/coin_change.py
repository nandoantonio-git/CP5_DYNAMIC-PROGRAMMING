from math import inf, gcd
from typing import Iterable, List

__all__ = [
    "qtdeMoedas",
    "qtdeMoedasRec",
    "qtdeMoedasRecMemo",
    "qtdeMoedasPD",
]

def _validar_normalizar(valor_alvo: int, moedas: Iterable[int]) -> List[int]:
    """
    Valida entradas e normaliza a lista de moedas.
    Retorna lista de moedas únicas e ordenadas.
    """
    try:
        valor_alvo = int(valor_alvo)
    except Exception as e:
        raise TypeError("M deve ser inteiro.") from e

    if valor_alvo < 0:
        return []
    try:
        moedas_validas = [int(m) for m in moedas if int(m) > 0]
    except Exception as e:
        raise TypeError("moedas deve ser iterável de inteiros positivos.") from e
    moedas_validas = sorted(set(moedas_validas))
    return moedas_validas

def qtdeMoedas(valor_alvo: int, moedas: Iterable[int]) -> int:
    """
    Estratégia gulosa (iterativa).
    """
    if valor_alvo == 0:
        return 0
    moedas = _validar_normalizar(valor_alvo, moedas)
    if not moedas:
        return -1
    moedas.sort(reverse=True)

    restante = valor_alvo
    total_moedas = 0
    for moeda in moedas:
        if restante == 0:
            break
        if moeda <= restante:
            quantidade = restante // moeda
            total_moedas += quantidade
            restante -= quantidade * moeda
    return total_moedas if restante == 0 else -1

def qtdeMoedasRec(valor_alvo: int, moedas: Iterable[int]) -> int:
    """
    Recursiva pura (sem memoização): explora todas as combinações possíveis.
    """
    if valor_alvo == 0:
        return 0
    moedas = _validar_normalizar(valor_alvo, moedas)
    if not moedas:
        return -1

    def resolver(valor: int) -> int:
        if valor == 0:
            return 0
        if valor < 0:
            return inf
        melhor_qtde = inf
        for moeda in moedas:
            sub = resolver(valor - moeda)
            if sub + 1 < melhor_qtde:
                melhor_qtde = sub + 1
        return melhor_qtde

    resposta = resolver(valor_alvo)
    return resposta if resposta != inf else -1

def qtdeMoedasRecMemo(valor_alvo: int, moedas: Iterable[int]) -> int:
    """
    Recursiva com memoização (Top-Down) usando dicionário.
    """
    if valor_alvo == 0:
        return 0
    moedas = _validar_normalizar(valor_alvo, moedas)
    if not moedas:
        return -1

    memo = {0: 0}  # base: 0 custa 0 moedas

    def resolver(valor: int) -> int:
        if valor in memo:
            return memo[valor]
        melhor_qtde = inf
        for moeda in moedas:
            if valor - moeda >= 0:
                sub = resolver(valor - moeda)
                if sub + 1 < melhor_qtde:
                    melhor_qtde = sub + 1
        memo[valor] = melhor_qtde
        return melhor_qtde

    resposta = resolver(valor_alvo)
    return resposta if resposta != inf else -1

def qtdeMoedasPD(valor_alvo: int, moedas: Iterable[int]) -> int:
    """
    Programação Dinâmica Bottom-Up: constrói soluções de 0..valor_alvo.
    """
    if valor_alvo == 0:
        return 0
    moedas = _validar_normalizar(valor_alvo, moedas)
    if not moedas:
        return -1

    # Checagem de impossibilidade via MDC
    mdc = moedas[0]
    for moeda in moedas[1:]:
        mdc = gcd(mdc, moeda)
    if valor_alvo % mdc != 0:
        return -1

    INFINITO = valor_alvo + 1
    dp = [0] + [INFINITO] * valor_alvo  # dp[i] = mín. moedas para formar i
    for moeda in moedas:
        for valor in range(moeda, valor_alvo + 1):
            if dp[valor - moeda] + 1 < dp[valor]:
                dp[valor] = dp[valor - moeda] + 1
    return dp[valor_alvo] if dp[valor_alvo] != INFINITO else -1

if __name__ == "__main__":
    # Casos de exemplo: (valor_alvo, lista_de_moedas)
    exemplos = [
        (6,  [1, 3, 4]),   # mínimo esperado: 2 (3+3)
        (7,  [2, 4]),      # impossível
        (11, [1, 5, 7]),   # mínimo esperado: 3 (5+5+1)
        (0,  [1, 3, 4]),   # 0
    ]

    # Rótulos mais claros para cada abordagem
    funcoes = [
        (qtdeMoedas,       "Guloso (não garante ótimo)"),
        (qtdeMoedasRec,    "Recursiva pura (exponencial)"),
        (qtdeMoedasRecMemo,"Recursiva c/ memo (Top-Down)"),
        (qtdeMoedasPD,     "PD Bottom-Up (ótimo)")
    ]

    def imprime_resultado(rotulo_metodo, resultado):
        if resultado == -1:
            print("  " + rotulo_metodo + ": impossível")
        else:
            print("  " + rotulo_metodo + ": " + str(resultado) + " moeda(s)")

    for idx, par in enumerate(exemplos):
        valor_alvo, lista_moedas = par
        print("\n" + "-" * 50)
        print("Caso " + str(idx + 1))
        print("Valor alvo (M): " + str(valor_alvo))
        print("Moedas: " + str(lista_moedas))

        # Executa cada abordagem e imprime de forma padronizada
        resultados = []
        for func, rotulo in funcoes:
            r = func(valor_alvo, lista_moedas)
            resultados.append((rotulo, r))
            imprime_resultado(rotulo, r)

        # Destaque opcional do melhor resultado encontrado
        # (ignora -1 e pega o mínimo entre os restantes)
        melhores = [r for r in resultados if r[1] != -1]
        if len(melhores) > 0:
            melhor_valor = min([r[1] for r in melhores])
            print("  --> Mínimo encontrado: " + str(melhor_valor) + " moeda(s)")
        else:
            print("  --> Nenhuma abordagem formou o valor (impossível)")
