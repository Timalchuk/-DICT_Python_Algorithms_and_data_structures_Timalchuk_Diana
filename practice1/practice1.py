class Horse:
    def __init__(self, name, breed, category, areal, weight, color):
        self.name = name
        self.breed = breed
        self.category = category
        self.areal = areal
        self.weight = weight
        self.color = color

    def determine_category_areal(self):
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

    def determine_areal_category(self):

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

    def generate_message(self):
        category_areal = self.determine_category_areal()
        areal_category = self.determine_areal_category()
        message = f"Кінь {self.name} породи {self.breed}, що відноситься до {category_areal} {areal_category} порід, важить {self.weight} і має забарвлення {self.color}."
        return message

# Запрос данных у пользователя
name = input("Введіть ім'я коня: ")
breed = input("Введіть породу коня: ")
category = input("Введіть категорію коня (верховий/упряжний): ")
areal = input("Введіть ареал коня (американський/євроазіатський/африканський/австралійський): ")
weight = input("Введіть вагу коня: ")
color = input("Введіть забарвлення коня: ")

# Створення об'єкту класу Horse
horse = Horse(name, breed, category, areal, weight, color)

# Вивід повідомлення про коня
message = horse.generate_message()
print(message)