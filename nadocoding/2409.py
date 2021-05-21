# <숫자 자료형>
print(5)
print(-10)
print(3.14)
print(1000)
print(5+3)
print(2*8)
print(3*(3+1))

# <문자열 자료형>
print('풍선')
print("나비")
print("ㅋㅋㅋㅋㅋㅋㅋㅋㅋ")
print("ㅋ"*9)

# <boolean 자료형> -> 참/거짓을 의미
print(5 > 10)
print(5 < 10)
print(True)
print(False)
print(not True)
print(not False)
print(not (5 > 10))

# <변수>
# ex) 애완동물을 소개해 주세요
animal = "고양이"
name = "해피"
age = 4
hobby = "낮잠"
is_adult = age >= 3

# 정수형은 str로 감싸주어야 한다.
# ,로 연결시 str로 감싸지 않아도 되며, 띄어쓰기 한칸이 자동으로 된다.
print("우리집 " + animal + "의 이름은 " + name + "에요")
hobby = "산책"
print(name, "는 ", age, "살이며, ", hobby, "을 아주 좋아해요")
print(name + "는 어른일까요? " + str(is_adult))

'''작은 따움표
3개는 
줄 바꿈 주석 ㅎㅎ '''

# <퀴즈 1>
station = "사당"
print(station + "행 열차가 들어오고 있습니다.")
station = "신도림"
print(station + "행 열차가 들어오고 있습니다.")
station = "인천공항"
print(station + "행 열차가 들어오고 있습니다.")



# <연산자>
print(1+1)
print(3-2)
print(5*2)
print(6/3)

print(2**3) #2^3 = 8
print(5%3) # 나머지 구하기 = 2
print(10%1) # 나머지 구하기 = 1
print(5//3) # 몫 구하기 = 1
print(10//3) # 3

print(10 > 3) #True
print(4 >= 7) #False
print(10 < 3) #False
print(5 <= 5) #True

print(3 == 3) #True
print(4 == 2) #False
print(3 + 4 == 7) #True

print(1 != 3) #True
print(not(1 != 3)) #False

print((3 > 0) and (3 < 5)) #True
print((3 > 0) & (3 < 5)) #True

print((3 > 0) or (3 > 5)) #True
print((3 > 0) | (3 > 5)) #True

print(5 > 4 > 3) #True
print(5 > 4 > 7) #False


# <간단한 수식>
print(2 + 3 * 4) # 14
print((2 + 3) * 4) #20
number = 2 + 3 * 4 #14
print(number)
number = number + 2 #16
print(number)
number += 2 #18
print(number)
number *= 2 #36
print(number)
number /= 2 #18
print(number)
number -= 2 #16
print(number)
number %= 5 #1
print(number)


# <숫자 처리 함수>
print(abs(-5)) #절댓값 = 5
print(pow(4, 2)) #4^2 = 4*4 = 16
print(max(5, 12)) #최댓값 = 12
print(min(5, 12)) #최솟값 = 5
print(round(3.14)) #반올림 = 3
print(round(4.99)) #반올림 = 5

from math import *
print(floor(4.99)) #내림 = 4
print(ceil(3.14)) #올림 = 4
print(sqrt(16)) #제곱근구하기 = 4


# <램덤함수>
from random import *
print(random()) # 0.0 ~ 1.0 미만의 임의의 값 생성
print(random() * 10) # 0.0 ~ 10.0 미만의 임의의 값 생성
print(int(random() * 10)) # 0 ~ 10 미만의 임의의 값 생성
print(int(random() * 10) + 1) # 1 ~ 10 이하의 임의의 값 생성

print(int(random() * 45) + 1) # 1 ~ 45 이하의 임의의 값 생성
print(randrange(1, 46)) # 1 ~ 46 미만의 임의의 값 생성
print(randint(1, 45)) # 1 ~ 45이하의 임의의 값 생성

# <퀴즈2>
date = randint(4, 28) # 4 ~ 28 이하의 값을 임의의 생성
print("오프라인 스터디 모임 날짜는 매월 " + str(date) + "일로 선정되었습니다")


# <문자열>
sentence = '나는 소년입니다'
print(sentence)
sentence2 = "파이썬은 쉬워요"
print(sentence2)
sentence3 = """
나는 소년이고,
파이썬이 쉬워요
"""
print(sentence3)

# <슬라이싱>
jumin = "990120-1234567"
print("성별 : " + jumin[7])
print("연 : " + jumin[0:2]) #0 부터 2 직전까지
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])

print("생년월일 : " + jumin[:6]) #처음부터 6직전까지
print("뒤 7자리 : " +jumin[7:]) #7부터 끝까지
print("뒤 7자리 (뒤에부터) : " + jumin[-7:]) #맨 뒤에서 7번째부터 끝까지

# <문자열 처리 함수>
python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace("Python", "Java"))

index = python.index("n")
print(index)
index = python.index("n", index + 1)
print(index)

print(python.find("n"))
print(python.find("Java")) # 없는 값을 찾으라하면 -1이 나옴
# print(python.index("Java")) # 없는 값을 찾으라하면 에러남
print(python.count("n"))

# <문자열 포맷>
print("a" + "b")
print("a", "b")
# 방법 1
print("나는 %d살입니다." % 20) #정수값만 가능
print("나는 %s를 좋아해요." % "파이썬")
print("Apple은 %c로 시작해요." % "A")
print("나는 %s살입니다." % 20)
print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간"))
# 방법 2
print("나는 {}살입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨간"))
print("나는 {0}색과 {1}색을 좋아해요.".format("파란", "빨간"))
print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨간"))
# 방법 3
print("나는 {age}살이며, {color}색을 좋아해요".format(age = 20, color="빨간"))
print("나는 {age}살이며, {color}색을 좋아해요".format(color="빨간", age = 20))
# 방법 4 (v3.6 이상~)
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요")

# <탈출문자>
# \n : 줄 바꿈
print("백문이 불여일견 \n백견이 불여일타")
# \" \' : 문장 내에서 따옴표
print("너는 '나도코딩'입니다")
print('너는 "나도코딩"입니다')
print("너는 \"나도코딩\"입니다")
print("너는 \'나도코딩\'입니다")
# \\ : 문장 내에서 \
print("E:\python2409env\Scripts\python.exe")
# \r : 커서를 맨 앞으로 이동
print("Red Apple\rPine")
# \b : 백스페이스 (한 글자 삭제)
print("Redd\bApple")
# \t : 탭
print("Red\tApple")

# <퀴즈3>
# Quiz) 사이트별러 비밀번호를 만들어 주는 프로그램을 작성하시오
#
# 예) http://naver.com
# 규칙1 : http:// 부분은 제외 = > naver.com
# 규칙2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
# 규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!"로 구성
# 예) 생성된 비밀번호 : nav51!

url = "http://naver.com"
my_str = url.replace("http://", "") #규칙1
my_str = my_str[:my_str.index(".")] #규칙2, 처음부터 .전까지
password = my_str[0:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print("{0}의 비밀번호는 {1} 입니다.".format(url, password))

# <리스트>
#지하철 칸별로 10명, 20명, 30명
subway1 = 10
subway2 = 20
subway3 = 30
subway = [10, 20, 30]
print(subway)
subway = ["유재석", "조세호", "박명수"]
print(subway)
# 조세호씨가 몇 번째 칸에 타고 있는가?
print(subway.index("조세호"))
# 하하씨가 다음 정류장에서 다음 칸에 탐
subway.append("하하")
print(subway)
# 정형돈씨가 유재석 / 조세호 사이에 탐
subway.insert(1, "정형돈")
print(subway)
# 지하철에 있는 사람을 한 명 씩 뒤에서 꺼냄
print(subway.pop())
print(subway)
print(subway.pop())
print(subway)
# 같은 이름의 사람이 몇 명 있는지 확인
subway.append("유재석") #유재석 추가
print(subway)
print(subway.count("유재석"))
# 정렬도 가능
num_list = [5, 2, 4, 3, 1]
num_list.sort()
print(num_list)
#순서 뒤집기
num_list.reverse()
print(num_list)
#모든 값 지우기
#num_list.clear()
print(num_list)
# 다양한 자료형 함께 사용 가능
mix_list = ["조세호", 20, True]
print(mix_list)
# 리스트 확장
num_list.extend(mix_list)
print(num_list)

# <사전>
cabinet = {3:"유재석", 100:"김태호"}
print(cabinet[3])
print(cabinet[100])
print(cabinet.get(3))
print(cabinet.get(5))
print(cabinet.get(5, "사용 가능"))
print(3 in cabinet)
print(5 in cabinet)

cabinet = {"A-3":"유재석", "B-100":"김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])
# 새 손님
print(cabinet)
cabinet["A-3"] = "김종국"
cabinet["C-20"] = "조세호"
print(cabinet)
# 간 손님
del cabinet["A-3"]
print(cabinet)
# key들만 출력
print(cabinet.keys())
# value들만 출력
print(cabinet.values())
# e둘다 출력
print(cabinet.items())
# 목욕탕 영업 종료
cabinet.clear()
print(cabinet)

# <튜플> - 변경되지 않는 목록을 이용할 때 사용
menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])
# menu.add("생선까스") 제공x 실행시 오류발생

name = "김종국"
age = 20
hobby = "코딩"
print(name, age, hobby)
# 간단하게 코드 변경
(name2, age2, hobby2) = ("유재석", 23, "독서")
print(name2, age2, hobby2)

# <세트(set)>
# 중복 안됨, 순서 없음
my_set = {1,2,3,3,3} #중복이라 나머지 3이 무시됨
print(my_set)
java = { "유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])
#교집합 (즉, java와 python을 모두 할 수 있는 개발자)
print(java & python)
print(java.intersection(python))
# 합집합
print(java | python)
print(java.union(python))
# 차집합 (java는 할 수 있지만 python은 할 줄 모르는 개발자)
print(java - python)
print(java.difference(python))
# python을 할 줄 아는 사람이 늘어남
python.add("김태호")
print(python)
# java를 잊다
java.remove("김태호")
print(java)

# <자료구조의 변경>
menu = {"커피" , "우유", "주스"}
print(menu, type(menu)) #중괄호
menu = list(menu)
print(menu, type(menu)) #대괄호
menu = tuple(menu)
print(menu, type(menu)) #소괄호
menu = set(menu)
print(menu, type(menu))

# # <퀴즈4>
# Quiz) 당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
# 참석률을 높이기 위해 댓글 이벤트를 진행하기로  하였습니다.
# 댓글 작성자들 중애 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.
#
# 조건1 : 편의상 댓글은 20명이 작성하였고 아이디는 1~20이라고 가정
# 조건2 : 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가
# 조건3 : ramdom 모듈의 shuffle과 sample를 활용
#
# (출력 예제)
# -- 당첨자 발표 --
# 치킨 당첨자 : 1
# 커피 당첨자 : [2, 3, 4]
# --축하합니다--
# (활용 예제)
# from random import *
# lst = [1,2,3,4,5]
# print(lst)
# shuffle(lst)
# print(lst)
# print(sample(lst, 1))

from random import *
users = range(1, 21) #[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# print(type(users))
users = list(users)
# print(type(users))
print(users)
shuffle(users)
print(users)
winners = sample(users, 4) #4명 중에서 1명은 치킨, 3명은 커피

print(" -- 당첨자 발표 -- ")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))
print(" -- 축하합니다 --")


# <if>
weather = "미세먼지"    #input("오늘 날씨는 어때요? ")
if weather == "비" or weather == "눈":
    print("우산을 챙기세요")
elif weather == "미세먼지":
    print("마스크를 챙기세요")
else:
    print("준비물이 없습니다.")

temp = 5    #int(input("기운이 어때요? "))
if 30 <= temp:
    print("너무 더워요. 나가지 마세요")
elif 10 <= temp and temp <= 301:
    print("괜찮은 날씨에요")
elif 0 <= temp < 10:
    print("외투를 챙기세요")
else:
    print("너무 추워요 나가지 마세요")

# <for>
# print("대기번호 : 1")
# print("대기번호 : 2")
# print("대기번호 : 3")
# print("대기번호 : 4")
for waiting_no in range(1, 6): # 1,2,3,4,5
    print("대기번호 : {0}".format(waiting_no))
starbucks = ["아이어맨", "토르", "아이엠 크루트"]
for customer in starbucks:
    print("{0}님, 커피가 준비되었습니다.".format(customer))

# <while>
customer2 = "토르"
index = 5
while index >= 1:
    print("{0}님, 커피가 준비 되었습니다. {1}번 남았습니다.".format(customer2, index))
    index -= 1
    if index == 0:
        print("커피가 폐기처분되었습니다.")

# customer3 = "아이언맨"
# index = 1
# while True:
#     print("{0}님, 커피가 준비 되었습니다. {1}회.".format(customer3, index))
#     index += 1  #무한루프, ctrl + c를 누르면 종료됨

# customer4 = "캡틴"
# person = "Unkown"
# while person != customer4 :
#     print("{0}님, 커피가 준비 되었습니다.".format(customer4))
#     person = input("이름이 어떻게 되나요? ")    #customer4와 같은 답이 나올때 for문 종료

# <continue와 break>
absent = [2, 5] #결석
no_book = [7] #책 x
for student in range(1, 11):
    if student in absent:
        continue # if문이 성립하지 않는 것을 건너뜀
    elif student in no_book:
        print("오늘 수업은 여기까지. {0}번은 교무실로 따라와".format(student))
        break # if문에 성립하지 않아 바로 if문을 종료
    print("{0}번, 책을 읽어봐".format(student))

# <한 줄 for문>
students = [1,2,3,4,5]
print(students)
students = [1+100 for i in students]
print(students)
# 학생이름을 길이로 변환
students = ["Iron man", "I am groot"]
students = [len(i) for i in students]
print(students)
# 학생이름을 대문자로 변환
students = ["Iron man", "Thor", "I am groot"]
students = [i.upper() for i in students]
print(students)

# <퀴즈 5>
# Quiz) 당신은 Cocoa 서비스를 이용하는 택시 기사님입니다.
# 50명의 승객과 매칭 기회가 있을 때, 총 탑승객 수를 구하는 프로그램을 작성하시오.
#
# 조건1 : 승객별 운행 소요 시간을 5분 ~ 50분 사이의 난수로 정해집니다.
# 조건2 : 당신의 소요 시간 5분 ~ 15분 사이의 승객만 매칭해야 합니다.
from random import *
cnt = 0 # 총 탑승객 수
for i in range(1, 51): # 1~50(승객 수)
    time = randrange(5, 51) # 5~50(소요시간)
    if 5 <= time <= 15: # 매칭 성공
        print("[O] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
        cnt += 1
    else: # 매칭 실패
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
print("총 탑승 승객 : {0}분".format(cnt))

# <함수>
def open_account():
    print("새로운 계좌가 생성되었습니다.")
open_account()

# <전달값과 반환값>
def deposit(balance, money): #입금
    print("입금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance + money))
    return balance + money
def withdraw(balance, money): #출금
    if balance >= money:
        print("출금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance - money))
        return balance - money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0}원입니다.".format(balance))
def withdraw_night(balance, money):
    commission = 100 # 수수료
    return commission, balance - money - commission
balance = 0
balance = deposit(balance, 1000)
# balance = withdraw(balance, 2000)
commissiom, balance = withdraw_night(balance, 500)
print("수수료는 {0}원이며, 잔액은 {1}원입니다.".format(commissiom, balance))

# <기본값>
# def profile(name, age, main_lang):
#     print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}".format(name, age, main_lang))
# profile("유재석", 20, "파이썬")
# profile("김태호", 25, "자바")
# 같은 학교 같은 학년 같은 반 같은 수업 일시
def profile(name, age = 18, main_lang = "파이썬"):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}".format(name, age, main_lang))
profile("유재석")
profile("김태호")

# <키워드값>
def profile2(name, age, main_lang):
    print(name, age, main_lang)
profile(name="유재석", main_lang="파이썬", age=20)    #순서가 뒤섞여있어도 함수안에 순서로 정리되어 출력됨됨
profile(main_lang="자바", age=24, name="김태호")

# <가변 인자>
# def profile3(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
#     print(lang1, lang2, lang3, lang4, lang5)
def profile3(name, age, *language):
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
    for lang in language:
        print(lang, end=" ")
    print()

print("유재석", 20, "Python", "Java", "C", "C++", "C#", "JavaScript")
print("유재석", 25, "Kolin", "Swift", "", "", "")


# <지역 변수와 전역 변수>
gun = 10

def checkpoint(soldiers):
    global gun #전역 공간에 있는 gun을 이용
    # gun = 20 #지역변수
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
def checkpoint_ref(gun, soldiers):
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun

print("전체 총 : {0}".format(gun)) #전역 변수 출력
# checkpoint(2)
gun = checkpoint_ref(10, 3)
print("남은 총 : {0}".format(gun)) #함수 내에서 이용(global로)한 후 전역변수 출력

# <퀴즈 6>
# Quiz) 표준 체중을 구하는 프로그램을 작성하시오
# * 표준 체중 : 각 개인의 키에 적당한 표준
#
# (성별애 따른 공식)
# 남자 : 키(m) x 키(m) x 22
# 여자 : 키(m) x 키(m) x 21
#
# 조건1 : 표준 체중은 별도의 함수 내에서 계산
#         * 함수명 : std_weight
#         * 전달값 : 키(height), 성별(gender)
# 조건2 : 표준 체중은 소수점 둘째자리꺼자 표시
#
# (출력 예제)
# 키 175cm 남자의 표준 체중은 67.38kg 입니다.
def std_weight(height, gender):  #키 m 단위 (실수), 성별 "남자"/"여자"
    if gender == "남자":
        return height * height * 22
    else:
        return height * height * 21
height = 162
gender = "여자"
weight = round(std_weight(height / 100, gender), 2)
print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))

print("___________________________________________________")

# <클래스> <__init__> <멤버 변수>
# # 마린: 공격 유닛, 군인. 총을 쏠 수 있음
# name = "마린"
# hp = 40
# damage = 5
# print("{} 유닛이 생성되었습니다.".format(name))
# print("체력 {0}, 공격력 {1}\n".format(hp, damage))
#
# # 탱크 : 공격 유닛, 탱크. 포를 쏠 수 있는데, 일반모드 / 시즈모드
# tank_name = "탱크"
# tank_hp = 150
# tank_damage = 35
# print("{} 유닛이 생성되었습니다.".format(tank_name))
# print("체력 {0}, 공격력 {1}\n".format(tank_hp, tank_damage))
#
# tank2_name = "탱크"
# tank2_hp = 150
# tank2_damage = 35
# print("{} 유닛이 생성되었습니다.".format(tank_name))
# print("체력 {0}, 공격력 {1}\n".format(tank_hp, tank_damage))
#
# def attack(name, location, damage):
#     print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format(name, location, damage))
#
# attack(name, "1시", damage)
# attack(tank_name, "1시", tank_damage)
# attack(tank2_name, "1시", tank2_damage)
#------------------클래스 이용---------------------
# class Unit:
#     def __init__(self, name, hp, damage):   #__init__ : 생성자 / 객체: 마린이나 탱크와 같이 어떤 클래스로부터 만들어지는 녀석들
#         self.name = name            #.name = 멤버 변수
#         self.hp = hp                #.hp = 멤버 변수
#         self.damage = damage        #.damage = 멤버 변수
#         print("{0} 유닛이 생성되었습니다.".format(self.name))
#         print("체력 {0}, 공격력 {1}\n".format(self.hp, self.damage))
#
# marine1 = Unit("마린", 40, 5)     #marine1, marine2, tank는 인스턴스이다.
# marine2 = Unit("마린", 40, 5)
# tank = Unit("탱크", 150, 35)
# # marine3 = Unit("마린")        #사용 불가
# # marine3 = Unit("마린", 40)    #사용 불가
#
# # 레이스 : 공중 유닛, 비행기. 클로킹 (상대방에게 보이지 않음)
# wraith1 = Unit("레이스", 80, 5)
# print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))
#
# # 마인드 컨트롤 : 상대방 유닛을 내것으로 만드는 것 (빼앗음)
# wraith2 = Unit("레이스", 80, 5)
# wraith2.clocking = True
#
# if wraith2.clocking == True:
#     print("{0}는 현재 클로킹 상태입니다.".format(wraith2.name))
# # if wraith1.clocking == True:
# #     print("{0}는 현재 클로킹 상태입니다.".format(wraith2.name))
# # <wraith1은 클로킹 할 것이 없기 때문에 오류가 난다.>

# <메서드>
# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed):   #__init__ : 생성자 / 객체: 마린이나 탱크와 같이 어떤 클래스로부터 만들어지는 녀석들
        self.name = name            #.name = 멤버 변수
        self.hp = hp                #.hp = 멤버 변수
        self.speed = speed
        print("{0} 유닛이 생성되었습니다.".format(name))

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

# 공격 유닛
class AttackUnit(Unit):     #상속
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(self.name, location, self.damage))

# 마린
class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "마린", 40, 1, 5)

    #스팀팩 : 일정 시간 동안 이동 및 공격 속도를 증가, 체력 10 감소
    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print("{0} : 스팀팩을 사용합니다. (HP 10 감소)".format(self.name))
        else:
            print("{0} : 체력이 부족하여 스팀팩을 사용하지 않습니다.".format(self.name))

# 탱크
class Tank(AttackUnit):
    # 시즈모드 : 탱크를 지상에 고정시켜, 더 높은 파워로 공격 가능. 이동 불가.
    seize_developed = False  # 시즈모드 개발여부

    def __init__(self):
        AttackUnit.__init__(self, "탱크", 150, 1, 35)
        self.seize_mode = False

    def set_seize_mode(self):
        if Tank.seize_developed == False:
            return
        # 현재 시즈모드가 아닐 때 -> 시즈모드 실행
        if self.seize_mode == False:
            print("{0} : 시즈모드로 전환합니다.".format(self.name))
            self.damage *= 2
            self.seize_mode = True
        # 현재 시즈모드일 때 -> 시즈모드 해제
        else:
            print("{0} : 시즈모드를 해제합니다.".format(self.name))
            self.damage /= 2
            self.seize_mode = False


# 날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))

# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable):       #다중상속 가능
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)  #지상 스피드는 0
        Flyable.__init__(self, flying_speed)

    def move(self, location):       #오버라이딩
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

# 레이스
class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5)
        self.clocked = False #클로킹 모드 (해제 상태)

    def clocking(self):
        if self.clocked == True: # 클로킹 모드 -> 모드 해제
            print("{0} : 클로킹 모드를 해제합니다.".format(self.name))
            self.clocked = False
        else: # 클로킹 모드 해제 -> 모드 실행
            print("{0} : 클로킹 모드를 실행합니다.".format(self.name))
            self.clocked = True

def game_start():
    print("[알림] 새로운 게임을 시작합니다")

def game_over():
    print("Player : gg")    # goog game
    print("[Player] 님이 게임에서 퇴장하셨습니다.")

# 실제 게임 진행
game_start()

# 마린 3기 생성
m1 = Marine()
m2 = Marine()
m3 = Marine()

# 탱크 2기 생성
t1 = Tank()
t2 = Tank()

# 레이스 1기 생성
w1 = Wraith()

# 유닛 일괄 관리
attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

# 전군 이동
for unit in attack_units:
    unit.move("1시")

# 탱크 시즈모드 실행
Tank.seize_developed = True
print("[알림] 탱크 시즈모드가 실행이 완료되었습니다.")

# 공격 모드 준비 (마린 : 스팀팩, )
for unit in attack_units:
    if isinstance(unit, Marine):
        unit.stimpack()
    elif isinstance(unit, Tank):
        unit.set_seize_mode()
    elif isinstance(unit, Wraith):
        unit.clocking()

# 전군 공격
for unit in attack_units:
    unit.attack("1시")

# 전군 피해
for unit in attack_units:
    unit.damaged(randint(5, 21))     #공격은 랜덤으로 받음(5~20)

# 게임 종료
game_over()

# # 건물
# class BuildingUnit(Unit):
#     def __init__(self, name, hp, location):
#         super().__init__(name, hp, 0)       #Unit.__init__(self, name, hp, 0)과 같음
#         self.location = location

# <super>
# class Unit:
#     def __init__(self):
#         print("Unit 생성자")
# class Flyable:
#     def __init__(self):
#         print("Flyable 생성자")
# class FlyableUnit(Unit, Flyable):
#     def __init__(self):
#         #super().__init__()      #super로 생성자를 호출하면 상속 받은 것 중 마지막 생성자만이 호출된다.
#         Unit.__init__(self)      #두개다 각자 초기화를 해서 하면은 둘다 생성자가 호출됨
#         Flyable.__init__(self)

# # 서플라이 디폿 : 건물, 1개 건물 = 8 유닛.
# supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")
#
# def game_start():
#     print("[알림] 새로운 게임을 시작합니다.")
# def game_over():
#     pass       #아무 것도 안하고 넘어가는 것(완성된것처럼)
# game_start()
# game_over()

# # 벌쳐 : 지상 유닛, 기동성이 좋음
# vulture = AttackUnit("벌쳐", 80, 10, 20)
#
# # 벌쳐 : 지상 유닛, 기동성이 좋음
# battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)
#
# vulture.move("11시")
# # battlecruiser.fly(battlecruiser.name, "9시")
# battlecruiser.move("9시")

# # 발키리 : 공중 공격 유닛, 한번에 14발 미사일 발사.
# valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
# valkyrie.fly(valkyrie.name,"3시")

# #파이어뱃 : 공격 유닛, 화염방사기.
# firebat1 = AttackUnit("파이어뱃", 50, 16)
# firebat1.attack("5시")
# # 공격 2번 받음
# firebat1.damaged(25)
# firebat1.damaged(25)

# <퀴즈 8>
# 주어진 코드를 활용하여 부동산 프로그램을 작성하시오.
#
# (출력 예제)
# 총 3대의 매물이 있습니다.
# 강남 아파트 매매 10억 2010년
# 마포 오피스텔 5억 2007년
# 송파 빌라 월세 500/50 2000년
class House:
    # 매물 초기화
    def __init__(self, location, house_type, deal_type, price, comletion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.comletion_year = comletion_year

    # 매물 정보 표시
    def show_detail(self):
        print(self.location, self.house_type, self.deal_type, self.price, self.comletion_year)

houses = []
house1 = House("강남", "아파트", "매매", "10억", "2010년")
house2 = House("마포", "오피스텔", "전세", "5억", "2007년")
house3 = House("송파", "빌라", "월세", "500/50", "2000년")

houses.append(house1)
houses.append(house2)
houses.append(house3)

print("총 {0}대의 매물이 있습니다.".format(len(houses)))
for house in houses:
    house.show_detail()

def solution(characters):
   result = ""
   result += characters[0]
   for i in range(1 ,len(characters)):
       if characters[i - 1] != characters[i]:
           result += characters[i]
   return result

#The following is code to output testcase. The code below is correct and you shall correct solution function.
characters = "senteeeencccccceeee"
ret = solution(characters)

#Press Run button to receive output.
print("Solution: return value of the function is", ret, ".")