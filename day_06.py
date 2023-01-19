# <Class>

# class Cat:
#     pass
#
# a_cat = Cat()
# another_Cat=Cat()
# print(a_cat)
#
# a_cat.age =3
# a_cat.name ="abc"
# a_cat.nemesis='another_cat'
# print(a_cat.age)

class Pokemon:

    def __init__(self): # 객체 생성시 동작
        print("포켓몬 객체 생성됨")

p1=Pokemon() # '포켓몬 객체 생성됨' 이 출력됨
p2=Pokemon() # '포켓몬 객체 생성됨' 이 출력됨

print(p1,p2) # 두 객체의 주소가 다르다. = 다른 객체이다.