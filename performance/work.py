from worklist import Worklist


class Workmenu:
    def __init__(self, worklist):
        self.work_list = worklist

    def show_workmenu(self):
        # 맨 위는 해야 할 일 띄워줌
        print()
        # 할 일 메뉴
        print('1. 완료한 일 체크')

        print('2. 할 일 추가')

        print('3. 할 일 삭제')

        print('4. 뒤로가기')

        num2 = input('메뉴를 선택해주세요 : ')
        return num2

    def workmenu(self):
        while True:
            num2 = self.show_workmenu()
            if num2 == '1':
                print(self.work_list.check_work())
            elif num2 == '2':
                # 할일추가
                print(self.work_list.add_work())
            elif num2 == '3':
                # 할일삭제
                print(self.work_list.del_work())
            elif num2 == '4':
                break
            else:
                print('알맞지 않은 입력입니다.')

# s = Workmenu()
# s.workmenu()
# print(s)