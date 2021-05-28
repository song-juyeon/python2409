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

    # 레시피 북에서 레시피 찾기
    def search_recipe(self):
        searched_recipe = []
        # 찾을 레시피이름을 검색한다. (입력받기)
        name = input('>> 원하는 레시피를 검색하세요: ')
        # 레시피 리스트에서 찾는 이름이 있는지 찾아본다(중복 확인, for문)
        for recipe in self.recipe_list:
            if name == recipe.name:
                # 중복되는 레시피가 있으면 보여준다.
                print(recipe)
                searched_recipe.append(recipe)
        # 중복되는 레시피가 없으면 없다고 알려준다. (searched_recipe가 비어있는 상황)
        if len(searched_recipe) == 0:
            # 레시피를 추가할지 물어본다
            answer = input('>> 찾는 레시피가 존재하지 않습니다. \n 추가하시겠습니까? (1: 예, 2: 아니요)')
            # 추가한다고 하면 레시피 추가
            if answer == '1':
                self.add_recipe()
            else:
                return

    # 재료로 레시피 찾기
    def search_ingredient(self):
        # 빈 셋(set) 생성 -> (재료의 중복제거)
        all_ingredient = set()
        # 레시피북에 있는 레시피의 재료들 셋에 넣기
        for recipe in self.recipe_list:
            for ingredient in recipe.ingredient:
                all_ingredient.add(ingredient)

        # 모든 재료를 보여주자
            for index, ingredient in enumerate(all_ingredient):
                print(f'{index + 1}. {ingredient}')



        # 찾을 재료의 이름을 검색
        search_num = int(input('>> 사용할 재료를 입력하세요 : '))
        search_ingredient = list(all_ingredient)[search_num - 1]

        # 레시피 리스트의 레시피 -> 레시피의 재료를 살펴보자
        for recipe in self.recipe_list:
            # 입력한 재료가 포함되면
            if search_ingredient in recipe.ingredient:
                # 해당 레시피를 모두 보여주자.
                print(recipe)

    def __str__(self):
        pass

