#program to add keys/values in a dictionary(update dictionary)
dict1={'a':1}
dict2={}
while True:
    key=input("enter the key:")
    if key=="done":
        break
    values=input("enter value:")
    dict2[key]=values
dict1.update(dict2)
print("after adding keys and values the dictionary is:",dict1)



