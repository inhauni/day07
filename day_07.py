# 포켓몬 게임

class Pokemon:

    def __init__(self, owner, skills): # name이라는 매개변수

        self.owner = owner
        self.skills = skills.split('/')
        print(f'포켓몬 생성:', end=' ')

    def info(self):

        print(f'{self.owner}의 포켓몬의 스킬')
        for i in range(len(self.skills)):
            print(f'{i+1} : {self.skills[i]}')

        # for skill in self.skills:
        #     print(f'{skill})

    def attack(self, idx):
        print(f'{self.owner}의 포켓몬이 {self.skills[idx]} 공격 시전!')
# #<상속>

class Pikachu(Pokemon): # 상속(inheritance) : 부모 class 는 pokemon / 자식 class는 pickchu
    def __init__(self, owner, skills):  # name이라는 매개변수
        super().__init__(owner,skills)
        self.name = '피카츄'
        print(f'{self.name}')

    def attack(self, idx):
        print(f'{self.owner}의 {self.name}가 {self.skills[idx]} 공격 시전!') # override

class KKobugi(Pokemon):
    def __init__(self,owner,skills):
        super().__init__(owner,skills)
        self.name = '꼬부기'
        print(f'{self.name}')

    def attack(self, idx): # override :부모 class의 method를 자식 class에서 재정의
        print(f'{self.owner}의 {self.name}가 {self.skills[idx]} 공격 시전!')

    def swim(self):
        print(f'{self.name}가 수영을 합니다')

# p1=Pokemon('피카츄','지우','백만 볼트/몸통박치기/전광속화') # 객체 생성
# p2=Pokemon('꼬부기','이슬이','물대포/몸통박치기')


class Pairi(Pokemon):
    def __init__(self, owner, skills):  # name이라는 매개변수
        super().__init__(owner,skills)
        self.name = '파이리'
        print(f'{self.name}')

while True:
    menu =input('1) 포켓몬 생성 2) 프로그램 종료 : ')
    if menu == '2':
        print('프로그램을 종료합니다')
        break
    elif menu=='1':
        pokemon = input('1) 피카츄 2) 꼬부기 3) 파이리 : ')
        if pokemon == '1':
            n=input('플레이어 이름 입력 :')
            sk=input('사용 가능한 기술 입력(/로 구분)')
            p=Pikachu(n,sk)

        elif pokemon == '2':
            n = input('플레이어 이름 입력 :')
            sk = input('사용 가능한 기술 입력(/로 구분)')
            p = KKobugi(n, sk)
        elif pokemon == '3':
            n = input('플레이어 이름 입력 :')
            sk = input('사용 가능한 기술 입력(/로 구분)')
            p = Pairi(n, sk)
        else:
            print('1,2,3 중에서 골라주세요: ')
        info_attack =input('공격하시겠습니까? (y/n) : ')
        if info_attack == 'n':
            print('프로그램을 종료합니다')
            break
        elif info_attack == 'y':
            p.info()
            attack_menu = input('공격 번호 선택 : ')
            p.attack(int(attack_menu)-1)
        else:
            print('메뉴에서 골라주세요')
    else:
        print('메뉴에서 골라주세요')