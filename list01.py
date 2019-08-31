string1="this is a"
string2="short string."
sentence=string1 + string2
print("{}".format(sentence))
print("{}{}{}".format("she is", " very"*4, " beautiful"))
m=len(sentence)
print("{}".format(m))

string1="my deliveralbe is due in may"
string1_list1=string1.split()
string1_list2=string1.split(" ",2)

print(string_list1)
print("FIRST PIECE:{0} SECOND PICEC:{1} THIRD PIECE:{2}"\
     .format(string1_list2[0],string1_list2[1],string1_list2[2]))
string2="Your,deliveralbe,is,due,in,june"
string2_list=string2.split(',')
print(string2_list)
print("{} {} {} {}".format(string2_list[1], string2_list[2], string2_list[5], \
                        string2_list[-1]))

print("{}".format(','.join(string2_list)))