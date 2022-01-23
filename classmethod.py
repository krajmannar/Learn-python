class klass(object):
    give_raise = 1.02

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        # self.email = first + '.'+ last +'@email.com'

    @classmethod
    def setraise(cls, value):
        cls.give_raise = value

    @classmethod
    def fromstrings(cls, name):
        first, last, pay1 = name.split('-')
        pay = int(pay1)
        return cls(first, last, pay)


    @property
    def fullname(self):
        print('{} {}'.format(self.first, self.last))

    @fullname.setter
    def fullname(self, name):
        self.first, self.last = name.split(' ')



    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def pay(self):
        return self.__pay

    @pay.setter
    def pay(self, value):
        if value < 10000:
            self.__pay = 10000
        elif value > 20000:
                self.__pay = 20000
        else:
            self.__pay = value


if __name__ == '__main__':

    emp1 = klass('raj', 'mannar', 25000)
    emp2 = klass('lakshmi', 'prasanna', 5000)
    print(emp1.email)
    print(emp1.pay)
    print(emp2.pay)
    print(emp1.give_raise)

    klass.setraise(1.07)
    print(klass.give_raise)
    print(emp1.give_raise)
    print(emp2.give_raise)

    emp1.fullname

    emp1.first = 'sai'
    print(emp1.email)
    emp1.fullname

    emp3 = klass.fromstrings('sai-kaushik-30000')
    print(emp3.email)
    print(emp3.pay)
    emp3.fullname
    print(emp3.give_raise)
    emp3.fullname = 'alice blue'
    print(emp3.first)
    print(emp3.last)
    print(emp3.email)
    emp3.fullname
    print(emp3.give_raise)

