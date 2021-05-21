# 레시피 검색하기, 레시피 보여주기,
def print_menu():
    print('1. 레시피 검색하기')
    print('2. 레시피 추가하기')
    print('3. 재료로 검색하기')
    print('4. 전체 레시피 보여주기')
    print('5. 종료하기')
    num = input('메뉴를 선택하세요: ')
    return num


def main():
    num = print_menu()
    while True:
        if num == '1':
            # 레시피 검색하기
            return
        elif num == '2':
            # 레시피 추가하기
            return
        elif num == '3':
            # 재료로 검색하기
            return
        elif num == '4':
            # 전체 레시피 보여주기
            return
        elif num == '5':
            break
        else:
            print('다시 입력하세요: ')

