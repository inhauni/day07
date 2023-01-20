

# class Pokemon:
#
#     def __init__(self, owner, skills): # name이라는 매개변수
#
#         self.owner = owner
#         self.skills = skills.split('/')
#         print(f'포켓몬 생성:', end=' ')
#
#     def info(self):
#
#         print(f'{self.owner}의 포켓몬의 스킬')
#         for skill in self.skills:
#             print(skill)
#
#     def attack(self, idx):
#         print(f'{self.owner}의 포켓몬이 {self.skills[idx]} 공격 시전!')
# #<상속>
#
# class Pikachu(Pokemon): # 상속(inheritance) : 부모 class 는 pokemon / 자식 class는 pickchu
#     def __init__(self, owner, skills):  # name이라는 매개변수
#         super().__init__(owner,skills)
#         self.name = '피카츄'
#         print(f'{self.name}')
#
#     def attack(self, idx):
#         print(f'{self.owner}의 {self.name}가 {self.skills[idx]} 공격 시전!') # override
#
# class KKobugi(Pokemon):
#     def __init__(self,owner,skills):
#         super().__init__(owner,skills)
#         self.name = '꼬부기'
#         print(f'{self.name}')
#
#     def attack(self, idx): # override :부모 class의 method를 자식 class에서 재정의
#         print(f'{self.owner}의 {self.name}가 {self.skills[idx]} 공격 시전!')
#
#     def swim(self):
#         print(f'{self.name}가 수영을 합니다')
#
# # p1=Pokemon('피카츄','지우','백만 볼트/몸통박치기/전광속화') # 객체 생성
# # p2=Pokemon('꼬부기','이슬이','물대포/몸통박치기')
#
# pk1 =Pikachu('덴트','번개/백만볼트')
#
# ggo1=KKobugi('이슬이','물대포/몸통박치기')
#
# ggo1.attack(1)
# pk1.attack(0)
# p1=Pokemon('주인공','어떤공격')
# p1.attack(0)
# ggo1.swim()
# # p1.swim() # 오류 발생 : KKobugi class만 사용 가능한 고유 method




class Animal:
    def says(self):
        return 'I speak!'

class Donkey(Animal):
    def says(self):
        return '히하'

class Horse(Animal):
    def says(self):
        return '히이잉!'

class Mule(Donkey,Horse):
    pass
class Hinny(Horse,Donkey):
    pass

m1=Mule()
m2=Hinny()

print(Mule.mro())
print(Hinny.mro())
