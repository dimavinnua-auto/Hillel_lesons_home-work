# Створіть клас геометричної фігури "Ромб". Клас повинен мати наступні атрибути:

# сторона_а (довжина сторони a).
# кут_а (кут між сторонами a і b).
# кут_б (суміжний з кутом кут_а).
# Необхідно реалізувати наступні вимоги:

# Значення сторони сторона_а повинно бути більше 0.
# Кути кут_а та кут_б повинні задовольняти умову: кут_а + кут_б = 180
# Протилежні кути ромба завжди рівні, тому при заданому значенні кут_а, значення кут_б обчислюється автоматично.
# Для встановлення значень атрибутів використовуйте метод __setattr__.

class Romb():
    def __init__(self, stor, angle):
        self.stor_a = stor
        self.stor_b = stor
        self.stor_c = stor
        self.stor_d = stor

        self.angle_a = angle
        self.angle_b = 180 - self.angle_a
        self.angle_c = self.angle_a
        self.angle_d = self.angle_b

    def __setattr__(self, name, value):
        if name.startswith("stor") and value <= 0:
            raise ValueError("Сторона має бути більшою за 0")

        if name.startswith("angle") and not (0 < value < 180):
            raise ValueError("Кут має бути в діапазоні (0, 180)")

        super().__setattr__(name, value)

r = Romb(5,80)
print(r.stor_a)
print(r.angle_b, r.angle_a)


