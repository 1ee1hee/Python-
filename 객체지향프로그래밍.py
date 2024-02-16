# 실습
# 제품 클래스 구현
# 속성 : 제품ID : str, 제품이름 : str, 제품가격 : int, 제조사이름 : str
# 정보은닉에 맞춰서 작성. 값을 대입 / 조회 하는 것은 변수 처리 방식을 할 수 있도록 구현
# 메소드 : 전체 정보를 출력하는 메소드
# 메소드 : setter-4개, getter-4개, 전체정보 출력하는 메소드 1개

class Product:
    def __init__(self, p_id : str, p_name : str, price : int, c_name : str):
        self.p_id = p_id
        self.p_name = p_name
        self.price = price
        self.c_name = c_name
        
    @property # decorator
    def p_id(self):
        # p_id의 getter
        print('getter p_id')
        return self.__p_id
    
    @p_id.setter
    def p_id(self, p_id):
        # p_id의 setter
        print('setter p_id', p_id)
        if len(p_id) >= 2:
            self.__p_id = p_id
    
    @property # decorator
    def p_name(self):
        # p_name의 getter
        print('getter p_name')
        return self.__p_name
    
    @p_name.setter
    def p_name(self, p_name):
        # p_name의 setter
        print('setter p_name', p_name)
        if len(p_name) >= 2:
            self.__p_name = p_name
            
    @property # decorator
    def price(self):
        # price의 getter
        print('getter price')
        return self.__price
    
    @price.setter
    def price(self, price):
        # price의 setter
        print('setter price', price)
        if price >= 10000:
            self.__price = price
            
    @property # decorator
    def c_name(self):
        # c_name의 getter
        print('getter c_name')
        return self.__c_name
    
    @c_name.setter
    def c_name(self, c_name):
        # c_name의 setter
        print('setter c_name', c_name)
        if len(c_name) >= 2:
            self.__c_name = c_name
            
    def print_info(self):
        print(f"제품ID : {self.p_id}, 제품이름 : {self.p_name}, 가격 : {self.price}, 회사이름 : {self.c_name}")
        
p = Product("Aem203", "컴퓨터", 3490000, "삼성")
p.print_info()
p.price = 50
print(p.price) # 바뀌지 않음


class Product2:
    def __init__(self, id, name, price, maker):
        self.id = id
        self.name = name
        self.price = price
        self.maker = maker
        
    # setter
    def set_id(self, id):
        if id:
            self.__id = id
            
    def set_name(self, name):
        if name:
            self.__name = name
            
    def set_price(self, price):
        if price:
            self.__price = price
            
    def set_maker(self, maker):
        if maker:
            self.__maker = maker
            
    # getter
    def get_id(self):
        return self.__id
    
    def get_name(self):
        return self.__name
    
    def get_price(self):
        return self.__price
    
    def get_maker(self):
        return self.__maker
    
    id = property(get_id, set_id)
    name = property(get_name, set_name)
    price = property(get_price, set_price)
    maker = property(get_maker, set_maker)
    
    def print_info(self):
        print(f"제품 id: {self.id}, 제품이름: {self.name}, 가격: {self.price}, 제조사:{self.maker}")
                
p = Product2('p-100', 'TV', 1000000, 'LG')
p.print_info()
print(p.price)

p.price = 500
p.print_info()

class Product3:
    def __init__(self, id, name, price, maker):
        self.id = id
        self.name = name
        self.price = price
        self.maker = maker
        
    # getter
    @property
    def id(self):
        return self.__id
    
    @property
    def name(self):
        return self.__name
    
    @property
    def price(self):
        return self.__price
    
    @property
    def maker(self):
        return self.__maker

    # setter
    @id.setter
    def id(self, id):
        if id:
            self.__id = id
    
    @name.setter
    def name(self, name):
        if name:
            self.__name = name
    
    @price.setter
    def price(self, price):
        if price:
            self.__price = price
            
    @maker.setter
    def maker(self, maker):
        if maker:
            self.__maker = maker
            
    def print_info(self):
        print(f"제품 id: {self.id}, 제품이름: {self.name}, 가격: {self.price}, 제조사:{self.maker}")
  
p3 = Product3("id-19999", '노트북', 5000000, '삼성')
p3.print_info()

p3.maker = 'Apple'
p3.print_info()

p3.maker=''
p3.print_info() # 변경 안됨


#######################################
class Person:
    def __init__(self, name, age, address = None):
        self.name = name
        self.age = age
        self.address = address
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        if len(name) >= 2:
            self.__name = name
            
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, age):
        if age >= 10:
            self.__age = age
    
    # 나이값 더하는 메소드
    def add_age(self, age):
        self.age = self.age + age
        
    def get_info(self):
        return f"이름 : {self.name}, 나이 : {self.age}, 주소 : {self.address}"
    

# Penson 속성: name, age, address
#Student 속성: grade(성적)    
class Student(Person):
    def __init__(self, name, age, address, grade):
        # name, age, address 는 부모객체에 초기화 -> Person클래스의 __init__() 을 호출
        super().__init__(name, age, address) # 부모클래스의 __init__()메소드를 호출
        self.grade = grade
    
    # get_info()메소드를 overriding -> grade 정보까지 추가
    def get_info(self):
        # name, age, address는 Person의 get_info()를 이용해서 조회
        i = super().get_info()
        return f"{i}, 성적 : {self.grade}"
    
s = Student('김학생', 15, '서울', 10)
print(s.get_info())

s.add_age(-2)
print(s.get_info())


# 다중 상속시 메소드 호출 순서(MRO)
# A_1, A_2 <- B_1 <- C -> B_2
class A_1:
    pass
class A_2:
    pass
class B_1(A_1, A_2):
    pass
class B_2:
    pass
class C(B_1, B_2):
    pass

print(C.mro())
# [<class '__main__.C'>, <class '__main__.B_1'>, <class '__main__.A_1'>, <class '__main__.A_2'>, <class '__main__.B_2'>, <class 'object'>]