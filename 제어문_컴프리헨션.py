# 실습
# 1. 다음 점수 구간에 맞게 학점을 출력하세요
# 91 ~ 100 : A학점
# 81 ~ 90 :  B학점
# 71 ~ 80 :  C학점
# 61 ~ 70 :  D학점
# 60이하   :  F학점
n = int(input()) # 점수 입력
if n < 0 or n > 100:
    print(f"{n} 올바른 점수가 아닙니다. 0~100 까지의 값을 넣으세요")
elif n > 90 :
    print("A학점")
elif n > 80 :
    print("B학점")
elif n > 70 :
    print("C학점")
elif n > 60 :
    print("D학점")
else:
    print("F학점")


# 2. 사용자로 부터 ID를 입력 받은 뒤 입력받은 ID가 5글자 이상이면 "사용할 수 있습니다."를 5글자 미만이면 "사용할 수 없는 ID입니다."를 출력하세요.
id = input("ID: ")
if len(id) >= 5:
    print("사용할 수 있습니다")
else:
    print("사용할 수 없는 ID입니다")
    
# 3. 사용자로부터 우리나라 도시명을 입력 받은 뒤 입력받은 도시명이 서울이면 "특별시"를 인천,부산,광주,대구,대전,울산 이면 "광역시"를 나머지는 "특별시나 광역시가 아닙니다."를 출력하세요.
city = input("도시:").strip() # 공백 거르기
cities = ["인천", "부산", "광주", "대구", "대전", "울산"]
if city == "서울":
    print("특별시")
elif city in c:
    print("광역시")
else:
    print("특별시나 광역시가 아닙니다")
    
# 4. 아래 리스트의 평균을 구하시오
jumsu = [100, 90, 100, 80, 70, 100, 80, 90, 95, 85]
sum = 0
for i in jumsu:
    sum += i
average = sum / len(jumsu)
print(average)

# 5. 위 jumsu리스트에서 평균점수이상은 pass, 미만은 fail을 index번호와 함께 출력하시오. (ex: 0-pass, 1-pass, 2-fail)
for index, value in enumerate(jumsu):
    if value >= average:
        print(f"{index}-pass")
    else:
        print(f"{index}-fail")
        
# 같은 코드
for index, value in enumerate(jumsu):
    print(f'{index}-{"pass"if value >= average else "fail"}')

# 6. 아래 리스트 값들 중 최대값을 조회해 출력
jumsu = [60, 90, 80, 80, 70, 55, 80, 90, 95, 85]
result = sorted(jumsu, reverse=True)
print(result[0])

# 6-1.
jumsu = [60, 90, 80, 80, 70, 55, 80, 90, 95, 85]
max_value = -1 # 최대값을 저장할 변수, 각각의 원소들을 이 변수 값과 비교해 큰값으로 이 변수값을 변경
for value in jumsu:
    if value > max_value:
        max_value = value

print("최대값: ", max_value)

print(min(jumsu), max(jumsu)) # 최소, 최대

#7. 다음 리스트 중에서 "쥐"와 "토끼" 제외한 나머지를 출력하세요.
str_list = ["쥐", "소", "호랑이", "토끼", "용", "뱀"]
str_list.remove("쥐")
str_list.remove("토끼")
print(str_list)

# 7-1.
str_list = ["쥐", "소", "호랑이", "토끼", "용", "뱀"]
s_list = []
for i in str_list:
    if i != "쥐" and i != "토끼":
        s_list.append(i)
print(s_list)

# 7-2.
str_list = ["쥐", "소", "호랑이", "토끼", "용", "뱀"]
for value in str_list:
    if value in ["쥐", "토끼"]:
        continue
    print(value)
    
# 8. 사용자로부터 정수를 입력받아 그 단의 구구단을 출력하시오
num = int(input("단을 입력하시오: "))
for i in range(1, 10):
    print(f"{num} X {i} = {num * i}")
    
# 컴프리헨션
# 9. 다음 리스트가 가진 값에 두배(* 2)를 가지는 새로운 리스트를 만드시오. (리스트 컴프리헨션 이용)
lst = [10, 30, 70, 5, 120, 700, 1, 35]
l = [value*2 for value in lst]
print(l)

# 10. 다음 리스트가 가진 값에 10배의 값을 가지는 값을 (원래값, 10배값) 의 튜플 묶음으로 가지는 리스트를 만드시오 (리스트 컴프리헨션 이용)
# Ex) [(10,100), (30,300), .., (35, 350)]
lst = [10, 30, 70, 5, 5, 120, 700, 1, 35, 35]
l = [(value, value * 10) for value in lst]
print(l)

# 11. 다음 리스트가 가진 값들 중 3의 배수만 가지는 리스트를 만드시오. (리스트 컴프리헨션 이용)
lst2 = [ 3, 20, 33, 21, 33, 8, 11, 10, 7, 17, 60, 120, 2]
l = [value for value in lst2 if value % 3 == 0]
print(l)

# 12. 다음 파일이름들을 담은 리스트에서 확장자가 exe인 파일만 골라서 새로운 리스트에 담으시오.(string의 endswith()함수 이용)
file_name=["test.txt", "a.exe", "jupyter.bat", "function.exe", "b.exe", "cat.jpg", "dog.png", "run.exe", "i.dll"]
l = [value for value in file_name if value.endswith(".exe")]
print(l)

# 13. 다음 중 10글자 이상인 파일명(확장자포함)만 가지는 리스트를 만드시오.
file_name=["mystroy.txt", "a.exe", "jupyter.bat", "function.exe", "b.exe", "cat.jpg", "dog.png", "run.exe", "i.dll"]
l = [(value, len(value)) for value in file_name if len(value)>=10]
print(l)

# 13-1. 확장자를 뺀 파일명이 5글자 이상인 파일들
l = [file for file in file_name if len(file.split(".")[0]) >= 5]
print(l)

# 14. 다음 리스트에서 소문자만 가지는 새로운 리스트를 만드시오.
str_list = ["A", "B", "c", "D", "E", "F", "g", "h", "I", "J", "k"]
l = [value for value in str_list if value.islower()]
print(l)

# 14-1. 대문자만 가지는 새로운 리스트를 만드시오
l2 = [value for value in str_list if value.isupper()]
print(l2)