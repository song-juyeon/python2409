from worklist import Worklist
from work import Workmenu
from Diary_main import Diarymenu

work_list = Worklist()
work_menu = Workmenu(work_list)
diary_menu = Diarymenu()

def print_main():
    # 맨 위는 해야 할 일 띄워줌

    # 할 일 메뉴
    print('1. 해야 할 일')
        # 할 일 체크
        # 할 일 추가
        # 할 일 삭제
        # 뒤로가기
    # 일기
    print('2. 일기')
        # 일기 띄워주기
        # 일기 작성
        # 일기 삭제
        # 뒤로가기
        # 종료
    print('3. 종료하기')

    num = input('메뉴를 선택해주세요 : ')
    return num

def main():
    work_list.write_work()
    while True:
        print(work_list.__str__())
        num = print_main()
        if num == '1':
            work_menu.workmenu()
            # 할일
            # 할 일 체크 0
            # 할 일 추가 0
            # 할 일 삭제 0
            # 뒤로가기 0
            pass
        elif num == '2':
            # 일기
            diary_menu.diarymenu()

        elif num == '3':
            break
        else:
            print('다시 입력하세요: ')

if __name__ == '__main__':
    main()