fruit= {"apple", "banana", "cherry"}
print(fruit)
# output:
# {'cherry', 'apple', 'banana'}
# {'apple', 'banana', 'cherry'}

fruit = {"apple", "banana", "cherry"}

for x in fruit:
  print(x)
#   output:
# {'apple', 'cherry', 'banana'}
# new :
# apple
# cherry
# banana

fruit = {"apple", "banana", "cherry"}

print("banana" in fruit)
# output:
# {'apple', 'cherry', 'banana'}
# apple
# cherry
# banana
# new:
# True

fruit = {"apple", "banana", "cherry"}

print("bread" in fruit)
# output :
# {'apple', 'cherry', 'banana'}
# apple
# cherry
# banana
# True
# new :
# False

fruit = {"apple", "banana", "cherry"}

fruit.add("orange")

print(fruit)

# output:
# {'apple', 'banana', 'cherry'}
# apple
# banana
# cherry
# True
# False
# new:
# {'orange', 'apple', 'banana', 'cherry'}

fruit = {"apple", "banana", "cherry"}

fruit.update(["orange", "mango", "grapes"])

print(fruit)

# output :
# {'banana', 'apple', 'cherry'}
# banana
# apple
# cherry
# True
# False
# {'banana', 'orange', 'apple', 'cherry'}
# new :
# {'mango', 'banana', 'orange', 'apple', 'grapes', 'cherry'}

fruit = {'mango', 'banana', 'orange', 'apple', 'grapes', 'cherry'}

print(len(fruit))

# output :
# {'banana', 'apple', 'cherry'}
# banana
# apple
# cherry
# True
# False
# {'banana', 'apple', 'cherry', 'orange'}
# {'banana', 'orange', 'apple', 'cherry', 'mango', 'grapes'}
# new :
# 6

fruit = {'banana', 'orange', 'apple', 'cherry', 'mango', 'grapes'}

fruit.remove("banana")

print(fruit)

# output :
# {'apple', 'cherry', 'banana'}
# apple
# cherry
# banana
# True
# False
# {'apple', 'cherry', 'orange', 'banana'}
# {'grapes', 'orange', 'mango', 'banana', 'cherry', 'apple'}
# 6
# new :
# {'grapes', 'orange', 'mango', 'cherry', 'apple'}

fruit = {"apple", "banana", "cherry"}

fruit.discard("banana")

print(fruit)

# output :
# {'banana', 'cherry', 'apple'}
# banana
# cherry
# apple
# True
# False
# {'banana', 'cherry', 'orange', 'apple'}
# {'mango', 'cherry', 'grapes', 'orange', 'apple', 'banana'}
# 6
# {'mango', 'cherry', 'grapes', 'orange', 'apple'}
# new :
# {'cherry', 'apple'}

fruit = {"apple", "banana", "cherry"}

x = fruit.pop()

print(x) #removed item

print(fruit) #the set after removal

# output :
# {'apple', 'cherry', 'banana'}
# apple
# cherry
# banana
# True
# False
# {'apple', 'cherry', 'orange', 'banana'}
# {'grapes', 'apple', 'cherry', 'orange', 'mango', 'banana'}
# 6
# {'grapes', 'apple', 'cherry', 'orange', 'mango'}
# {'apple', 'cherry'}
# new :
# apple
# {'cherry', 'banana'}

fruit = {"apple", "banana", "cherry"}

fruit.clear()

print(fruit)

# output :
# {'banana', 'cherry', 'apple'}
# banana
# cherry
# apple
# True
# False
# {'banana', 'orange', 'cherry', 'apple'}
# {'orange', 'apple', 'mango', 'banana', 'cherry', 'grapes'}
# 6
# {'orange', 'apple', 'mango', 'cherry', 'grapes'}
# {'cherry', 'apple'}
# banana
# {'cherry', 'apple'}
# new :
# set()


# thisset = {"apple", "banana", "cherry"}

# del thisset

# print(thisset) #this will raise an error because the set no longer exists
# output :
# NameError: name 'thisset' is not defined

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)
