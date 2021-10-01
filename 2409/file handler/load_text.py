print('전체 한꺼번에 읽기')
f = open('text.txt', 'r', encoding='utf-8')
data = f.read()
f.close()
print(data)

print('---------------------\n한줄 씩 읽기')
f = open('text.txt', 'r', encoding='utf-8')
while True:
    line = f.readline()     #line: 이유빈: 초록색\n
    if line == '':
        break
    print(line.rstrip())    #line.replace('\n', '')
f.close()

print('---------------------\n전체를 한꺼번에 읽고, 줄 별로 리스트')
f = open('text.txt', 'r', encoding='utf-8')
lines = f.readlines()
f.close()
for line in lines:
    print(line.rstrip())

# quiz
# 이름: 이유빈 [tab] 좋아하는 색: 초록색
# 이름: 김효진 [tab] 좋아하는 색: 하늘색
print('---------------------\n퀴즈')
f = open('text.txt', 'r', encoding='utf-8')
lines = f.readlines()
f.close()
for line in lines:
    # line = '고에스더:검은색'
    data = line.split(':')

    # print('이름:' + line.rstrip()[:3] + '\t좋아하는 색: ' + line.rstrip()[4:])
    print('이름:' + data[0] + '\t좋아하는 색: ' + data[1])
