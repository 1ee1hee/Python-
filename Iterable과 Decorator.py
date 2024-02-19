# 실습

l = [1, 2, 3]
l_iterator = iter(l)
print(type(l_iterator))

print(next(l_iterator))
print(next(l_iterator))

def for_in(iterable):
    iterator = iter(iterable)
    while True:
        try:
            v = next(iterator)
            print(v)
        except:
            break
for_in(l)

# Iterable 과 Iterator 구현
# Iterable 과 Iterator를 다른 클래스로 구현

#Iterable
class MyIterable:
    def __init__(self, *args):
        # *args : 제공해 줄 원소들을 가면인자로 받음
        self.values = args # 튜플
        
    def __str__(self):
        return str(self.values)
    
    def __iter__(self):
        return MyIterator(self.values)
        # MyIterator가 MyIterable의 values값을 사용할 수 있도록 전달
        
class MyIterator:
    def __init__(self, values):
        self.values = values
        self.index = 0
        
    def __next__(self):
        if len(self.values) <= self.index:
            raise StopIteration()
        ret_value = self.values[self.index]
        self.index += 1
        return ret_value
    
mi = MyIterable(1, 2, 3, 4)
print(mi)
m_iter = iter(mi)
print(type(m_iter))

print(next(m_iter))
print(next(m_iter))

class MyIterable2:
    
    def __init__(self, *args):
        """
        *args: 제공해줄 원소들을 가변인자 받는다
        """
        self.values = args # 튜플
        self.index = 0
        
    def __str__(self):
        """제공할 원소들을 가진 튜플을 문자열로 묶어서 반환"""
        return str(self.values)
    
    def __iter__(self):
        """iterable은 __iter__()를 반드시 재정의 해야한다
        Iterator 객체를 생성해서 반환하도록 처리"""
        return self # MyIterator가 MyIterable의 values값을 사용할 수 있도록 전달 

    def __next__(self):
        """next(iterator) 했을 때 호출된 메소드. 다음 원소를 제공. 제공할 다음 원소가 없으면 StopIteration Exception
        발생시킨다.
        """
        # self.values의 값을 하나씩 조회해서 return
        if len(self.values) <= self.index:
            raise StopIteration()
        ret_value = self.values[self.index]
        self.index += 1
        return ret_value
    
    def __getitem__(self, index):
        # 객체[index] : self = 객체, index = index
        return self.values[index]
    
for v in MyIterable2(1, 2, 3, 4, 5, 6, 7):
    print(v, end = '\t')
    
mi2 = MyIterable2(1, 2, 3, 4, 5)
print(type(mi2))
m_iter2 = iter(mi2)
print(type(m_iter2))


# Generator
# range()를 generator로 구현
def my_range(start, end = None, step = 1):
    if end == None:
        end = start
        start = 0
    while True:
        if start >= end:
            break
        yield start
        start += step

print(type(my_range(5, 8)))

gen = my_range(5, 8)
print(next(gen))
print(next(gen))

# Decorator
# 함수가 실행된 실행시간을 재는 decorator
import time
time.time()

print(1)
time.sleep(2) # 2초 멈춤
print(2)

def timechecker_decorator(func):
    def wrapper():
        s = time.time()
        func()
        e = time.time()
        print(f"걸린시간 : {e-s}")
    return wrapper

@timechecker_decorator
def test1():
    print(1)
    time.sleep(3)
    print(2)
    
@timechecker_decorator
def test2():
    print(1)
    time.sleep(2)
    print(2)
    
@timechecker_decorator
def test3():
    print(1)
    time.sleep(5)
    print(2)
    
s = time.time()
test1()
e = time.time()
print(e - s)

test1()
test2()
test3()


def timechecker_decorator1(func):
    def wrapper():
        s = time.time()
        func()
        e = time.time()
        print(f'{func.__name__} 함수의 걸린시간 : {round(e-s, 2)} 초')
    return wrapper

@timechecker_decorator1
def test():
    print('test')
    
test()