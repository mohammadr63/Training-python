tpl = ("this", "is", "a", "test", "for", "tuples!")
print( tpl[2] )

# output :
# a

print( tpl[-4] )

# output :
# a

tpl = ("this", "is", "a", "test", "for", "tuples!")
print( tpl[1:5] )

# output :
# ('is', 'a', 'test', 'for')

print( tpl[2:-1] )

# output :
# ('a', 'test', 'for')

print( tpl[-5:-1] )

# output :
# ('is', 'a', 'test', 'for')

print( tpl[-4:4] )

# output :
# ('a', 'test')

tuple1 = ( "Test", "Element" )
tuple2 = ( 11, 37, 23 )
tuple3 = tuple1 + tuple2

print( tuple3 )

# output :
# ('Test', 'Element', 11, 37, 23)



tpl = ("Sara", "Elham", "Mohsen", "Omid")
len( tpl ) # 4



tuple1 = ( "Test", "Element" )
tuple2 = ( 11, 37, 23 )
tuple3 = tuple1[1:] + tuple2[:-1]
print( tuple3 )

# output :
# ('Element', 11, 37)


tpl = ("Sabz", "Danesh")
print( tpl*3 )
# output :
# ('Sabz', 'Danesh', 'Sabz', 'Danesh', 'Sabz', 'Danesh')

tpl = (17, 25, 32, 37, 42, 50)
print( 32 in tpl ) #True
print( 35 in tpl ) #False