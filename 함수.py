# 실습
# 1. 사용자가 입력한 단의 구구단을 출력하는 함수를 구현(매개변수로 단을 받는다.)
def gugudan(num):
    for i in range(1, 10):
        print(f"{num} X {i} = {num * i}")

gugudan(3)

# 2. 시작 정수, 끝 정수를 받아 그 사이의 모든 정수의 합을 구해서 반환하는 함수를 구현(ex: 1, 20 => 1에서 20 사이의 모든 정수의 합계)
def summation(start:int, end:int) -> int:
    sum = 0
    for i in range(start, end+1):
        sum += i
    return sum

print(summation(1, 5))

# 3. 2번 문제에서 시작을 받지 않은 경우 0을, 끝 정수를 받지 않으면 10이 들어가도록 구현을 변경
def summation2(start = 0, end = 10):
    sum = 0
    for i in range(start, end + 1):
        sum += i
    return sum

print(summation2())

# 3-1. 같은 코드
def summation2_1(start = 0, end = 10):
    return sum(range(start, end + 1))
print(summation2_1())

def accumulate3(**kwargs):
    # 가변인자를 사용할 경우에는 docstring을 필수로 잘 닫아줘야 함
    start = kwargs['start'] # kwargs.get('start', 0)
    stop = kwargs['stop']
    operator = kwargs['operator']
    result = None
    if operator == '+':
        result = sum(range(start, stop+1))
    elif operator == 'x':
        result = 1
        for i in range(start, stop+1):
            result *= i
    return result

print(accumulate3(start = 1, stop = 3, operator = '+'))
print(accumulate3(start = 1, stop = 3, operator = 'x'))


# 4. 체질량 지수는 비만도를 나타내는 지수로 키가 a미터 이고 몸무게가 b kg일때 b/(a**2) 로 구한다.
# 체질량 지수가
#- 18.5 미만이면 저체중
#- 18.5이상 25미만이면 정상 
#- 25이상이면 과체중
#- 30이상이면 비만으로 하는데 
#몸무게와 키를 매개변수로 받아 비만인지 과체중인지 반환하는 함수를 구현하시오.
def body(a, b):
    bmi = b/((a/100)**2)
    if bmi >= 30:
        print(f"체질량은 {bmi} 비만입니다")
        return "비만"
    elif bmi >= 25:
        print(f"체질량은 {bmi} 과체중입니다")
        return "과체중"
    elif bmi >= 18.5:
        print(f"체질량은 {bmi} 정상입니다")
        return "정상"
    else:
        print(f"체질량은 {bmi} 저체중입니다")
        return "저체중"
    
print(body(180, 70))

def check_bmi(tall, weight):
    """
    bmi 지수를 계산해서 비만도 정도를 알려주는 함수
    parameter:
        tall: float, int - 키를 미터로 입력받는다
        weight : float, int - 몸무게를 kg으로 입력받는다
    return:
        str - 비만도 (저체중, 정상, 과체중, 비만)
        tuple - (비만도, bmi 지수)
    raise:
    """
    bmi = weight/(tall**2)
    result = None
    if bmi < 18.5:
        result = '저체중'
    elif bmi < 25:
        result = '정상'
    elif bmi < 30:
        result = '과체중'
    else:
        result = '비만'
    return result, round(bmi, 2) # round는 반올림 함수 소수점 2번째 자리까지 표현

print(check_bmi(1.8, 90))

# 람다식
# 5. filter()를 이용해 다음 리스트에서 양수만 추출해 리스트 구현
ex1 = [1, -10, -2, 20, 3, -5, -7, 21]
a = filter(lambda num : num > 0, ex1)
a = list(a)

b = [x for x in ex1 if x>0]
print(a, b)

# filter()에서 사용하는 함수: 매개변수 - iterable의 원소를 받는 매개변수를 하나 선언
#                           반환값-bool : 원소가 조건을 만족하는지 여부


# 6. filter()와 map()을 이용해 다음 리스트에서 음수만 추출한 뒤 그 2 제곱한 값들을 가지는 리스트를 구현
ex2 = [1, -10, -2, 20, 3, -5, -7, 21]
a = filter(lambda num : num < 0, ex2)
b = map(lambda num : num**2, a)
b = list(b)

c = [i for i in ex2 if i<0]
d = [j**2 for j in c]
print(b, d)

b2 = map(lambda num : num**2, filter(lambda num : num < 0, ex2))
b2 = list(b2)
print(b, b2)