# 실습

# 간단한 터미널 기반 메모장
# 1. 사용자로부터 파일명을 입력받는다.
# 2. 사용자로부터 파일에 저장할 문장을 입력받아 파일에 저장한다
    # 한줄씩 입력받는다
    # 사용자가 !q를 입력하면 저장 후 종료 한다.
# 3. 사용자가 저장한 파일을 읽어서 출력한다.

print("저장할 파일명을 입력하세요")
file_name = input("파일명: ")
print(f"{file_name}에 저장합니다")
print("="*50)

with open(file_name, 'wt', encoding='utf-8') as fw:
    print("저장할 내용을 입력하세요")
    print("=" * 30)
    while True:
        line_txt = input(">")
        if line_txt == "!q":
            break
        fw.write(line_txt+"\n")
print("종료")


# member.csv파일을 읽어 각 열의 값을 배열에 담는다
file_name = 'member.csv'
names = []
ages = []
addresses = []
with open(file_name, 'rt', encoding='utf-8') as fr:
    for idx, line_txt in enumerate(fr):
        if idx == 0 : 
            continue
        name, age, address = line_txt.strip().split(',')
        names.append(name)
        ages.append(age)
        addresses.append(address)
        
print(names)
print(ages)
print(addresses)

# 행 단위 조회
for info in zip(names, ages, addresses):
    print(info)