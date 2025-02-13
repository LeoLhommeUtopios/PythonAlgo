def add(a,b):
    return a+b

print("avec fonction")
print(add(1,2))

add_lambda = lambda a,b: a + b

print("avec lambda")
print(add_lambda(1,2))

# map() modification de la liste

# def double(x):
#     return x * 2

nums = [1,2,3,4]
result = list(map(lambda x: x * 2,nums))


print(result)

# filter filtrer des elements

# def is_pair(x):
#     return x % 2 ==0

nums = [1,2,3,4,5,6]
# syntaxe : 
result = list(filter(lambda x: x % 2 == 0,nums))
result2 = list(filter(lambda x: x == 5,nums))

print(result)
print(result2)