def wordFreq(input):
    punc = ",.!?;:/@#$%^&*({)}]["
    input = input.lower()
    for let in input:
        if let in punc:
            input = input.replace(let, "")
    test = input.split()
    store = {}
    for word in test: 
        if word in store.keys():
            store[word] += 1
        else:
            store[word] = 1
    store_values = sorted(store.values(), reverse=True)
    new_store = {}
    for i in store_values:
        for j in sorted(store.keys()):
            if store[j] == i:
                new_store[j] = store[j]          
    for val in new_store:
        print(val, new_store[val])

