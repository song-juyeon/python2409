class Date:
    _IMOJI = ('😰', '😥', '🤔', '☺', '🤩')

    def __init__(self, Title):
        #일기 제목
        self.Title = Title
        #일기를 쓴 날짜
        self.date = ''
        #일기를 쓴 날의 날씨
        self.weather = ''
        #일기 내용
        self.dairy = ''
        #일기를 쓰고 난 뒤 내 기분 (ex:최고로 좋다면 5를 입력, 많이 우울하다면 1을 입력)
        self.mood = 3

    def set_Title(self):
        print('··· 일기 작성 중 ···')
        Title = input('오늘 나의 하루의 제목을 적어주세요😎 >> ')
        self.Title = '떠오르지 않나요..?' if Title == '' else Title

    def set_date(self):
        date = input('오늘 날짜는? (ex 2021. 1. 1.) >> ')
        self.date = '알려주세요...' if date == '' else date

    def set_weather(self):
        weather = input('날씨도 이야기 해주세요! >> ')
        self.weather = '얘기해주셨으면 좋겠다...!!' if weather == '' else weather

    def set_dairy(self):
        dairy = input('오늘 나의 하루를 쭈루룩 적어내려가봐요 😊 >> ')
        self.dairy = '...숨 쉰 거라도 적어주세요 😢' if dairy == '' else dairy

    def set_mood(self):
        for index, mood in enumerate(Date._IMOJI):
            print(f'{index + 1} : {mood}')
        mood = input('마지막 질문!! 오늘의 기분은?!(ex:최고로 좋다면 5를 입력, 많이 우울하다면 1을 입력해주세요✨) >> ')
        if mood == '':
            self.mood = 0
        else:
            mood = int(mood)
            self.mood = mood - 1

    def __str__(self):
        return f'✨====🌹====💕내가 적은 나의 하루💕====🌹====✨\n\n제목 : [ {self.Title} ]\n그 날 날짜 [ {self.date} ]\n그 날 날씨 [ {self.weather} ]\n쭈루룩 적어본 하루 [ {self.dairy} ]' \
               f'\n그때 나의 기분 [ {Date._IMOJI[self.mood]} ]'

    def set_diary(self):
        f'{self.date} 때 일기'
        self.set_Title()
        self.set_date()
        self.set_weather()
        self.set_dairy()
        self.set_mood()