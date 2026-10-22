# Como não existe algoritmo nacional padrozinado, os estados e seus orgãos emissores ficam encarregados por gerar os RGs. Por isso, esse programa gera na verdade, sequência aleatórias de números com formatação do RG de cada estado. Para os estados que o RG possuí o digito vereficador, estarei usando um algoritmo para cria-lo, garantindo que se torne plausível.
from secrets import choice

def sequencialSimples(estado=None):
    # Definições
    qntCaracteres = {
        'AP': 7,
        'BA': 8,
        'DF': 7,
        'ES': 8,
        'GO': 7,
        'MA': 8,
        'MS': 8,
        'MT': 9,
        'PA': 7,
        'PB': 7,
        'PE': 7,
        'PI': 8,
        'RN': 7,
        'RS': 10,
        'RO': 7,
        'RR': 7,
        'SC': 7,
        'SE': 8,
        'TO': 7}
    def genRG(estadoLocal):
        RGlocal = []
        for i in range(1, (qntCaracteres[estadoLocal] + 1)):
            randomCrt = choice(range(0, 10))
            RGlocal.append(randomCrt)
        return RGlocal

    def formatacaoIndividual(RG, formato):
        if formato == "PE" or formato == "SC":
            RG.insert(1, ".")
            RG.insert(5, ".")
            return RG
        else:
            return RG

    def randomizar(listaEstados):
        estadoKey = choice(list(listaEstados.keys()))
        return estadoKey

#####################################

# Parte solicitadora
    # Subparte
    if estado == None:
        raise TypeError("O parâmetro estado deve ser preenchido para o RG ser formado. Para visualizar quais opções de estado a função suporta, use 'HELP' como parâmetro.")

    if estado not in list(qntCaracteres.keys()) and estado.upper() != "RND" and estado.upper() != "HELP":
        raise KeyError("Estado inválido para função! Caso queira ver a lista de estados compatíveis com está função, use sequencialSimples('HELP')")

    elif estado.upper() == "HELP":
        return"""
Você usou o comando de ajuda. Essa função retorna um RG já formatado para o estado posto como parâmetro na função, para usar o estado como parâmetro, deve-se colocalo entre aspas. ex: sequencialSimples('RS')

    Segue os estados compatíveis com ESTE comando.

        1. AP
        2. BA
        3. DF
        4. ES
        5. GO
        6. MA
        7. MS
        8. MT
        9. PA
        10. PR
        11. PB
        12. PE
        13. PI
        14. RN
        15. RS
        16. RO
        17. RR
        18. SC
        19. SE
        20. TO


[IMPORTANTE!] Para ter acesso a RGs de outros estados, use o parâmetro 'HELP' na função sequencialComDV ou minasGerais.
"""

    elif estado.upper() == "RND":
        parametroRND = randomizar(qntCaracteres)
        RG = genRG(parametroRND)
        RG = formatacaoIndividual(RG, parametroRND)
        RGformatado = "".join(map(str, RG))
        return RGformatado, parametroRND

    else:
        RG = genRG(estado)
        RG = formatacaoIndividual(RG, estado)
        RGformatado = "".join(map(str, RG))
        return RGformatado, estado

def minasGerais(ajuda=None):
    if ajuda == "HELP" or ajuda == "help":
        return"""
Você usou o comando de ajuda. Essa função retorna um RG com formatação do estado de Minas Gerais, e somente este estado. Para utiliza-lo, basta declara-lo sem parâmetro algum. ex: minasGerais()

[IMPORTANTE!] Para ter acesso a RGs de outros estados, use o parâmetro 'HELP' na função sequencialComDV ou sequenciaSimples.
"""


    def formatar(RG):
        RG.insert(3, ".")
        RG.insert(7, ".")
        return RG

    RGprimitivo = ["MG-"]
    for i in range(8):
        rndCaracter = choice(range(0,10))
        RGprimitivo.append(rndCaracter)

    RG = formatar(RGprimitivo)
    RG = "".join(map(str, RG))

    return RG, "MG"

def sequencialComDV(estado=None):
# Definições
    qntCaracteres = {
        'AC': 7,
        'AL': 8,
        'AM': 8,
        'CE': 8,
        'PR': 7,
        'RJ': 8,
        'SP': 8
    }

    def genRgSemDV(estadoLocal):
        RGprimitivo = []
        for i in range(1, (qntCaracteres[estadoLocal] + 1)):
            rndCaracter = choice(range(0,10))
            RGprimitivo.append(rndCaracter)
        return RGprimitivo

    def gerarDv(RGsemDv):
        soma = sum(RGsemDv)
        return (soma % 10)

    def formatar(RGlocal, formato):
        if formato == "AC":
            RGlocal.insert(7, "-")
            return RGlocal
        elif formato == "AL" or formato == "AM" or formato == "CE":
            RGlocal.insert(8, "-")
            return RGlocal
        elif formato == "PR":
            RGlocal.insert(1, ".")
            RGlocal.insert(5, ".")
            RGlocal.insert(9, "-")
            return RGlocal
        elif formato == "RJ":
            RGlocal.insert(2, ".")
            RGlocal.insert(6, ".")
            RGlocal.insert(10, "-")
            return RGlocal
        elif formato == "SP":
            RGlocal.insert(2, ".")
            RGlocal.insert(6, ".")
            RGlocal.insert(10, "-")
            return RGlocal
        else:
            return RGlocal

    def randomizar(listaEstados):
        estadoKey = choice(list(listaEstados.keys()))
        return estadoKey

###############################

# Parte solicitadora
    # Subparte vereficadora
    if estado == None:
        raise TypeError("O parâmetro estado deve ser preenchido para o RG ser formado. Para visualizar quais opções de estado a função suporta, use 'HELP' como parâmetro.")

    if estado not in list(qntCaracteres.keys()) and estado.upper() != "RND" and estado.upper() != "HELP":
        raise KeyError("Estado inválido para função! Caso queira ver a lista de estados compatíveis com está função, use sequencialSimples('HELP')")

    elif estado.upper() == "HELP":
        return"""
Você usou o comando de ajuda. Essa função retorna um RG já formatado para o estado posto como parâmetro na função, para usar o estado como parâmetro, deve-se colocalo entre aspas. ex: sequencialComDv('SP')

    Segue os estados compatíveis com ESTE comando.

        1. AC
        2. AL
        3. AM
        4. CE
        5. PR
        6. RJ
        7. SP


[IMPORTANTE!] Para ter acesso a RGs de outros estados, use o parâmetro 'HELP' na função sequencialSimples ou minasGerais.
"""

    if estado.upper() == "RND":
        parametroRND = randomizar(qntCaracteres)
        RG = genRgSemDV(parametroRND)
        DV = gerarDv(RG)
        RG.append(DV)
        formatar(RG, parametroRND)
        RG = "".join(map(str, RG))
        return RG, parametroRND

    else:
        RG = genRgSemDV(estado)
        DV = gerarDv(RG)
        RG.append(DV)
        formatar(RG, estado)
        RG = "".join(map(str, RG))
        return RG, estado