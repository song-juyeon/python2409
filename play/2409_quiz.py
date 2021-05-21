'''

'''

# import random
# 반4 = list(range(1,20)) # 1~19까지
# 반4.remove(3) # 3번을 제외함
# print(반4)
# print(random.choice(반4))

'''
3-1.주민등록번호 앞 6자리를 변수 id_number에 넣고,
출생년도 끝 두자리\n출생 월일\n그 두개의 곱 출력
예시
id_number = 020316 일 때

출력 예시
02
0316
632
'''
id_number = "040317"
year = id_number[0:2]
# print(id_number[0:2])   #방법1
# print(id_number[:2])    #방법2
# print(id_number[-6:-4]) #방법3
# print(id_number[:-4])   #방법4
month_day = id_number[-4:]
# print(id_number[2:])    #방법1
# print(id_number[2:6])   #방법2
# print(id_number[-4:])   #방법3
# print(int(year) * int(month_day)) #문자열이기 때문에 숫자로 변경
# print('곱한 결과 : ' + str(int(year) * int(month_day))) #+로 연결시 같은 타입으로만 연결가능
# print('곱한 결과 : ', int(year) * int(month_day)) #,로 연결하면 타입이 달라도 연결가능/ ,부분은 한칸 띄어짐
# type = 자료형


'''
1-2. 집 전화번호를 phone_number에 넣고,
지역번호\n맨 끝 네 자리 출력하기(지역번호의 자리수와 상관없이 동작하도록 하자)
예시
phone_number = 02-1234-5678 또는 032-9876-4321

출력 예시
02 또는 032
5678 또는 4321
'''
phone_number = "033-1374-2556"
# print(phone_number[0:3])
print(phone_number[:phone_number.index("-")])
print(phone_number[-4:])

# f-sring
name = '송주연'
age = 18
# %-formatting
print('안녕 나는 %s이야, 내 나이는 %d살이야' %(name, age))
# str.format()
print('안녕 나는 {}이야, 내 나이는 {}살이야'.format(name, age))
# f-string *
print(f'안녕 나는 {name}이야, 내 나이는 {age}살이야')
print(name * 10)
# 문자열 + 문자열 <가능>
# 문자열 * 정수형 <가능>(문자열의 반복)
student_number = '2409'
print(student_number[1:2])
print(student_number[1])
print(student_number[-2:][1])
print(int(student_number[-2:]))

# 휴대폰 번호를 입력할 때 - 상관없이
phone_number1 = "010-2540-5357"
phone_number2 = "010 7584 1367"
phone_number3 = "01073201685"

# result = phone_number1.replace('-', '')
# print(result)
# result = phone_number2.replace(' ','')
# print(result)
phone_Number = phone_number1
result = phone_Number.replace('-','').replace(' ','')
print(result)
print(phone_number3)


# Quiz2-1. 학번을 student_number 변수에 넣고, 학급을 출력하고, 학과를 출력하기
# 반이 0 미만이거나 7 이상이면 "잘못 입력했습니다." 출력하기
# student_number = '2100' 또는 student_number = '2000'
# <출력 예시>
# 1반 뉴미디어소프트웨어과 또는 잘못 입력했습니다.

student_number = '2409'
ban = int(student_number[1])
majors = ['소프트웨어과', '소프트웨어과', '웹솔루션과', '웹솔루션과', '디자인과','디자인과']
if 1 <= ban <= 6:
    print(f"{ban}반 {majors[ban - 1]}")
else:
    print("잘못 입력했습니다.")


# Quiz2-2. 학번을 함수의 인수(argument)로 전달하여 호출하면 학년과 학과를 리턴하는 함수 만들기
# <함수 호출>
# grade, major = get_major('2100')
# print(major, grade) #뉴미디어소프트웨어과 2

def get_major(student_number):
    majors = ['소프트웨어과', '소프트웨어과', '웹솔루션과', '웹솔루션과', '디자인과', '디자인과']
    grade = student_number[0]
    classroom = int(student_number[1])
    return grade, majors[classroom-1]

grade, major = get_major('2100')
print(major, grade)


# Quiz2-3. 인수의 개수에 상관없이 인수로 숫자를 여러개 넣고, 함수를 호출하면 그 인수들의 평균을 구하여 리턴하는 함수 만들기
# <함수 호출>
# print(average(10, 20, 30)) #20.0
# print(average(4, 23)) #13.5

def average(*number):
    return sum(number)/len(number)

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

def get_bmi(height, weight):
    height /= 100
    bmi = weight / height ** 2      # ** =제곱
    return round(bmi, 1)

bmi = get_bmi(176, 69)
print(bmi)

if bmi < 18.5:
    print("저체중입니다.")
elif bmi < 23:
    print("보통입니다.")
elif bmi < 25:
    print("과체중입니다")
else:
    print("비만입니다")


# # <range>
# a=range(1, 10, 2)
# print(a)

# 구구단 7단 출력
# i = 1~9
for i in range(1,10):
    print(f'7 x {i} = {7*i}')

# 구구단 2~9단 출력하기
for dan in range(2,10):
    for j in range(1,10):
        print(f'{dan} x {j} = {dan*j}')
    print()
print('-------------------')
# 구구단 2~7단 출력하기
for dan in range(2,10):
    for j in range(1,10):
        print(f'{dan} x {j} = {dan*j}')
    print()
    if dan == 7:
        break
print('-------------------')

# 구구단 2~9단 출력하기
for dan in range(2,10):
    for j in range(1,10):
        if j % 2 == 0:    #if j == 2 or j == 4 or j == 6 or j == 8:
            continue
        print(f'{dan} x {j} = {dan*j}')
    print()
    if dan == 7:
        break


# print(5/2)
# print(5//2)
# print(5%2)