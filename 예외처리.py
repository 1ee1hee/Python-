# 실습

# try = except
print("프로그램 시작") # 1
try:
    num = int(input()) # 2 Exception 발생가능성이 있는 코드
    result = 10 // num # 3
    print(result) # 4
    
except:
    print('실행도중 문제가 발생') # 5
print('프로그램 종료') # 6

# Exception이 발생하지 않을 때 순서
# 1 -> 2 -> 3 -> 4 -> 6
# Exception이 발생할 때 순서
# 1 -> 2(x) -> 5 -> 6

#################################
print('프로그램 시작') # 1
try:
    num = int(input()) # 2  ValueError    
    result = 10 // num # 3  ZeroDivisionError
    print(result) # 4
    print(result2) # NameError Exception 발생
    
except ValueError as ve: # ValueError Exception은 여기서 처리
    print('숫자가 아니여서 예외 발생: ', ve) # 5-1
    
except ZeroDivisionError as ze : #ZeroDivisionError Exception은 여기서 처리
    print('0으로 나눌 수 없습니다: ', ze) # 5-2

except:
    print('ValueError, ZeroDivisionError를 제외한 나머지 Exception을 처리하는 except block')
print('프로그램 종료') # 6

# ValueError 발생 시
# 1 -> 2(x) -> 5-1 -> 6
# ZeroDivisionError 발생 시
# 1 -> 2 -> 3(x) -> 5-2 -> 6

##################################
print('시작')
try: 
    print(1)
    a = 10/0
    print(2)
    
except NameError:
    print(3)

finally:
    print(4)

print('종료')

# 구문 순서
# 1. try - except - finally
# 2. try - except 
# 3. try - finally

class NotEnoughStockException(Exception):
    def __init__(self, stock_amount, order_amount):
        self.stock_amount = stock_amount
        self.order_amount = order_amount
    
    def __str__(self):
        return f"재고량 보다 많은 개수를 주문했습니다. 재고량 : {self.stock}, 주문량 : {self.order_amount}"
    
# 주문처리 함수
def order(order_amount):
    print("재고량 조회")
    stock_amount = 10
    
    if stock_amount < order_amount:
        raise NotEnoughStockException(stock_amount, order_amount)
    
    print("주문처리")
    print("주문정보 저장")
    stock_amount -= order_amount
    print('주문완료. 남은 재고량: ', stock_amount)
    
try: 
    order(50)
except NotEnoughStockException as e:
    print('전체 주문 실패', e)
    order(e.stock_amount)