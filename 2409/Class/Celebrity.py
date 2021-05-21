class Celebrity:
    def __init__(self, name):
        # 이름
        self.name = name

    def set_name(self, name):
        self.name = name

    def set_entertainment(self, entertainment):
        self.entertainment = entertainment

    # def info(self):
    #     print(f'이름: {self.name}\t소속사: {self.entertainment}')

    def __str__(self):
        return f'이름: {self.name}\t소속사: {self.entertainment}'

class Talent(Celebrity):
    def __init__(self, name):
        super().__init__(name)      #Celebrity 클래스(부모클래스)의 생성자 호출

    def set_drama(self, drama):
        self.drama = drama

    def __str__(self):
        return  super().__str__() + f'\t드라마: {self.drama}'
#        return f'이름: {self.name}\t소속사: {self.entertainment}\t 드라마: {self.drama}'

class Singer(Celebrity):
    def __init__(self, name, song):
        super().__init__(name)
        self.song = song

    def __str__(self):
        return super().__str__() + f'\t노래: {self.song}'

IU = Celebrity('이지은')
#IU.set_name('이지은')
IU.set_entertainment('이담')
# IU.info()
print(IU.name, IU.entertainment)
print(IU)       #클래스의 __str__() 호출됨

이광수 = Celebrity('이광수')
#이광수.set_name('이광수')
이광수.set_entertainment('킹콩')
# 이광수.info()

이광수 = Talent('이광수')
이광수.set_entertainment('킹콩')
이광수.set_drama('라이브')
print(이광수)

현진 = Singer('현진', '神메뉴')
현진.set_entertainment('JYP')
print(현진)
필립스 = Singer('필립스', 'Back Door')
필립스.set_entertainment('JYP')
print(필립스)

스트레이키즈 = []
스트레이키즈.append(현진)
스트레이키즈.append(필립스)
print(스트레이키즈)
for i in 스트레이키즈:
    print(i)
# fot i in range(len(스트레이키즈)):
#     print(스트레이키즈[i])

