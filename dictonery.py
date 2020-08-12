# dict={"name":"mohan" ,"age": 22, "role": "Ba"}
# print(dict)
# thisdict={"name":["mohan","harsh","raj"],
#           "age":[23,22,25],
#         "role":["Ba","dba","gov"]}
# print(thisdict)
# dict.pop("age")
# print(dict)
# dict.popitem()
# print(dict)
# dict.clear()
# print(dict)
# del dict["age"]
# print(dict)
# #making dictionary in tuple
# t=((1,'a'), (2,'b'))
# print(dict(t))
# dict["name"]="kantaa"
# print(dict)
# dict["salary"]=25000
# print(dict)
# #
# print(dict.items())
# for x,y in dict.items():
#     print(x,y)
# #
# print(dict.keys())
# for x in dict.keys():
#     print(x)
# #
# # print(dict.values())
# # for y in dict.values():
# #     print(y)
# #
keys={"a","e","i","o","u"}
values="vowels"
vowels=dict.fromkeys(keys,values)
print(vowels)
dict_2={"name":"sohan","age":"22","role":"baa"}
print(dict_2)
print(dict_2.get("age"))
dict_2['age']=23
print(dict_2.get("age"))
ag=dict_2.setdefault('salary',240000)
print('ag=',dict_2)
print('ag=',ag)
# #for adding salary
# dict_2["salary"]=20000,50000
# print(dict_2)
# dict_3=dict_2.copy()
# print(dict_3)
# ####################
# #########################################
d1={'simple_key':'hello'}
print(d1['simple_key'])
d2={'k1':{'k2':'hello'}}
print(d2['k1']['k2'])
d3={'k1':[{'nest_key':['this is deep',['hello']]}]}
print(d3['k1'][0]['nest_key'][1][0])