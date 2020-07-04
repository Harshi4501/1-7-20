#program to demonstrate accessing an element from a Dictionary
dict1={}
print("enter key and values:")
print('!!!enter done twice to stop !!!')
while True:
    key=input('enter key:')
    value=input('enter value:')
    if key=='done' or value=='done':
        break
    dict1[key]=value
key1=input('enter key element to be accessed:')
if key1 in dict1:
    print('element is ',dict1[key1])
else:
    print('element not found')



