#!/usr/bin/env python
# coding: utf-8

# In[7]:


# QUIZ) 숫자와 부호를 입력받아 계산식을 구하는 프로그램 작성 (입력 형식은 10 + 20)
id = input(f'숫자를 입력하시오 ex) 10 + 20 : ').split()
if id[0].isdigit() and id[2].isdigit:
    if id[1] in '+-*/':
        if id[1] == '+':
            result = int(id[0]) + int(id[2])
        elif id[1] == '-':
            result = int(id[0]) - int(id[2])
        elif id[1] == '*':
            result = int(id[0]) * int(id[2])
        else:
            result = int(id[0]) / int(id[2])
        print(f'{id[0]} {id[1]} {id[2]} = {result}')
    else:
        print(f'입력 오류 : 부호 입력')
else:
    print(f'입력 오류 : 숫자 입력')


# In[9]:


# 1부터 100까지의 수 중에서 3의 배수의 합을 구하세요
total = 0
for i in range(1, 101):
    if i % 3 == 0:
        total += i
print(total)


# In[14]:


# 숫자를 입력받아 해당하는 숫자의 구구단을 출력하세요
input_data = input('숫자를 입력하세요 : ')
if input_data.isdigit():
    for i in range(1,10):
        print(f'{input_data} * {i} = {int(input_data)*i}')
else:
    print(f'입력 오류 : 숫자 입력')


# In[24]:


out = ''
for i in range(1, 11):
    for j in range(0,i):
        out += '*'
    out += '\n'
print(out)

for i in range(1,11):
    for j in range(0,i):
        print('*', end = '')  # end의 default 값 = \n
    print(end = '\n')


# In[31]:


# 구구단 로직
for i in range(2,10,4):
    for num in range(i,i+4):
        print(f'   {num}단\t', end = '\t')
    print()
    for j in range(1,10):
        for num in range(i,i+4):
            print(f'{num} * {j} = {num*j}', end = '\t')
        print()


# In[34]:


# 1부터 10까지의 수 중에서 2의 배수의 합을 구함 (while문 이용)
total = 0
i = 0
while True:
    if i > 10:
        break
    i += 1
    if i % 2 == 0:
        total += i
    else:
        continue
    print(f'{i} = {total}')


# In[40]:


# 문제) 2부터 9 사이의 숫자를 입력받아 해당 숫자의 구구단 출력
# 입력한 자료에 'q'가 입력되면 종료
while True:
    num = input('숫자를 입력하세요 : ')
    if num == 'q':
        break
    if not num.isdigit():
        print('2 ~ 9 사이의 숫자를 입력하세요')
        continue
    num=int(num)
    if num < 2 or num > 9:
        continue
    for i in range(1,10):
        print(f'{num} * {i} = {num*i}')


# In[44]:


# 문제) 이름과 성적을 입력받아 이름을 키로 성적을 값으로 딕셔너리에 저장
#       이름에 'q'가 입력되면 입력 종료
#       1. 입력된 자료를 홍길동 80 이러한 형식으로 출력
#       2. 검색하고자 하는 이름 입력 -> 입력된 이름을 검색한 후 해당 점수 출력
#       3. 전체 입력한 학생의 학생 수와 총첨 평균을 출력
#       4. 홍길동 80 입력은 이름과 성적을 동시에 입력

# name = '홍길동'
# students[name] = 80
# 이름과 성적을 입력받아 문자열을 space로 분리해서 처음 자료는 name에, 두번째 자료는 score 저장
# name이 'q'이면 입력 종료
#  아니면 students에 자료 저장

students = {}
while True:
    student = input('이름과 성적을 입력하세요 : ').split()
    if student[0] == 'q':
        break
    if not (student[0].isalpha() and student[1].isdigit()) :
        continue
    name = student[0]
    score = student[1]
    students[name] = int(score)
print(students)


# In[46]:


# 검색하고자 하는 이름 입력 -> 입력된 이름을 검색한 후 해당 점수 출력
sn = input('이름을 입력하시오 : ')
if sn in students:
    print(students[sn])


# In[50]:


# 전체 입력한 학생의 학생 수와 총첨 평균을 출력
total = 0
for i in students:
    total += students[i]
print(len(students), total/len(students))


# In[2]:


# 이름과 국어 영어 수학 성적을 입력받아 이름을 키로 딕셔너리에 저장
# 이름에 'q'가 입력되면 입력 종료
# 각 학생의 총점 평균 추가
# 전체 학생의 과목별 총점, 평균을 구하세요
students = {}
while True:
    student = input('이름과 각 과목의 성적을 입력하세요 : ').split()
    if student[0] == 'q':
        break
    if not len(student) == 4:
        continue
    name = student[0]
    scores = []
    for i in range(1,4):
        scores.append(int(student[i]))  # append는 추가할 때 마지막에 추가됨
    students[name] = scores
print(students)


# In[3]:


# 각 학생의 총점 평균 추가
for i in students:
    scores = students[i]
    total = 0
    for j in scores:
        total += j
    print(total, total/3)


# In[13]:


character = {
    'name' : '기사',
    'level' : 12,
    'items' : {
        'sword': '불꽃의 검',
        'armor' : '풀플레이트'
    },
    'skill' : ['베기', '세게 베기', '아주 세게 베기']
}

for key in character:
    if type(character[key]) == list:
        for value in character[key]:
            print(f'{key} : {value}')
    elif type(character[key]) == dict:
        pass
        for value in character[key]:
            print(f'{key} : {character[key][value]}')
    else:
        print(f'{key} : {character[key]}')


# In[3]:


import sys

print(sys.argv)
print()
print("window version : ", sys.getwindowsversion())
print()
print('copyright : ', sys.copyright)
print()
print('version : ', sys.version)

sys.exit()


# In[ ]:




