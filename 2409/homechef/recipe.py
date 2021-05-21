class Recipe:

    def __init__(self, name):
        # 재료
        self.ingredient = []
        # 내용
        self.contents = ''
        # 이름
        self.name = name
        # 인분
        self.people = 1
        # 영상링크
        self.video = ''

    def set_contents(self):
        contents = input('레시피 내용을 입력하세요: ')
        self.contents = '입력된 정보보이 없습니다' if contents == '' else contents

    def set_people(self):
        people = input('몇 인분인가요? ')
        self.people = 1 if people == '' else people

    def set_video(self):
        video = input('레시피 영상 링크를 입력하세요: ')
        self.video = '입력된 정보가 없습니다.' if video == '' else video

    def __str__(self):
        pass