import json

def get_pairs(lst:list)->dict:
    count = {}
    for i in range(len(lst)-1):
        pair = lst[i],lst[i+1]
        count[pair] = count.get(pair,0) + 1 

    return count

def get_merges(lst:list,pair:dict,idx:int)->list:
    new_ls = []
    i=0 
    while i < (len(lst)):
        if i < len(lst) -1 and (lst[i],lst[i+1]) == pair:
            new_ls.append(idx)
            i+=2
        else:
            new_ls.append(lst[i])
            i+=1

    return new_ls



if __name__ == "__main__":

    with open("taylorswift.txt","r",encoding="utf-8") as file:
        content = file.read()

    text = content
    text = text.encode("utf-8")
    tokens = list(map(int,text))
    vocab_size = 1024
    NUM_MERGES_TO_MAKE = vocab_size - 256
    ids = list(tokens) #making a copy 

    merges = {}
    vocab = {}

    for i in range(NUM_MERGES_TO_MAKE):
        stats = get_pairs(ids)
        top_max_pair = max(stats,key=stats.get)
        idx = 256+i
        print(f'Merging for Pair{top_max_pair}its new id ->{idx}')
        ids = get_merges(ids,top_max_pair,idx)
        merges[top_max_pair] = idx
    
    #create a vocab from the merges 
    #tokenID ->Byte Seq
    
    for idx in range(256):
        vocab[idx] = bytes([idx])

    for (b1,b2),idx in merges.items():
        vocab[idx] = vocab[b1]+vocab[b2]

    #Json friendly format 
    json_vocab = {
        str(k): list(v)   # bytes → [0..255]
        for k, v in vocab.items()
    }
    
    with open("Vocab.json","w") as f:
        json.dump(json_vocab,f,indent=2)
