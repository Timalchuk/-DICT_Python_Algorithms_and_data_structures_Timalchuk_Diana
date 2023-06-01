import random
from main_modul import Horse


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


def abstract_object():
    return None
