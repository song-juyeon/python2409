#math
import math
print(math.ceil(3.5))           # 4         ceil:올림
print(math.floor(3.5))          # 3         floor:내림
print(math.pow(2, 10))          # 1024.0    pow:제곱
print(math.sin(math.pi/2))      # 1.0
# print(math.sin(math.pi/2))

print(round(3.5))               # 4         round:반올림

print('-'*30)

#random
import random
print(random.random())                          # 0.0 <= r < 1.0
print(random.randrange(1, 10))                  # 1 <= r < 10
print(random.randint(1, 10))                    # 1 <= r <= 10
list1 = ['굶었음', '피자', '김치찜', '닭가슴살']
print(random.choice(list1))                     # list1 중 하나
print(list1)
random.shuffle(list1)                    # list1 섞기
print(list1)
print(random.sample(list1, 2))                  # list1에서 n개 뽑기

print('-'*30)

#datetime
import datetime
now = datetime.datetime.now()
print(now)
print(now.day)
print(now.hour)
birthday = datetime.datetime(2004, 9, 16)
print(birthday)
print(now - birthday)

print('-'*30)

# <연습 문제>
# 핸드폰 요금이 62421원 나왔다. 100원 미만은 절사한다고 한다. 62400원 청구. 59827원일 경우, 실제 청구 금액은?0
fee = 59827
result_fee = fee//100*100
# result_fee = fee - fee%100
# result_fee = math.floor(fee/100)*100
# result_fee = int(fee/100)*100
print(result_fee)

# 평가계획은 100점 만점에 10점 단위로 점수를 줄 수 있다. 채점한 결과 93점이 나왔다. 90점 부여. 56점은 몇 점 부여?
score = 56
print(round(score/10)*10)
print(round(score, -1))

# 로또 복권 자동 생성기를 만든다면?
# (로또복권: 1~45 사이의 번호 중 랜덤으로 6개 뽑기)
lotto = list(range(1, 46))
result_lotto = random.sample(lotto, 6)
print(result_lotto)

# 1~9 숫자로 중복되지 않은 숫자 세자리를 뽑는 방법은?(185:O, 212:X)
nums = list(range(1, 10))  # num = [1,2,3,4,5,6,7,8,9]
number = random.sample(nums, 3)
print(number[0]*100 + number[1]*10 + number[2] )

# print("".join(str(n) for n in number))

# 내가 태어난 날로부터 며칠이 지났는지?
now = datetime.datetime.now()
birthday = datetime.datetime(2004, 9, 16)
result = now - birthday
print(result.days,'일 지남')

# 올해 크리스마스까지 며칠이 남았는지?
christmas = datetime.datetime(2021, 12, 25)
result = christmas - now
print(result.days,'일 후 성탄절')

# 내 생일이 며칠 남았는지?
thsiyear_birthday = datetime.datetime(2021, 9, 16)
result = thsiyear_birthday - now
print(result.days,'일 후 생일')

# 랜덤하게 번호로 자리를 배치하는 방법은?
# 제적(전출, 자퇴) 인원이 있다면?2
# 마지막번호, 1~마지막번호 리스트생성/ 제적번호 제거(반복될수 있음)/ 섞기, 출력
last_number = input("마지막 번호 : ")            #'9'
list_class = list(range(1, int(last_number) + 1))

while True:
    exclude_number = input("제외 할 번호(enter시 종료) : ")
    if exclude_number == '':
        break
    list_class.remove(int(exclude_number))

random.shuffle(list_class)

print('자리\t학생번호')
for i, number in enumerate(list_class):
    print(f'{i+1}\t{number}')
