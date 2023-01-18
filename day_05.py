# Closures : 일반 함수와 다르게 외부 함수의 변수 값을 기억 하고 있다

def calculate():
    x = 1
    y = 2

    def add_sub(n): # x값과 y값(외부함수로부터 생성된 변수값)을 기억하고 있는 closure(고차함수)

        # x=11 : 외부함수의 변수값을 변경하고 저장 -> 이는 calculate 함수의 x=1과 다르다 \
                # 왜냐하면 x=11의 x는 local variable (지역변수) 이므로 함수 밖에선 효력을 상실한다.

        return x + n - y
    print('once') # 한번만 출력됨!!! add_sub로 들어가서 거기서 for문이 돌아감
    return add_sub


c1 = calculate() # 함수를 변수에 대입

for i in range(5):
    print(c1(i)) # add_sub(i)와 같은 의미

#nonlocal : 지역함수 해제
def calculate():
    x = 1
    y = 2
    temp = 0
    def add_sub(n):  # x값과 y값(외부함수로부터 생성된 변수값)을 기억하고 있는 closure(고차함수)
        nonlocal temp
        # x=11 : 외부함수의 변수값을 변경하고 저장 -> 이는 calculate 함수의 x=1과 다르다 \
        # 왜냐하면 x=11의 x는 local variable (지역변수) 이므로 함수 밖에선 효력을 상실한다.
        temp = temp + x +n - y # 이전의 temp값이 남아있어 여기에 대입 된다
        return temp

    return add_sub
