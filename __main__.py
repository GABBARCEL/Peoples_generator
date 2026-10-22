from _manager import *
from _manager.Generator import *
from time import sleep

def welcome():
    print("""
    \n
    $$\   $$\           $$\ $$\                 $$\      $$\                     $$\       $$\ $$\ 
    $$ |  $$ |          $$ |$$ |                $$ | $\  $$ |                    $$ |      $$ |$$ |
    $$ |  $$ | $$$$$$\  $$ |$$ | $$$$$$\        $$ |$$$\ $$ | $$$$$$\   $$$$$$\  $$ | $$$$$$$ |$$ |
    $$$$$$$$ |$$  __$$\ $$ |$$ |$$  __$$\       $$ $$ $$\$$ |$$  __$$\ $$  __$$\ $$ |$$  __$$ |$$ |
    $$  __$$ |$$$$$$$$ |$$ |$$ |$$ /  $$ |      $$$$  _$$$$ |$$ /  $$ |$$ |  \__|$$ |$$ /  $$ |\__|
    $$ |  $$ |$$   ____|$$ |$$ |$$ |  $$ |      $$$  / \$$$ |$$ |  $$ |$$ |      $$ |$$ |  $$ |    
    $$ |  $$ |\$$$$$$$\ $$ |$$ |\$$$$$$  |      $$  /   \$$ |\$$$$$$  |$$ |      $$ |\$$$$$$$ |$$\ 
    \__|  \__| \_______|\__|\__| \______/       \__/     \__| \______/ \__|      \__| \_______|\__|
                                                                                                   
                                                                                                   
                                                                                                 
    
    """)

def goodBye():
    print("""

 $$$$$$\                            $$\       $$$$$$$\                      $$\ 
$$  __$$\                           $$ |      $$  __$$\                     $$ |
$$ /  \__| $$$$$$\   $$$$$$\   $$$$$$$ |      $$ |  $$ |$$\   $$\  $$$$$$\  $$ |
$$ |$$$$\ $$  __$$\ $$  __$$\ $$  __$$ |      $$$$$$$\ |$$ |  $$ |$$  __$$\ $$ |
$$ |\_$$ |$$ /  $$ |$$ /  $$ |$$ /  $$ |      $$  __$$\ $$ |  $$ |$$$$$$$$ |\__|
$$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |      $$ |  $$ |$$ |  $$ |$$   ____|    
\$$$$$$  |\$$$$$$  |\$$$$$$  |\$$$$$$$ |      $$$$$$$  |\$$$$$$$ |\$$$$$$$\ $$\ 
 \______/  \______/  \______/  \_______|      \_______/  \____$$ | \_______|\__|
                                                        $$\   $$ |              
                                                        \$$$$$$  |              
                                                         \______/               

""")

def singlePerson():
    print("\nTo generate your data, we need a range of years during which this person might have been born.")
    sleep(2)
    while True:
        try:
            minYear = int(input(" What would be the minimum year of the range?\n     -"))
            maxYear = int(input("\n What would be the maximum year of the range?\n     -"))

        except ValueError:
            print("\n\n[ERRO]   Enter an appropriate input!\n\n")

        else:
            if minYear > maxYear:   # Pra caso algum animal tente colocar um intervalo impossível >:)
                print("\n\n[ERRO]   The minimum year of the range cannot be greater than the maximum year!\n\n")
            else:
                people = createIndividue(1, minYear, maxYear)
                return people

def multiplesPeoples():
    print("\nTo generate your data, we need a range of years during which this person might have been born.")
    sleep(2)
    while True:
        try:
            minYear = int(input(" What would be the minimum year of the range?\n     -"))
            maxYear = int(input("\n What would be the maximum year of the range?\n     -"))

            if minYear > maxYear or minYear == 0 or maxYear == 0:   # Pra caso algum animal tente colocar um intervalo impossível >:)
                print("\n\n[ERRO]   The minimum year of the range cannot be greater than the maximum year!\n\n")
                raise ValueError()
        
        except ValueError:
            print("\n\n[ERRO]   Enter an appropriate input!\n\n")

        else:
            break
            
    while True:
            try:
                quantityPeoples = int(input("  How many people do you wish to generate?"))
                if quantityPeoples <= 0:
                    print("The number of people generated cannot be equal to or less than 0!")
                    raise ValueError()
                
            except ValueError:
                print("\n\n[ERRO]   Enter an appropriate input!\n\n")

            else:
                break

    while True:
        try:
            options_yn = ("y", "n")
            repeat_ask = input("\n\n\n[ATTENTION] There is a possibility that some data may occasionally be duplicated. With a small number of people, this is usually rare, but as the number of people increases, the likelihood of this happening also increases. Would you like to prevent data duplication? [y/n]\n      - ").lower()
            print("\n\n\n")

            if repeat_ask not in options_yn:
                raise ValueError()
                        
        except ValueError or AttributeError:
            print("\n\nEnter a valid option! 'y' for yes, and 'n' for no.\n\n")

        else:
            if repeat_ask == "y":
                peoples = CreatePersons(quantityPeoples, minYear, maxYear, True)

            else:
                peoples = CreatePersons(quantityPeoples, minYear, maxYear, False)
            return peoples
            break

def save(saveObject):
    print("\n\n\nThe time has come to save your data!\n\n")
    sleep(2)
    print("     How would you like to save your data?\n")
    print("""
                    [1] JSON
                    [2] DataBase [ not yet available :( ]
                    [3] Text (at this terminal)
                    [Ctrl + c] to cancel

""")

    while True:
        try:
            response = input("\n\n      Your response:\n    -")

            if response not in options:
                raise ValueError()

        except ValueError:
            print("Enter a valid value!")

        else:
            if response == "1":
                saving = saveAsJSON_folder(saveObject)
                print(f"List saved successfully in {saving}")
                return saving
                break
            elif response == "2":
                print("This option not yet available ")
                break
            elif response == "3":
                print("\n\n\n\n\n")
                print(saveObject)
                print("\n\n\n\n\n")
                print("List printed successfully!")


if __name__ == "__main__":
    while True:
        options = ["1", "2", "3"]
        welcome()
        sleep(2)
        print("Welcome to peoples generator!")
        sleep(2)
        print("Here you can create fake peoples, and save it in JSON files!")
        sleep(5)
        print("Please note that these are FICTITIOUS data, which must not be used for malicious purposes!")
        sleep(3)

        print("\n \n        Choose an action by typing the number corresponding to your choice:")
        print("""
                [1] Generate a single person
                [2] Generate a table of people
                [3] Exit

        """)

        response = input("\n    -Your response:         \n-")

        if response not in options:
            print("Please, choose a valid option!\n\n")

        elif response == "1":
            list_person = singlePerson()

        elif response == "2":
            list_person = multiplesPeoples()

        else:
            goodBye()
            sleep(5)
            break

        save(list_person)
