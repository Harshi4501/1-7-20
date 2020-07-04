#program to remove items from the dictionary
dict1={}
print("enter key and values:")
print('!!!enter done twice to stop !!!')
while True:
    key=input('enter key:')
    value=input('enter value:')
    if key=='done' or value=='done':
        break
    dict1[key]=value
    
print("before removing the item the dictionary is:",dict1)
print('!!!enter done to stop entering key!!!:')
while True:
    key=input('enter key element of item to be deleted:')
    if key=='done':
        break
    del dict1[key]
print("after removing the items the dictionary is:",dict1)