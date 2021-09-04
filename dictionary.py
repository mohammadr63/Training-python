person  = {
    "name": "mohammad",
    "job": "Programming",
    "car": "BMW x6",
    "age": 14,
    "code": 134
}
# and :

person = dict( name="mohammad", job="Programming", car="BMW x6", age=14, code=134 )

print( "Name: " + person["name"] )
# output :
# Name: mohammad

print( "Name: " + person.get("name") )

# output: Name: mohammad

info = {'name': 'omid', 'job': 'programmer', 'code': 177}
print( info['name'] )
# print( info['family'] )

# output :
# omid
# KeyError: 'family'

print( info['name'] )
print( info['job'] )
print( info['code'] )
# output :
# Name: mohammad
# Name: mohammad
# omid
# omid
# programmer
# 177


