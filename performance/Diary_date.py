from diary import Date

class contents:

    def __init__(self):
        self.diary_list = []

    def write_diary(self):
        title = input("제목을 입력해주세요 >> ")
        #다이어리 객체 만들기
        new_diary = Date(title)
        #다이어리 속성 설정하기
        new_diary.set_diary()
        #다이어리 self.diary_list에 어펜드하기
        self.diary_list.append(new_diary)

    def modify_diary(self):
        for index, diary in enumerate(self.diary_list):
            print(f'{index + 1}.\n {diary}')
        deletion = input("수정할 일기에 번호를 입력하세요 : ")
        del self.diary_list[int(deletion) - 1]
        self.write_diary()

    def delete_diary(self):
        for index, diary in enumerate(self.diary_list):
            print(f'{index + 1}.\n {diary}')
        deletion = input("삭제할 일기에 번호를 입력하세요 : ")
        del self.diary_list[int(deletion) - 1]
        print("===============================")

    def show_diary(self):
        for index, diary in enumerate(self.diary_list):
            print(f'{index + 1}.')
            print(diary)
            print("===============================")

    def __str__(self):
        pass