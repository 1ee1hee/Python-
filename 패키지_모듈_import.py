# 실습
import my_module
from my_package import calculator as c

print(my_module.__version__)
print(my_module.greeting('홍길동'))

print(c.plus(1, 2))
print(c.minus(3, 2))
print(c.multiply(3, 6))
print(c.divide(8, 2))

from my_module import greeting, Person
print(greeting('이순신'))
print(Person('유관순', 30))