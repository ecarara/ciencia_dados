"""
Propósito: Calculadora financeira de juros compostos
Autor: Edson Angelo Carara (edson.carara@gmail.com)
Curso: Analista de Dados com Ênfase em Mercado financeiro
Turma: 2024-11A

Trabalho prático Módulo 1 enunciado em https://online.igti.com.br/courses/7972/files/641842?wrap=1

Esta calculadora permite calcular juros compostos com base nas seguintes informações: Valor Final (vf), Capital Inicial (ci), Período (t) e Taxa (i).

Fórmulas:
vf = ci * (1 + i)**t
ci = vf / (1 + i)**t
i = ((vf / ci)**(1/t)) – 1
t = log(vf / ci) / log(1 + i)

"""
import math

def CalculadoraFinanceiraJurosCompostos() -> None:
    """
    Calcula o juros compostos com base na escolha do usuário
    """

    print("Bem-vindo à calculadora de juros compostos!")
    print("Desenvolvido por Edson Angelo Carara")
    print("Turma: 2024-11A")
    print()

    while True:
        opcao = EscolherCalculadora()
        if( opcao == "vf"):
            CalculadoraValorFinal()
        elif( opcao == "ci"):
            CalculaorCapitalInicial()
        elif( opcao == "i"):
            CalculadoraTaxa()
        elif( opcao == "t"):
            CalculadoraPeriodo()

        print()
        resposta = ObterEscolha("Deseja fazer mais algum cálculo?", ["S", "N"], False)
        if resposta == "N":
            break

def EscolherCalculadora() -> str:
    """
    Permite o usuário selecionar uma calculadora válida e retorna o seu código, sendo:
    vf: Valor Final
    ci: Capital Inicial
    t: Período
    i: Taxa

    Returns
    -------
    O código da calculadora
    """

    print("Valor Final (vf), Capital Inicial (ci), Período (t) e Taxa (i)")
    opcoes = ['vf', 'ci', 't', 'i']
    return ObterEscolha("O que você gostaria de calcular?", opcoes)

def CalculadoraValorFinal() -> None:
    """
    Calculadora do valor final
    """
    ci = ObterCapitalInicial()
    i = ObterTaxa()
    t = ObterPeriodo()
    vf = ci * (1 + i)**t
    print(f"O Valor Final é: {vf:.2f}")
   
def CalculaorCapitalInicial() -> None:
    """
    Calculadora do valor inicial
    """

    vf = ObterCapitalFinal()
    i = ObterTaxa()
    t = ObterPeriodo()
    ci = vf / (1 + i)**t
    print(f"O Capital Inicial é: {ci:.2f}")

def CalculadoraTaxa() -> None:
    """
    Calculadora da taxa
    """

    vf = ObterCapitalFinal()
    ci = ObterCapitalInicial()
    t = ObterPeriodo()
    i = ((vf / ci)**(1/t)) - 1
    print(f"A Taxa é: {i:.2%}")

def CalculadoraPeriodo() -> None:
    """
    Calculadora de período
    """

    vf = ObterCapitalFinal()
    ci = ObterCapitalInicial()
    i = ObterTaxa()
    t = math.log(vf / ci) / math.log(1 + i)
    print(f"O Período é: {t:.2f}")

def ObterCapitalInicial() -> float:
    """
    Obtém a informação digitada do capital inicial

    Returns
    -------
    float
       O valor do capital inicial digitado pelo usuário
    """
    return ObterVariavel("Informar o valor do Capital Inicial (ci)", False)

def ObterCapitalFinal() -> float:
    """
    Obtém a informação digitada do capital final

    Returns
    -------
    float
       O valor do capital final digitado pelo usuário
    """
    return ObterVariavel("Informar o valor do Capital Final (cf)", False)

def ObterPeriodo() -> float:
    """
    Obtém a informação digitada do período

    Returns
    -------
    float
       O valor do período digitado pelo usuário
    """
    return ObterVariavel("Informar o Período (t)", False)

def ObterTaxa() -> float:
    """
    Obtém a informação digitada da taxa

    Returns
    -------
    float
       O valor da taxa digitado pelo usuário
    """
    return ObterVariavel("Informar a Taxa (i)") / 100

def ObterVariavel(mensagem: str, podeSerZero: bool = True) -> float:
    """
    Obtém informações numéricas que são digitadas pelo usuario.

    Parameters
    ----------
    mensagem: str
       Mensagem que vai ser exibida para o usuário no momento do input
    podeSerZero : bool
       Indica se o valor informado pode ser zero. Por padrão é True.

    Returns
    -------
    float
       O valor numérico digitado pelo usuário

    """    
    input_valido = False
    while not input_valido:
        try:
            print(f"{mensagem}:")
            valor = input().strip()
            valor = float(valor)
            if( valor == 0 and not podeSerZero ):
                print(f"O valor informado {valor} não pode ser zero.")
            elif( valor < 0):
                print(f"O valor informado {valor} não pode ser negativo.")
            else:
                return valor
        except:
            print(f"{valor} não é um número válido. Por favor informar o número no padrão 999.99")

def ObterEscolha(mensagem: str,opcoes: list[str], opcoesEmMinusculas: bool = True) -> str:
    """
    Obtém a escolha do usuário entre as opções fornecidas.

    Parameters
    ----------
    mensagem: str
       Mensagem que vai ser exibida para o usuário no momento do input
    opcoes: list[str]
       Lista de opções válidas para escolha
    opcoesEmMinusculas: bool
       Indica se as opções devem ser convertidas para minúsculas. Por padrão é True.

    Returns
    -------
    str
       A opção escolhida pelo usuário

    """
    input_valido = False
    while not input_valido:
        escolha = input(f"{mensagem} ({'/'.join(opcoes)}): ").strip().lower()
        if not  opcoesEmMinusculas:
            escolha = escolha.upper()

        if escolha in opcoes:
            input_valido = True
        else:
            print(f"Opção inválida. Por favor, escolha entre {'/'.join(opcoes)}.")
    return escolha

def main():
    CalculadoraFinanceiraJurosCompostos()

if __name__ == "__main__":
    main()
