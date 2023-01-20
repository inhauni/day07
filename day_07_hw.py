# # 10. 1
#
# class Thing():
#     pass
#
# print(Thing)
#
# example=Thing()
# print(example)
#
# # 10. 2
#
# class Thing2:
#     letters='abc'
#
# print(Thing2.letters)

# 10. 3

class Thing3:
    def __init__(self,letters):
        self.h_letters=letters

    def info(self):
        print(self.h_letters)

    # @property
    # def letters(self):
    #     print('inside the getter', end=' ')
    #     return self.h_letters



t3=Thing3('xyz')
t3.info()
# t3.letters = 'zyx' if letters 속성을 property를 이용해서 private으로 바꾸면-> 오류 발생 : property 속성으로 인해 외부 접근이 차단됨
# t3.info()

# 10. 4 , 10. 5

class Element:
    def __init__(self,name,symbol,number):
        self.name=name
        self.symbol=symbol
        self.number=number

    def dump(self):
        print(f'{self.name} 원소의 약칭은 {self.symbol}이고, 원소번호는 {self.number} 입니다.')


e1=Element('Hydrogen','H',1) # 객체 생성

el_dict={keyz:vals for keyz,vals in zip(('name','symbol','number'), (e1.name,e1.symbol,e1.number))}

print(el_dict) # dic 생성

# hydrogen=Element(el_dict['name'],el_dict['symbol'],el_dict['number'])
hydrogen=Element(**el_dict) # **kwargs는 함수 외부에서 딕셔너리 kwargs를 이름=값 형태의 인수(키워드 인수)로 분해한다.
                            # 따라서, name=Hydrogen라는 키워드 인수가 Element 클래스에 대입됨.
print(f'이름 : {hydrogen.name}, symbol : {hydrogen.symbol}, 순서 : {hydrogen.number}')

# 10. 6

# hydrogen.dump()

# 10. 7

print(hydrogen)

class Element2(Element):
    def __init__(self,name,symbol,number):
        super().__init__(name,symbol,number)


    def __str__(self):
        return f'{self.name} 원소의 약칭은 {self.symbol}이고, 원소번호는 {self.number} 입니다.'

hydrogen2=Element2(**el_dict)
print(hydrogen2) # __str__ 이 반환됨


# 10. 8

# <name 속성만 private로 바꿔본 예시>

# 1] getter / setter method


class Element:
    def __init__(self,name,symbol,number):
        self.name=name
        self.symbol=symbol
        self.number=number

    def dump(self):
        print(f'{self.name} 원소의 약칭은 {self.symbol}이고, 원소번호는 {self.number} 입니다.')

    def get_name(self):
        print('inside the getter',end=' ')
        return self.name
    def set_name(self, name):
        print('inside the setter')
        self.name = name

e2=Element('ox','O',8)
print(e2.get_name())
e2.set_name('oxygen')
print(e2.get_name())

# 2-1] Use property (name 구문 이용)

class Element:
    def __init__(self,input_name,symbol,number):
        self.hidden_name=input_name
        self.symbol=symbol
        self.number=number

    def dump(self):
        print(f'{self.hidden_name} 원소의 약칭은 {self.symbol}이고, 원소번호는 {self.number} 입니다.')


    def get_name(self):
        print('inside the getter',end=' ')
        return self.hidden_name

    def set_name(self, name):
        print('inside the setter')
        self.hidden_name = name

    name = property(get_name, set_name)

e3=Element('Helyum','He',2)

print(e3.name)  # getter에 접근 (속성처럼 name에 접근 가능)
e3.name='Helium'  # setter에 접근
print(e3.name)

# 2-2] Use property (decorator 사용)

class Element:
    def __init__(self,input_name,symbol,number):
        self.hidden_name=input_name
        self.symbol=symbol
        self.number=number

    def dump(self):
        print(f'{self.hidden_name} 원소의 약칭은 {self.symbol}이고, 원소번호는 {self.number} 입니다.')

    @property
    def name(self):
        print('inside the getter',end=' ')
        return self.hidden_name

    @name.setter
    def name(self, name):
        print('inside the setter')
        self.hidden_name = name

e4=Element('리튬','Li',3)

print(e4.name)
e4.name='Lithium'
print(e4.name)


# 10. 8 예시

class Element:
    def __init__(self,input_name,symbol,number):
        self.hidden_name=input_name
        self.hidden_symbol=symbol
        self.hidden_number=number


    @property
    def name(self):
        print('inside the getter',end=' ')
        return self.hidden_name

    @property
    def symbol(self):
        print('inside the getter', end=' ')
        return self.hidden_symbol

    @property
    def number(self):
        print('inside the getter', end=' ')
        return self.hidden_number

    # @name.setter  -> 속성에 대한 setter 프로퍼티를 명시하지 않을 경우 외부로부터 속성 설정 불가 : 읽기 전용이 된다 (READ ONLY)
    # def name(self, name):
    #     print('inside the setter')
    #     self.hidden_name = name
    #
    # @symbol.setter
    # def symbol(self, symbol):
    #     print('inside the setter')
    #     self.hidden_symbol = symbol
    #
    # @number.setter
    # def numberset(self, number):
    #     print('inside the setter')
    #     self.hidden_number = number


e5=Element('베릴륨','Be',4)

print(e5.name)
# e5.name ='Beryllium' -> 오류 발생 : can't set attribute (외부에서 속성을 건들 수 없기 때문)



# 10. 9

class Bear:

    @classmethod
    def eats(cls):
        return f'\'berries\' ({cls.__name__})'

class Rabbit:

    @classmethod
    def eats(cls):
        return f'\'clover\' ({cls.__name__})'

class Octothorpe:

    @classmethod
    def eats(cls):
        return f'\'campers\' ({cls.__name__})'

print(Bear.eats(),Rabbit.eats(),Octothorpe.eats())

# -> 'berries' (Bear) 'clover' (Rabbit) 'campers' (Octothorpe) 출력


class Bear:

    def eats(self):
        return 'berries'

class Octothorpe:

    def eats(self):
        return 'campers'

class Rabbit:


    def eats(self):
        return 'clovers'

bear=Bear()
rabbit=Rabbit()
octothorpe=Octothorpe()

print(bear.eats(),rabbit.eats(),octothorpe.eats())


# 10. 10

class Laser:
    def does(self):
        return 'disintegrate'


class Claw:
    def does(self):
        return 'crush'


class Smartphone:
    def does(self):
        return 'ring'

class Robot:
    # def __init__(self,laser,claw,smart):
        # self.laser=laser
        # self.claw=claw
        # self.smart=smart
    def __init__(self):
        self.laser=Laser()  # 여기서 바로 self.laser를 Laser class의 객체로 생성
        self.claw=Claw()
        self.smart=Smartphone()
    def does(self):
        return f'Laser : {self.laser.does()}, Claw : {self.claw.does()}, Smartphone : {self.smart.does()}'
         # -> self.laser가 객체이므로 바로 does() 함수 호출 가능


# l=Laser()
# c=Claw()
# s=Smartphone()
# r=Robot(l.does(),c.does(),s.does())
# r.does()

robbie=Robot()
print(robbie.does())





