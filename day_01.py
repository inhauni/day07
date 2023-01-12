
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
