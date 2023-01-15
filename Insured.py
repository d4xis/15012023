class Insured():
    def __init__(self, name, surname, age, phone):
        self.name = name
        self.surname = surname
        self.age = age
        self.phone = phone

    def __str__(self):
        return f"Jméno: {self.name}, Příjmení: {self.surname}, Věk: {self.age}, Telefonní číslo: {self.phone}"