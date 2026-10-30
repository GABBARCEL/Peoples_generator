from secrets import choice
from pathlib import Path
import unicodedata
import _manager.Generator.RGcreator as RGc
import json

# Hierarquia da construção do indivíduo:
#    pessoaPt1 -> nome, 2 sobrenomes, nasimento e sexo;
#    pessoaPt2 -> RG, CPF;
#    pessoaPt3 -> Cidade, email e telefone.

# Formato final: 
# {
#     "id": 1,
#     "nome": "nome sobrenome1 sobrenome2",
#     "sobrenome": [
#         "sobrenome1",
#         "sobrenome2"
#     ],
#     "sexo": "Masculino", # Fim da pessoaPt1
#     "nascimento": "00/00/0000",
#     "CPF": "123.456.789-10",
#     "RG": "00.000.000-0", # Fim da pessoaPt2
#     "Estado": "SP",
#     "cidade": "São Paulo SP",
#     "email": "nomeSobrenome1@email.com",
#     "telefone": "11-999999999" # Fim da pessoaPt3
# }

def createIndividue(numero, anoMinimo, anoMaximo):
    def genPessoaPt1(id, anoNascimentoMinimo, anoNasimentoMaximo):
        id = numero
        caminhoNomeJson = Path(__file__).resolve().parent.parent.parent / "_Data" / "nomes.json"
        sexo = choice(["Masculino", "Feminino"])

        def genNome(genero):
            with open(caminhoNomeJson, "r", encoding="utf-8") as arq:
                dados = json.load(arq)

                if genero == "Masculino":
                    seed = choice(range(len(dados['nomes_masculinos'])))
                    return dados['nomes_masculinos'][seed]

                elif genero == "Feminino":
                    seed = choice(range(len(dados['nomes_femininos'])))
                    return dados['nomes_femininos'][seed]

        def genSobrenome():
            with open(caminhoNomeJson, "r", encoding="utf-8") as arq:
                dados = json.load(arq)
                seed = choice(range(len(dados["sobrenomes"])))
                return dados['sobrenomes'][seed]

        def genNasc(anoMinimo, anoMaximo):
            ano = choice(range(anoMinimo, (anoMaximo + 1)))
            mes = choice(range(1,13))

            if mes == 2:
                dia = choice(range(1, 29))
            elif mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
                dia = choice(range(1, 32))
            else:
                dia = choice(range(1, 31))

            nascimento = f"{dia:02}/{mes:02}/{ano}"

            return nascimento

        nome = genNome(sexo)
        sobrenome = [genSobrenome(), genSobrenome()]
        nascimento = genNasc(anoNascimentoMinimo, anoNasimentoMaximo)
        pessoaPt1 = {
            'id': id,
            'nome': nome + " " + sobrenome[0] + " " + sobrenome[1],
            'sobrenome': sobrenome,
            'sexo': sexo,
            'nascimento': nascimento
            }

        return pessoaPt1

    def genPessoaPt2():
        def genCpf(): # Código reaproveitado, JÁ DISPONIVEL NO GITHUB!
            seed = []
            for i in range(9):
                seed.append(choice(range(10)))
            def calculoProdutos(CPF):
                PreVereficador = []
                peso = len(CPF) + 1
                for i in range(len(CPF)): # Gerando os produtos para somar depois e calcular os  DVs
                    preSoma = CPF[i] * peso
                    peso -= 1
                    PreVereficador.append(preSoma)
                return PreVereficador

            def formatar(CPFlocal):
                CPFlocal.insert(3, ".")
                CPFlocal.insert(7, ".")
                CPFlocal.insert(11, "-")

            # Parte de criação e atribuição do Dv1
            produtosDv1 = calculoProdutos(seed)
            dv1 = (sum(produtosDv1) * 10 % 11)
            if dv1 == 10:
                dv1 = 0
            CPF= seed + [dv1]
            #Parte de criação e atribuição do Dv2
            produtosDv2 = calculoProdutos(CPF)
            dv2 = (sum(produtosDv2) * 10 % 11)
            if dv2 == 10:
                dv2 = 0
            CPF.append(dv2)
            formatar(CPF)
            CPF = "".join(map(str, CPF))
            return CPF

        def genRG():
            fncRND = choice(range(1,4))
            if fncRND == 1:
                return RGc.sequencialSimples("RND")
            if fncRND == 2:
                return RGc.minasGerais()
            if fncRND == 3:
                return RGc.sequencialComDV("RND")

        CPF = genCpf()
        RGeEstado = genRG()
        RG = RGeEstado[0]
        estado = RGeEstado[1]

        pessoaPt2 = {
            "CPF": CPF,
            "RG": RG,
            "Estado": estado
        }

        return pessoaPt2

    def genPessoaPt3(pessoa1, pessoa2):
        caminhoCidadesJson = Path(__file__).parent.parent.parent / "_Data" / "cidades.json"

        def genCidade(estado):
            with open(caminhoCidadesJson, "r", encoding="utf-8") as arq:
                dados = json.load(arq)
                valorCidade = choice(range(len(dados[estado])))
                caminhoCidade = dados[estado][valorCidade]
                return caminhoCidade

        def genEmail(nome):
            def remover_acentos(texto):
                nfkd = unicodedata.normalize('NFKD', texto)
                return u"".join([c for c in nfkd if not unicodedata.combining(c)])

            nome = remover_acentos(nome.replace(" ", ""))

            # Gera 3 tipos de email:
            def emailTipo1(): # nomeSobrenome@email.com
                email = nome + "@email.com"
                return email
            def emailTipo2(): # nomeSobrenome94@email.com #
                numRnd = choice(range(0, 10))
                numRnd2 = choice(range(0, 10))
                email = nome + str(numRnd) + str(numRnd2) + "@email.com"
                return email
            def emailTipo3(): # nomeSobrenome123@gmail.com
                sqnl = choice(range(1,8))
                email = nome + str(sqnl) + str(sqnl + 1) + str(sqnl + 2) + "@email.com"
                return email

            tipoEmail = choice(range(1,4))
            if tipoEmail == 1:
                email = emailTipo1()
                return email
            if tipoEmail == 2:
                email = emailTipo2()
                return email
            if tipoEmail == 3:
                email = emailTipo3()
                return email

        def genTelefone(DDD):
            prefixo = []
            sufixo = []
            for i in range(4):
                rnd = choice(range(0,10))
                prefixo.append(str(rnd))
            for i in range(4):
                rnd = choice(range(0,10))
                sufixo.append(str(rnd))

            telefone = prefixo + sufixo
            telefone.insert(0, f"{DDD[1]}-9")
            telefone = "".join(map(str, telefone))
            return telefone

        estadoPessoa = pessoa2["Estado"]
        nomePessoa = pessoa1['nome']

        cidade = genCidade(estadoPessoa)
        email = genEmail(nomePessoa)
        telefone = genTelefone(cidade)
        pessoaPt3 = {
            'cidade': cidade[0] + " " + estadoPessoa,
            'email': email,
            'telefone': telefone
        }
        return pessoaPt3

    pessoa1 = genPessoaPt1(numero, anoMinimo, anoMaximo)
    pessoa2 = genPessoaPt2()
    pessoa3 = genPessoaPt3(pessoa1, pessoa2)

    individuo = pessoa1 | pessoa2 | pessoa3

    return individuo