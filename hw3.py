from threading import Thread, Lock
import random
import time


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = Lock()

    def deposit(self):
        for i in range(100):
            amount = random.randint(50, 500)
            self.lock.acquire()
            try:
                self.balance += amount
                if self.balance >= 500 and self.lock.locked():
                    print(f'Пополнение: {amount}, Баланс: {self.balance}')
            finally:
                self.lock.release()
            time.sleep(0.001)

    def take(self):
        for i in range(100):
            amount = random.randint(50, 500)
            print(f'Запрос на {amount}')
            self.lock.acquire()
            try:
                if amount <= self.balance:
                    self.balance -= amount
                    print(f'Снятие: {amount}, баланс: {self.balance}')
                else:
                    print('Запрос отклонён, недостаточно средств')
            finally:
                self.lock.release()
            time.sleep(0.001)


bk = Bank()

th1 = Thread(target=bk.deposit)
th2 = Thread(target=bk.take)

th1.start()
th2.start()

th1.join()
th2.join()

print()
print(f'Итоговый баланс: {bk.balance}')
