class Horse:
    def __repr__(self) -> str:
        return f"Horse(name={self.name}, breed={self.breed}, category={self.category}, areal={self.areal}, weight={self.weight},color={self.color})"


    def __init__(self, name: str, breed: str, category: str, areal: str, weight: float, color: str):
        self.name = name
        self.breed = breed
        self.category = category
        self.areal = areal
        self.weight = weight
        self.color = color

    def determine_category_areal(self) -> str:
        if self.category == "верховий":
            if self.breed in ["ахалтекінська", "арабська", "чистокровна верхова", "терська"]:
                return "верховим"
            else:
                return "невідомою"
        elif self.category == "упряжний":
            if self.breed in ["орловська", "російська рисиста", "володимирський важковоз"]:
                return "важковозами"
            elif self.breed in ["російський тяжкий", "російський рисисто-гнідий"]:
                return "рисистими"
            else:
                return "невідомою"

    def determine_areal_category(self) -> str:

        if self.areal == "Північна та Південна Америка":
            return "американським"
        elif self.areal == "Європа та Азія":
            return "євроазіатським"
        elif self.areal == "Африка":
            return "африканським"
        elif self.areal == "Австралія":
            return "австралійським"
        else:
            return "невідомим"

    def generate_message(self) -> str:
        category_areal = self.determine_category_areal()
        areal_category = self.determine_areal_category()
        message = f"Кінь {self.name} породи {self.breed}, що відноситься до {category_areal} {areal_category} порід, важить {self.weight} і має забарвлення {self.color}."
        return message

# Запрос данных у пользователя
name = input("Введіть ім'я коня: ")
breed = input("Введіть породу коня: ")
category = input("Введіть категорію коня (верховий/упряжний): ")
areal = input("Введіть ареал коня (американський/євроазіатський/африканський/австралійський): ")
weight = float(input("Введіть вагу коня: "))
color = input("Введіть забарвлення коня: ")

# Створення об'єкту класу Horse
horse = Horse(name, breed, category, areal, weight, color)

# Вивід повідомлення про коня
message = horse.generate_message()
print(message)
#  вага не є числом
horse1 = Horse("Буцефал", "Арабська", "верховий", "Європа та Азія", "1000 кг", "червоне")

#  порода невідома
horse2 = Horse("Імператор", "невідома порода", "верховий", "Африка", 500, "біле")