# 실습
import re

# info 변수는 한줄에 한사람의 data가 있고 구성은 이름, 이메일 주소, 주민번호 순서로 되어있다
info ='''김정수 kjs@gmail.com 801023-1010221
박영수 pys.abc@gmail.com 700121-1120212
이민영 lmy-abc@naver.com 820301-2020122
김순희 ksh@daum.net 781223-2012212
오주연 ojy@daum.co.kr 900522-1023218
'''

# Email 주소만 추출해 출력
pattern = r'[a-z\.\-\@]+[a-z]'
p = re.compile(pattern)
m = p.findall(info)
print('email 주소: ', m)

# 주민번호들만 조회해서 출력
pattern = r'[\d\-]+[\d]'
p = re.compile(pattern)
m = p.findall(info)
print('주민번호: ',m)

# 다른 방법
# Email 주소만 추출해서 출력
pattern = r'[\w\-\.]+@[\w\-\.]+[\w\-]{2,4}'
p = re.compile(pattern)
result = p.findall(info)
print(result)

# 주민번호 조회 출력
pattern = r'\d{6}-[012349]\d{6}'
p = re.compile(pattern)
result = p.findall(info)
print(result)

# finditer
result = p.finditer(info)
print(type(result))
for m in result:
    print(m)
    
# 문자열 변경
txt = """오늘은     수요일      입니다.
내일은     목요일      입니다.
글피는    금\t요일       입니다."""

pattern = r'\s+'
p = re.compile(pattern)
result, cnt = p.subn(' ', txt)
print('변경개수:', cnt)
print(result)

txt = 'test1, test2, test3, test4, test50'
pattern = r'\D'
p = re.compile(pattern)
result, cnt = p.subn('', txt)
print('변경개수: ', cnt)
print(result)

# 나누기(split)
txt = "사과,복숭아,배|수박"
p = re.compile(r'[,|]')
print(p.split(txt))

# grouping
txt = "abc@naver.com, test@daum.net, my_mail@gmail.com"
pattern = r'(\w+)@(\w+\.\w+)'
p = re.compile(pattern)
print(p.findall(txt))
for id, domain in p.findall(txt):
    print(f'ID: {id}, 도메인: {domain}')
    
for m in p.finditer(txt):
    print(m.group())
    print('계정ID: ', m.group(1))
    print('도메인: ', m.group(2))
    print("="*30)
    
    
# 패턴내 특정 부분 변경
print(info)
# 주민번호 마지막 6개 숫자 #으로 변경
pattern = r'(\d{6}-[012349])\d{6}'
p = re.compile(pattern)
result = p.sub('\g<1>######', info)
print(result)

# Greedy(최대일치) 와 Non-Greedy(최소일치)
txt = "<div>파이썬 <b>정규표현식</b> </div>"
# <div><b></b></div> 태그만 조회
pattern = r'<.+?>'
p = re.compile(pattern) # Non-Greedy pattern
print(p.findall(txt))


# 전/후방 탐색
info = """TV 300001원 30개
컴퓨터 2300001원 50개
모니터 4200001원 70개
"""
# 가격만 조회
# pattern = r'\d+원'
# 가격만 조회 -> 조회결과에서 '원'은 뺀다
pattern = r'\d+(?=원)' # 전방탐색
p = re.compile(pattern)
print(p.findall(info))


info = """TV $300001 30개
컴퓨터 $2300001 50개
모니터 $4200001 70개
"""
# 가격만 조회
# pattern = r'\$\d+'
# 가격만 조회 -> 결과에서 $는 뺀다
pattern = r'(?<=\$)\d+' # 후방탐색
p = re.compile(pattern)
print(p.findall(info))