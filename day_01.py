
fahrenheit= float(input("화씨온도 : "))
celsius=(fahrenheit-32.0)*5.0/9.0

print(f'화씨 온도 {fahrenheit}도는 섭씨온도 {celsius}도와 같다')

# 교재
# for countdown in 5,4,2,1, "hey!":
#   print(countdown)
# print('프로그램 종료')
countdown_list = [5, 4,3, 2, 1, "hey!"]

for countdown in countdown_list:
    print(countdown_list[-3])
    print(countdown_list[3]) #2
print('프로그램 종료')


# 교재 딕셔너리 예제

subjects = { '의사소통영어' : 'A+',
             '오래된 미래' : 'B+',
             '양자역학' : 'A0',
}

student = '김도훈'
subject = '오래된 미래'
print(student, '학생의 ', subject, '과목 성적은' ,subjects[subject], '입니다')
# old style
print("%s 학생의 %s 과목 성적은 %s입니다" % (student, subject, subjects[subject]))
# morden style (format함수)
print("{0} 학생의 {1} 과목 성적은 {2}입니다".format(student, subject, subjects[subject]))
# f스트링
print(f'{student} 학생의 {subject} 과목 성적은 {subjects[subject]}입니다')

import tkinter as tk

win = tk.Tk()
win.geometry('400x300')
win.title('파이썬 1일차 preview')
win.mainloop()
