# class Parent:
#     def __init__(self,name):
#         self.name=name
#     def info(self):
#         print(self.name)
#
# class Childeren(Parent):
#     pass
#
#
# c1=Childeren('지현')
# c1.info()

# class Duck():
#     def __init__(self, input_name):
#         self.hidden_name=input_name
#     @property # 이미 만들어진 decorator 사용
#     def name(self):
#         print('inside the getter', end=' ')
#         return self.hidden_name # return 이 있는 쪽에 property
#     @name.setter
#     def name(self, input_name): #함수 이름도 set_name에서 name으로 변경
#         print('inside the setter')
#         self.hidden_name=input_name
#     # name = property(get_name,set_name) # property
#
# # don=Duck('Donald')
# # # print(don.get_name())
# # print(don.name)
# # # don.set_name('Donna')
# # don.name='Donna'
# # # print(don.get_name())
# # print(don.name)
#
# fowl=Duck('Howard')
# print(fowl.name)
# fowl.name ='Happy'
# print(fowl.name)


class Duck():
    def __init__(self, input_name):
        self.__name=input_name # __name : <맹글링> : 외부코드에서 이 속성을 우연히 발견하는 것을 막아줌\
                                        # (단, 속성이 private해지는 것은 아님)
    @property
    def name(self):
        print('inside the getter', end=' ')
        return self.__name
    @name.setter
    def name(self, input_name):
        print('inside the setter')
        self.__name=input_name

fowl=Duck('Howard')
print(fowl.name)
fowl.name ='Happy'
print(fowl.name)
# print(fowl.__name) -> 바로 접근하는 건 불가능
print(fowl._Duck__name)  # -> 이런식으로 접근하면 출력은 가능, 단 이때 'inside the getter는 출력되지 않음' \
                            # (속성의 의도적인 접근을 어렵게 만듦)