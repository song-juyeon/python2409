# 1-1.주민등록번호 앞 6자리를 변수 id_number에 넣고,
# 출생년도 끝 두자리\n출생 월일\n그 두개의 합 출력
# 예시
# id_number = 020316 일 때
#
# 출력 예시
# 02
# 0316
# 732
import math

id_number = "040916"
print(id_number[0:2])
print(id_number[2:])
print(int(id_number[0:2]) + int(id_number[2:]))


# 1-2. 집 전화번호를 phone_number에 넣고,
# 지역번호\n맨 끝 네 자리 출력하기(지역번호의 자리수와 상관없이 동작하도록 하자)
# 예시
# phone_number = 02-1234-5678 또는 032-9876-4321
#
# 출력 예시
# 02 또는 032
# 5678 또는 4321

phone_number = "033-1374-2556"
print(phone_number[0:3])
print(phone_number[-4:])


# Quiz2-1. 학번을 student_number 변수에 넣고, 학급을 출력하고, 학과를 출력하기
# 반이 0 미만이거나 7 이상이면 "잘못 입력했습니다." 출력하기
# student_number = '2100' 또는 student_number = '2000'
# <출력 예시>
# 1반 뉴미디어소프트웨어과 또는 잘못 입력했습니다.
student_number = '2409'
ban = int(student_number[1])
if ban == 1 or ban == 2:
    print(str(ban) + "반 소프트웨어과")
elif 3 <= ban <= 4:
    print(str(ban) + "반 웹솔루션과")
elif ban == 5 and ban == 6:
    print(str(ban) + "반 디자인과")
else:
    print("잘못 입력했습니다.")


# Quiz2-2. 학번을 함수의 인수(argument)로 전달하여 호출하면 학년과 학과를 리턴하는 함수 만들기
# <함수 호출>
# grade, major = get_major('2100')
# print(major, grade) #뉴미디어소프트웨어과 2

def get_major(number):
    major = "과"
    if int(number[1]) == 1 or int(number[1]) == 2:
        major = "소프트웨어과"
    elif int(number[1]) == 3 or int(number[1]) == 4:
        major = "웹솔루션과"
    else:
        major = "디자인과"

    grade = int(number[0])
    print(major, grade)
get_major('2509')

# Quiz2-3. 인수의 개수에 상관없이 인수로 숫자를 여러개 넣고, 함수를 호출하면 그 인수들의 평균을 구하여 리턴하는 함수 만들기
# <함수 호출>
# print(average(10, 20, 30)) #20.0
# print(average(4, 23)) #13.5

def average(*number):
    sum = 0
    for num in number:
        sum += num
    return sum / len(number)

print(average(10, 20, 30))


# Quiz2-4. 키(cm)와 몸무게(kg)를 인수로 넣고, 함수를 호출하여 BMI 지수를 리턴하는 함수 만들기
# (소수 첫째자리까지 반올림)
# * BMI 지수 계산법: 체중(kg) ÷ 키의 제곱(m²)
# 18.5 미만: 저체중
# 18.5 이상 23 미만: 보통
# 23 이상 25 미만: 과체중
# 25 이상: 비만

# <함수 호출>
# bmi = get_bmi(176, 69)
# print(bmi) #22.3

def get_bmi(height, weight):  #키 m 단위 (실수), 성별 "남자"/"여자"
    BMI = round(weight / pow((height/100), 2) ,1)
    print("BMI지수는 " + str(BMI) + "입니다")
    if BMI < 18.5:
        return "저체중입니다."
    elif BMI < 23:
        return "보통입니다."
    elif BMI < 25:
        return "과체중입니다"
    else:
        return "비만입니다"
print( get_bmi(160, 55))
print( get_bmi(170, 75))


# Quiz3-1. n_sum() 함수를 만든다. 함수의 인수(argument)로 10자리 숫자보다 작은 숫자를 넣으면, 각 자리의 숫자의 합계를 리턴한다. 10자리 이상이면 -1 리턴한다.
# result = n_sum(10)
# print(result)        #1
# result = n_sum(331)
# print(result)         #7
# result = n_sum(408)
# print(result)         #12
# result = n_sum(1000000000)
# print(result)         #-1

def n_sum(n):
    num = str(n)
    # 123//100 : 1
    # 123//10 : 2
    # 123%3 : 3
    if len(num) < 10:
        sum = 0
        # for i in range(len(num)):   #len(num):3 range(3): 0, 1 ,2
        #     sum += int(num[i])  #'4'->4
        for i in num:       #문자열은 인덱스[0]부터 차례대로 그냥 들어간다.
            sum += int(i)
        return sum
    else:
        return -1

result = n_sum(10)
print(result)        #1
result = n_sum(331)
print(result)         #7
result = n_sum(408)
print(result)         #12
result = n_sum(1000000000)
print(result)         #-1



# Quiz3-2. get_subway_fare() 함수를 만든다. 이 함수는 인수로 가는 거리(km)를 숫자로 넣으면, 요금을 리턴한다.
# * 지하철 요금계산법 10km 이내: 720원(청소년), 10~50km: 5km마다 100원, 50km 초과 시 8km마다 100원
# fare = get_subway_fare(5)
# print(fare)        #720

# fare = get_subway_fare(26)
# print(fare)        #1120
# fare = get_subway_fare(61)
# print(fare)        #1720

def get_subway_fare(km):
    fare = 720
    if km < 10:
        return fare
    elif km < 50:
        fare = math.ceil((km -10) / 5) * 100 + 720
        return round(fare)
    else:
        fare = 720 + (50-10)//5*100 + (math.ceil((km - 50) / 8) * 100)      # 1520: 720 + (50-10)//5*100
        return round(fare)

fare = get_subway_fare(5)
print(fare)        #720
fare = get_subway_fare(25)
print(fare)        #1020
fare = get_subway_fare(26)
print(fare)        #1120
fare = get_subway_fare(61)
print(fare)        #1720


# Quiz3-3. get_three_six_nine() 함수를 만든다. 이 함수에 숫자를 입력하면 369 게임에  해당하는 답변을 리턴한다.
# * 369게임: 숫자의 어느 자리든 3 또는 6 또는 9가 있다면 그 갯수만큼 '짝'을 외치고, 아니면 그냥 숫자를 외친다.
# 힌트: 문자열 함수 중에 특정 글자를 세는 함수가 있음
# result = get_three_six_nine(1)
# print(result)        #1
# result = get_three_six_nine(3)
# print(result)        #짝
# result = get_three_six_nine(16)
# print(result)        #짝
# result = get_three_six_nine(36)
# print(result)        #짝짝

def get_three_six_nine(game):
    num = str(game)
    count_369 = 0
    for x in num:       # num: '16' x: '1' '6'
        if (x == '3') or (x == '6') or (x == '9'):
            count_369 += 1
    if count_369 == 0:
        return num
    else:
        return count_369 * '짝'

result = get_three_six_nine(1)
print(result)        #1
result = get_three_six_nine(3)
print(result)        #짝
result = get_three_six_nine(16)
print(result)        #짝
result = get_three_six_nine(36)
print(result)        #짝짝

# Quiz3-4. 나만의 재미난 문제를 만들어보세요. 단, 조건이 있습니다.
# 1. 함수의 이름을 정해준다.
# 2. 인수로 넣어야하는 자료형이나 개수를 말해준다.
# 3. 리턴하는 것을 말해준다.
# 4. 출력 예시를 보여준다.
# 5. 내가 낸 문제의 답안을 제출한다.

# 1. 함수의 이름은 RSP()이다
# 2. 인수에는 '가위', '바위', '보' 중에 2가지를 입력한다.
# 3. 리턴에는 가위바위보에 결과를 출력한다.
# 4. 출력 예시: "비겼습니다!" "바위가 이겼습니다!"
# 5.

lis = ['가위', '바위', '보']
def RSP(a, b):
    if (a == b):
        return "비겼습니다!"
    elif (a == lis[0] and b == lis[1]) or (b == lis[0] and a == lis[1]):
        return "바위가 이겼습니다!"
    elif (a == lis[0] and b == lis[2]) or (b == lis[0] and a == lis[2]):
        return "가위가 이겼습니다!"
    elif (a == lis[1] and b == lis[2]) or (b == lis[1] and a == lis[2]):
        return "보가 이겼습니다!"

result = RSP('가위', '가위')
print(result)
result = RSP('바위', '가위')
print(result)
result = RSP('바위', '보')
print(result)


'''
Quiz4-1. [학생퀴즈] 소수판별하기(소수: 1이나 자기자신으로만 나누어 떨어지는 수)
is_prime() 함수를 만든다.
인수로 1개의 숫자를 받는다.
인수로 넘어온 숫자가 소수(prime number)이면 "소수" 아니면, "소수 아님" 리턴한다.
'''

def is_prime(n):
    if n != 1:
        for i in range(2, n):
            if n % i == 0:
                return '소수 아님'
    else:
        return '소수 아님'
    return '소수'
result = is_prime(2)
print(result)     #소수
result = is_prime(13)
print(result)     #소수
result = is_prime(36)
print(result)     #소수 아님


'''
Quiz4-2. [학생퀴즈] get_compliment() 함수를 만든다. 이 함수에 '고구마' 또는 '맛있는'이 들어가는 말을 입력하면 그에 해당하는 답변을 리턴한다.
'고구마'가 들어가는 말을 입력하면 '왓쇼이!', '맛있는'이 들어가는 말을 입력하면 '우마이!',
'놀랄 만한', '황당한', '굉장한'이 들어가는 말을 입력하면 '요모야..!', 특정 단어가 하나라도 들어가지 않는다면 '으무!'를 리턴한다. 
'''
def get_compliment(word):
    if '고구마' in word:
        return '왓쇼이'
    elif '맛있는' in word:
        return '우마이'
    elif '놀랄 만한' in word or '황당한' in word or '굉장한' in word:
        return '요모야..!'
    else:
        return '으무!'

result = get_compliment('고구마 된장국')
print(result) # 왓쇼이!
result = get_compliment('맛있는 크레이프')
print(result) # 우마이!
result = get_compliment('놀랄 만한 상황')
print(result) # 요모야..!
result = get_compliment('좋은 마음가짐이다!')
print(result) # 으무!