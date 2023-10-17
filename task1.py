class Cash:
    def __init__(self, m=10000):
        self.money = m

    def top_up(self, x):
        self.money += x

    def count_1000(self):
        print(self.money//1000)

    def take_away(self, x):
        if self.money >= x:
            self.money -= x
        else:
            print('Ошибка! Недостаточно средств.')
