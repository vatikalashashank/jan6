# dct={'name':'arjun','age':21}
# print(dct['name'])

# dct={'name':'arjun','age':21}
# for key,value in dct.items():
#     print(key,value)

# dct={'hr':{'name':'raj','age':21},'it':{'name':'rrr','age':25}}
# print(dct['it']['name'])

# lst=[1,2,3,4]
# emp=[]
# for x in lst:
#     emp.append(x**3)
# print(emp)
# print([x**3 for x in [1,2,3,4]])

lst=[1,2,3,4]
print({x:x**3 for x in lst})
print({x:x**2 for x in lst})