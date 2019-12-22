# demonstrate hashtable usage


# create a hashtable all at once
myItems = dict({"key1" : 1, "key2" : 2, "key3" : "banana!"})
print(myItems)

# create a hashtable progressively
yourItems = {}
yourItems["key1"] = 1
yourItems["key2"] = "bananaa!"
yourItems["key3"] = 2
print(yourItems)

# try to access a nonexistent key
#print(myItems["key5"])

# replace an item
yourItems["key3"] = 3
print(yourItems)

# iterate the keys and values in the dictionary
for key, value in yourItems.items():
    print("key: ", key + " value: ", value)