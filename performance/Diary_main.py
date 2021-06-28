from Diary_date import contents

class Diarymenu:
    def print_menu(self):
        print('1. 일기 작성')
        print('2. 일기 수정')
        print('3. 일기 삭제')
        print('4. 이때까지 작성한 일기 확인')
        print('5. 뒤로가기')
        num = input('메뉴를 선택해주세용 >> ')
        return num

    def diarymenu(self):
        diary = contents()

        while True:
            num = self.print_menu()
            if num == '1':
                # 일기 작성
                diary.write_diary()
            elif num == '2':
                # 일기 수정
                diary.modify_diary()
            elif num == '3':
                # 일기 삭제
                diary.delete_diary()
            elif num == '4':
                # 작성한 일기 확인
                diary.show_diary()
            elif num == '5':
                # 종료하기
                break
            else:
                print('\n 잘못 선택하셨어요, 다시 입력해주세요!\n')

    if __name__ == '__main__':
        diarymenu()