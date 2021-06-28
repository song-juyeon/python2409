class Recipe:

    def __init__(self, name):
        # 재료
        self.ingredient = {}    # 빈 딕셔너리 생성
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
        self.contents = '입력된 정보가 없습니다' if contents == '' else contents

    def set_people(self):
        people = input('몇 인분인가요? ')
        self.people = 1 if people == '' else people

    def set_video(self):
        video = input('레시피 영상 링크를 입력하세요: ')
        self.video = '입력된 정보가 없습니다.' if video == '' else video

    def set_ingredient(self):
        while True:
            ingredient = input("재료를 입력하세요(입력예시: '감자 100')\n 재료입력 완료시 enter: ")
            if ingredient == '':
                break
            ingredient_name, ingredient_gram = ingredient.split()
            # '감자 200'.split() -> '감자', '200' (key)-(value)
            self.ingredient[ingredient_name] = ingredient_gram
            #{'감자':'200'}

    def __str__(self):
        return f'레시피: {self.name}\n재료: {self.ingredient}\n양: {self.people}인분\n정보: {self.contents}\n참고영상링크: {self.video}'

    def set_recipe(self):
        self.set_people()
        self.set_ingredient()
        self.set_contents()
        self.set_video()
    
# 카레 = Recipe('카레')
# 카레.set_recipe()
# print(카레)