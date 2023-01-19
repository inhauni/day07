# 파이썬 예제 문제

groups ={
    '빅뱅':['지디','태양','탑','대성','승리',],
    '마마무' :['화사','문별','솔라','휘인']
}

for group, mems in groups.items():

    print(f'{group}의 멤버:')

    for mem in mems:
        if mem != '승리':
            print(mem)

