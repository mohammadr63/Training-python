
print('welcom')

name = input('please enter  your name ? >')
print(' Hi , {}'.format(name))
import time
i = int(input('{} enter your number to finish ? >'.format(name)))
while i:
    print(i)
    time.sleep(1)
    i -= 1 #i = i-1
print("At the end i equals {}".format(i))
# output:
# 20
# 19
# 18
# 17
# 16
# 15
# 14
# 13
# 12
# 11
# 10
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1
# At the end i equals 0

i = int(input('{} Select a number to get started ?'.format(name)))
while i:
    print(i)
    time.sleep(1)
    i += 1 #i = i+1
print("At the end i equals {}".format(i))
#unlimited




 
