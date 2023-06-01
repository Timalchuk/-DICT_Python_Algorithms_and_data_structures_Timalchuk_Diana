import random
from typing import List, Union

class Horse:
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

class Generator:
    @staticmethod
    def generate_horse() -> Horse:
        names = ["Буцім", "Мак", "Харт", "Фредді", "Санчо", "Багіра", "Рейн", "Роксі", "Смокі", "Джек"]
        breeds = ["ахалтекінська", "арабська", "чистокровна верхова", "терська", "орловська", "російська рисиста", "володимирський важковоз", "російський тяжкий", "російський рисисто-гнідий"]
        categories = ["верховий", "упряжний"]
        areals = ["Північна та Південна Америка", "Європа та Азія", "Африка", "Австралія"]
        colors = ["чорний", "коричневий", "білий", "сірий", "рудий"]

        # Генерувати випадкові значення для кожної властивості коня
        name = random.choice(names)
        breed = random.choice(breeds)
        category = random.choice(categories)
        areal = random.choice(areals)
        weight = round(random.uniform(150, 1000), 2)  # вага від 150 до 1000 кг
        color = random.choice(colors)

        # Створити об'єкт класу Horse з випадковими властивостями
        horse = Horse(name, breed, category, areal, weight, color)
        return horse
# Створення випадкового коня
random_horse = Generator.generate_horse()

# Вивід повідомлення про випадкового коня
message = random_horse.generate_message()
print(message)


def generate_1000(self) -> list:

    plist = list()
    for i in range(1000):
        plist.append(self.generate_horse())
    return plist


def generate_10_000(self) -> list:
    plist = [self.generate_horse() for i in range(10000)]
    return plist
