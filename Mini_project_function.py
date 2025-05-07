
ledger = {} 

def input_intData(number):
    num = input(number).strip()  


    # 입력값이 비었는지 확인
    if not num:
        print('\n▶ 입력된 데이터가 없습니다.') # 오류 메시지 출력
        return None # None 반환
    
    # 입력값이 숫자인지 확인
    if num.isdigit(): # 문자열이 숫자로만 이루어졌는지 검사
        return int(num)  # 통과 => 숫자 반환
    
    # 숫자가 아닌 경우 처리
    print('\n▶ 숫자만 입력해 주세요.')
    return None  # None 반환
    
    


def input_strData(msg):
    msgS = input(msg).strip()  
    
    # 입력 값이 비었는지 확인
    if not msgS:
        
        return None, '\n▶ 입력된 데이터가 없습니다.'
    
    if not msgS.isalpha(): 
        
        return None, '\n▶ 문자만 입력해 주세요.'

    
    return msgS

# 잔액 확인 함수 : 사용자의 ledger 딕셔너리를 이용하여 수입, 지출, 잔액을 계산하는 함수를 만들었음
def balance_check(ledger):
    balance = 0  # 초기 잔액 설정
    total_income = 0  # 총 수입
    total_expense = 0  # 총 지출

   
    for key,value in ledger.items(): 
        
        if value > 0: # 값이 양수이면 income
        
            total_income += value 
        
        else: # 값이 음수이면 지출
        
            total_expense += value 
            # => Mini_project.py => dict key = vlaue에 (-)를 붙임 => ledger[key] = -value
        
        balance += value  # 잔액 업뎃

    # 출력: ,는 천단위마다 구분
    print("\n====== 현재 잔액 요약 ======")
    print(f"총 수입  : {total_income:,}원")
    print(f"총 지출  : {total_expense:,}원")
    print(f"현재 잔액: {balance:,}원")
    print("===========================")

    return balance

