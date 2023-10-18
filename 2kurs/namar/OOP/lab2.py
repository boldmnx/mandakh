# Даалгавар 1
# Дараах тэмдэгт мөр өгөгдөв: 1
s = 'django'

print(s[0])
print(s[5])
print(s[:-1])

print(s[:-2][1:])
print(s[4:])
print(s[3:-1])
# -----------------------------------------------------------------------------------------------------------------------

## Даалгавар 2 ##
#################

# Дараах холимог жагсаалт өгөгдөв. (nested list)
# l = [3, 7, [1, 4, 'hello']]
# l[2][2] = 'goodbye'
# print(l)
# "hello" тэмдэгтийг "goodbye" болгон өөрчилнө үү #


## Даалгавар 3 ##
#################

# Дараах dictionary-с 'hello' тэмдийг хэвлэнэ үү

# d1 = {'simple_key':'hello'}
# print(d1['simple_key'])

# d2 = {'k1':{'k2':'hello'}}
# print(d2['k1']['k2'])

# d3 = {'k1':[{'nest_key':['this is deep',['hello']]}]}
# print(d3['k1'][0]['nest_key'][1][0])


## Даалгавар 4 ##
#################

# Дараах жагсаалтыг утгын давхцалгүй жагсаалт болгоно үү:
# mylist = [1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]
# print(set(mylist))

## Даалгавар 5 ##
#################

# # Дараах 2 хувьсагч өгөгдөв:
# age = 4
# name = "Sammy"

# # Дараах форматаар хэвлэнэ үү:
# "Hello my dog's name is Sammy and he is 4 years old"
# print("Hello my dogs name is "+name+" and he is "+str(age)+" years old")

# # f string ашиглан дараах форматаар хэвлэнэ үү:
# "Hello my dog's name is Sammy and he is 4 years old"
# print(f'Hello my dogs name is {name} and he is {age} years old')


# Даалгавар 6 ##
#################
# •	1-10 хүртэлх тоог while давталт ашиглан хэвлэх
# i = 0
# while i < 10:
#     i += 1
#     print(i)


# too = print('sn Bnuu my applicationd tavtai moril')
# while too != 0:
#     too = int(input("1-7hurtel too oruulna uu garah bol 0 tovchiig darn uu: "))
#     if too == 1:
#         print('davaa garig')
#     elif too == 2:
#         print('mygmar garig')
#     elif too == 3:
#         print('lhagva garig')
#     elif too == 4:
#         print('purev garig')
#     elif too == 5:
#         print('baasan garig')
#     continue


# •	100-10 хүртэлх тоог хэвлэх (break)
# for i in range(100,10,-1):
#     if i==11:
#         break
#     print(i)
# •	1-50 хүртэлх тоонуудаас тэгш тоог хэвлэх
# while i < 50:
#     i += 1
#     if i % 2 == 0:
#         print(i)
# •	1-10 хүртэлх тоонуудаас хамгийн эхний тэгш тоог хэвлэх (break)
# while i < 10:
#     i += 1
#     if i % 2 == 0:
#         print(i)
#         break

#################
## Даалгавар 7 ##
#################
# •	“Python” тэмдэгтээс “h” тэмдэгтийг хасаж хэвлэх
# a = 'Pythonh'
# too = ''
# for i in a:
#     if i != 'h':
#         too += i
# print(too)
# print(a.replace('h', '',2))
# •	1-50 хүртэлх тоонуудаас тэгш тоог хэвлэх (continue)
# for i in range(1, 50):
#     if i % 2 != 0:
#         continue
#     print(i)


# •	1-10 хүртэлх тоонуудаас хамгийн сүүлчийн тэгш тоог хэвлэх (continue, break)
# last = 0
# for i in range(1, 10):
#     if i % 2 == 0:
#         last = i
#     continue
# print(last)


#################
## Даалгавар 8 ##
#################
# •	Гараас ямар нэгэн тоон утга авч оронгийн нийлбэрийг хэвлэх. Жишээ нь:
# a = 123
# too = str(a)
# s = 0
# for i in too:
#     s += int(i)
# print(s)
# •	Оролт: 123
