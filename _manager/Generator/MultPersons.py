from _manager.Generator.Person import createIndividue


def CreatePersons(quantity, min, max, repeat=True, showRepeatsData = False):
    # Pra caso o usuário seja BURRO de querer colocar quantidade 0 ou negativa >:)
    if quantity <= 0:
        raise ValueError("[ERROR] The quantity value MUST be different from 0 and MUST be positive! ")

    else:
        listPersons = []
        persons_completed = 0
        repeats = 0

        #   Pra caso o usuário não queria repetições de dados. (Mais frequêntes em listas grandes)
        if repeat == False:
            while persons_completed < quantity:
                duplicate = False
                new_person = createIndividue(persons_completed + 1, min, max)

                if listPersons == []:
                    listPersons.append(new_person)
                    persons_completed += 1
                else:
                    for person in listPersons:
                        if (
                            new_person["nome"] == person["nome"]
                            or new_person["CPF"] == person["CPF"]
                            or new_person["RG"] == person["RG"]
                            or new_person["telefone"] == person["telefone"]
                        ):

                            duplicate = True
                            repeats += 1
                            break 

                    if not duplicate:
                        listPersons.append(new_person)
                        persons_completed += 1

        
        #   Caso o usuário não se importe com repetições de dados.
        else:
            for i in range(0, quantity):
                listPersons.append(createIndividue(i+1, min, max))


        # Tenho dúvidas se eu realmente tinha que adicionar isso...
        if showRepeatsData == True:
            print(f"    Persons with repeated data: {repeats}\n      ╰>   These were excluded, and are not included in the count ;)") #Uma gracinha minha ;)


        
        return listPersons