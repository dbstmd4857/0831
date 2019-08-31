#리스트를 만들기 의해서는 대괄호([])를 사용한다

#괄호(()),중괄호({}),대괄호([])

#len()함수를 통해 리스트 내 원소의 수를 샌다.

#max() 함수와 min()함수는 최대/최소 값을 찾는다.

#count()함수는 리스트 내 특정 값이 등장한 횟수를 샌다. 
a_list = [1, 2, 3] 
print(a_list) 
print("a_list has {} elements.".format(len(a_list))) 
print("the maximum value in a_list is{}.".format(max(a_list)))
print("the minimum value in a_list is{}.".format(min(a_list))) 
another_list = ['printer',5,['star','circle',9]] 
print(another_list) 
print("another_list also has {} elements.".format(len(another_list))) 
print("5 is in another_list {} time.".format(another_list.count(5))) 
print(a_list[0]) 
print(a_list[1]) 
print(a_list[2]) 
print(a_list[-1]) 
print(a_list[-2]) 
print(a_list[0:2])
