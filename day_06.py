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

    def __init__(self, name, owner, skills): # name이라는 매개변수
        self.name = name # 받은 name을 속성.name에 저장
        print(f'포켓몬 {name} 객체 생성됨')
        self.owner = owner # 받은 owner변수를 속성.owner에 저장
        self.skills = skills.split('/')
    def info(self):
        print(f'{self.owner}의 포켓몬은 {self.name}입니다.')
        for skill in self.skills:
            print(skill,end=' ')



p1=Pokemon('피카츄','지우','백만 볼트/몸통박치기/전광속화') # 객체 생성
p2=Pokemon('꼬부기','이슬이','물대포/몸통박치기')

# print(f'{p1.owner}의 포켓몬은 {p1.name}입니다.')
# 이 부분을 일일이 치기 귀찮으므로 class 내부에 info라는 함수를 새로 만들어 이 값을 출력

p1.info()
p2.info()
print(p1.skills)


