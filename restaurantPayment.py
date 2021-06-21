from abc import ABC, abstractmethod
class restaurant(ABC):
    def check(self, amount):
        print("Your total comes to $", amount)
#passes argument through encapsulation
    @abstractmethod
    def payment(self, amount):
        pass

class CreditPayment(restaurant):
#defined payment from parent check class
    def payment(self, amount):
        print('Your total of ${} exceeded your $1000 limit '.format(amount))

obj = CreditPayment()
obj.check("1200")
obj.payment("1000")
