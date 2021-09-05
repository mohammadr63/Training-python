def list_sort( lst ):
    lst.sort()
    print( "Sorted List is: ", lst )
# output :
# Sorted List is:  [15, 18, 21, 27, 36]


mylist = [21, 15, 36, 18, 27]
list_sort( mylist )
print( mylist )

# output :
# [15, 18, 21, 27, 36]

def average( *vals ):
    total = 0
    for val in vals:
        total += val
    return total/len(vals)  
average(5)
# 5.0
average(1, 2, 3, 4, 5)
# 3.0
average(1, 3, 5, 7, 9, 11, 13, 15)
# 8.0