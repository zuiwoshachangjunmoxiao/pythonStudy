# -- coding:utf-8 --

ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there's not 10 things in that list, let's fix that."

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print "Adding: ", next_one
    stuff.append(next_one)
    print "There's %d items now." % len(stuff)
    
print "There we go: ", stuff

print "Let's do some things with stuff."

print stuff[1]
print stuff[-1] # whoa! fancy
# pop()函数，将list最后一个元素截取出来。
print stuff.pop()
print ' '.join(stuff) # what? cool!
# '#'.join(stuff[3:5])函数，表示以#作为分隔符，将stuff[3:5]连接成一个新的字符串 Telephone#Lig
# '#'.join()，也可以以其他符号作为分隔符，也可以为空（空格作为分隔符）
print '#'.join(stuff[3:5]) # super stellar!