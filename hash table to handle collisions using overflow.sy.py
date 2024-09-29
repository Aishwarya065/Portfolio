def display_hash(hashTable):
    for i in range(len(hashTable)):
        print(i, end="")
        for j in hashTable[i]:
            print("-->", end="")
            print(j, end="")
        print()  # Move print() outside the inner loop to ensure each bucket prints on a new line

# Creating Hashtable as a nested list
HashTable = [[] for _ in range(10)]

def Hashing(keyvalue):
    return keyvalue % len(HashTable)

def insert(Hashtable, keyvalue, value):
    hash_key = Hashing(keyvalue)
    Hashtable[hash_key].append(value)

# Driver Code
insert(HashTable, 10, 'Gujrat')
insert(HashTable, 25, 'Mumbai')
insert(HashTable, 20, 'Mathura')
insert(HashTable, 9, 'Delhi')
insert(HashTable, 21, 'Pune')
insert(HashTable, 21, 'Noida')

display_hash(HashTable)


