# 실습
#1. 주민 번호 "901211-1027213"의 앞 6자리만 조회해서 출력하시오
id = "901211-1027213"
print(id[:6])
print(id.split('-')[0])

#2. "안녕하세요"를 10번 출력하시오.
print("안녕하세요" * 10)

#3. 다음 문자열의 글자수를 출력하시오.
str_value = "akdlclkdkdlelql39du7마구0ㅌ" 
print(len(str_value))

#4.
name = "TV"
price = 300000
maker = "LG"
# 위 변수의 값을 다음과 같은 형태로 출력하시오.
# "제품명" : TV, 가격 : 300000, 제조사 : LG"
print(f"\"제품명 : {name}, 가격 : {price}, 제조사 : {maker}\"")

#5.
fruits = "사과 복숭아 귤 배"
# 위 fruits에 "수박이 있는지 확인하는 코드를 작성하시오"
print("수박" in fruits)
# -------------------------------
a = "수박" in fruits
"있음" if a == True else "없음"

#6.
str_value1="aldkjaldjfalfjlksajfladlkaalalkdjfa"
# str_value1 문자열안에 a가 몇개 있는지 출력하시오
print(str_value1.count('a'), "개")