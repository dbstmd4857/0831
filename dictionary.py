#중괄호를 이용하여 딕셔너리를 생성합니다.
#각 쌍의 키와 값 사이에 콜론(:)을 사용합니다.
#len()함수는 딕셔너리에 있는 키-값 쌍의 수를 셉니다.

a_dict={'one':1,'two':2,'three':3}
b_dict={3:'red',4:'green',5:'blue'}
print(a_dict)
print(b_dict)
print("a_dict has {!s} elements".format(len(a_dict)))
print(a_dict['one'])
print(b_dict[3])
