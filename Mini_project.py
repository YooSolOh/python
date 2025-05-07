
import Mini_project_function as pf



user_ledger =  {}
menu = {1:'수입 입력하기', 
        2:'지출 입력하기', 
        3:'현재 저장된 내역 출력하기', 
        4:'수익과 지출의 잔액 확인하기', 
        5:'종료하기'}


while True:
    print('    ╭──                             ──╮')
    print("{:^43}".format("_______Ledger__Log_______"))
    print('\n' + ' '*13 + "1. 수입 입력하기")
    print('\n' + ' '*13 + "2. 지출 입력하기")
    print('\n' + ' '*8 + "3. 현재 저장된 내역 출력하기")
    print('\n' + ' '*8 + "4. 수익과 지출의 잔액 확인하기")
    print('\n' + ' '*15 + "5. 종료하기")
    print('    ╰──                             ──╯')

  
    choice = pf.input_intData("\n ☞ 원하시는 메뉴의 번호를 입력해주세요: ") 
    
   
   
    if choice is None  or choice not in range(1, 6):  
        print('\n▶ 잘못된 번호입니다. 목록 번호 중에서 선택해주세요.')
        
        continue
        
    
    # 1번: 수입 입력  
    if choice == 1 :
        print(f'{choice}. [{menu[1]}]를 선택하셨습니다.')
        
        amount1 = pf.input_intData('\n금액을 입력해 주세요: ') 
        
        if amount1 is None: 
            continue        # 유효하지 않은 금액이면 반복문 계속 => while True로 돌아간다
        
        
        profit_content =  pf.input_strData('기록할 내용을 적어주세요(예시: 월급): ') 
        if profit_content is None:
            continue
        
        print(f"\n[Income] {profit_content}: + {amount1}원 입력되었습니다.")
       

        user_ledger[profit_content] = amount1  
        
    
    elif choice == 2 : # 2번: 지출 입력
        print(f'{choice}. [{menu[2]}]를 선택하셨습니다.')
        amount2 = pf.input_intData('\n금액을 입력해 주세요: ')
        
        if amount2 is None: 
            continue        # 유효하지 않은 금액이면 반복문 계속 => while True로 돌아간다
        
        loss_content = pf.input_strData('기록할 내용을 적어주세요(예시: 식비): ')
        if loss_content is None:
            continue
        
        print(f"\n[Expenditure] {loss_content}: -{amount2}원 입력되었습니다.")
        
        user_ledger[loss_content] = -amount2  

    
    elif choice == 3 : # 3번: 내역 출력
        print(f'{choice}. [{menu[3]}]를 선택하셨습니다.')
        
        if not user_ledger:
            print('\n ▶ 현재 저장된 내역이 없습니다. 다시 메뉴로 돌아가서 기록 해주세요!')
            continue # 빈칸이면 False니까 다시 메뉴로 돌아가게 함s
        else:
            print("\n====== 현재 저장된 내역 ======")
            for key, value in user_ledger.items(): # 값이 있는 만큼 출력
                print(f'\n § {key}: {value:,}원')
            print("==============================")

                
    
    
    elif choice == 4 : # 4번: 잔액 확인
        print(f'{choice}. [{menu[4]}]를 선택하셨습니다.')
        if not user_ledger:
            print('\n ▶ 현재 저장된 내역이 없습니다. 다시 메뉴로 돌아가서 기록 해주세요!')
            continue
        else:
            balance = pf.balance_check(user_ledger) 
            print(balance, type(balance))
            continue
            
    
    
    elif choice == 5 : # 5번: 종료
        print(f'{choice}. [{menu[5]}]를 선택하셨습니다.')
        quit_ledger = input('\n정말로 종료 하시겠습니까? [y/n]: ').strip()
        if quit_ledger.lower() == 'y':
            print('\n ▷▶▷▶ 프로그램이 종료됩니다.. _( :⁍ 」 )_..')
            break
        elif quit_ledger.lower() == 'n':
            print('\n ▷▶▷▶ 처음 메뉴로 돌아갑니다.')
            continue
            
        
    
    
    

        
    
