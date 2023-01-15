# Soubor Main.py
import Insured

class Main():
    def __init__(self):
        self.insured_list = []

    # Funkce pro vytvoření nového pojištěného
    def create_insured(self):
        name = input("Zadejte jméno: ")
        surname = input("Zadejte příjmení: ")
        age = input("Zadejte věk: ")
        phone = input("Zadejte telefonní číslo: ")
        new_insured = Insured.Insured(name, surname, age, phone)
        self.insured_list.append(new_insured)
        print("Nové pojištěné bylo vytvořeno.")

    # Funkce pro vyhledání pojištěného
    def find_insured(self):
        name = input("Zadejte jméno: ")
        surname = input("Zadejte příjmení: ")
        for insured in self.insured_list:
            if insured.name == name and insured.surname == surname:
                print(insured)
                return
        print("Pojištěné nebylo nalezeno.")

    # Funkce pro zobrazení seznamu pojištěných
    def show_insured_list(self):
        print("Seznam pojištěných:")
        for insured in self.insured_list:
            print(insured)

    # Funkce pro spuštění menu
    def run(self):
        while True:
            print("1 - Vytvořit nové pojištěné")
            print("2 - Vyhledat pojištěné")
            print("3 - Zobrazit seznam pojištěných")
            print("4 - Konec aplikace")

            option = int(input("Zadejte volbu: "))

            if option == 1:
                self.create_insured()
            elif option == 2:
                self.find_insured()
            elif option == 3:
                self.show_insured_list()
            elif option == 4:
                break
            else:
                print("Neplatná volba. Zkus znovu")

if __name__ == "__main__":
    main = Main()
    main.run()


