from recipe import Recipe

class RecipeBook:
    def __init__(self):
        self.recipe_list = []

    def add_recipe(self):
        # 추가할 레시피 이름 입력받기
        name = input('>> 레시피 이름을 입력하세요: ')
        # 같은 이름의 레시피가 있는지 중복 체크
        for recipe in self.recipe_list:     #레시피리슽안에 있는 레시피를 하나씩 비교한다
        # 중복되는 레시피가 있으면
            if name == recipe.name:
                #중복된다고 알림
                print('이미 존재하는 레시피입니다.')
                return
        # 중복되는 레시피가 없으면
        # 레시피 생성
        new_recipe = Recipe(name)
        new_recipe.set_recipe()
        # 레시피리스트에 레시피 추가
        self.recipe_list.append(new_recipe)

    def show_recipe(self):
        for index, recipe in enumerate(self.recipe_list):
            print(f'{index + 1} ')
            print(recipe)

    def __str__(self):
        pass




















