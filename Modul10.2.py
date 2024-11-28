import time
from threading import Thread


class Knight(Thread):
    total_enemies = 100

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.days = 0

    def run(self):
        print(f"{self.name}, на нас напали!")
        while Knight.total_enemies > 0:
            time.sleep(1)
            self.days += 1

            if Knight.total_enemies > 0:

                Knight.total_enemies -= self.power

                if Knight.total_enemies < 0:
                    Knight.total_enemies = 0

                print(f"{self.name}, сражается {self.days} день(дня)..., осталось {Knight.total_enemies} воинов.")

        print(f"{self.name} одержал победу спустя {self.days} дней(дня)!")


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print("Все битвы закончились!")
