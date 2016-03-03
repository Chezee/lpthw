def new(num_bucket=256):                                                                  #Number of buckets
    aMap = []                                                                             #Making of array
    for i in range(0, num_bucket):                                                        #Making cells for hashes
        aMap.append([])
    return aMap
    
def hash_key(aMap, key):
    return hash(key) % len(aMap)                                                          #Counting cell
    
def get_bucket(aMap, key):
    bucket_id = hash_key(aMap, key)
    return aMap[bucket_id]
    
def get_slot(aMap, key, default=None):
    bucket = get_bucket(aMap, key)
    
    for i, kv in enumerate(bucket):
        k, v = kv
        if key == k:
            return i, k, v
    return -1, key, default
            
def get(aMap, key, default=None):
    i, k, v = get_slot(aMap, key, default=default)
    return v
    
def set(aMap, key, value):
    bucket = get_bucket(aMap, key)
    i, k, v = get_slot(aMap, key)
    
    if i >= 0:
        bucket[i] = (key, value)
    else:
        bucket.append((key, value))
        print bucket
        
def delete(aMap, key):
    bucket = get_bucket(aMap, key)
    
    for i in xrange(len(bucket)):
        k, v = bucket[i]
        if key == k:
            del bucket[i]
            break
            
def list(aMap):
    for bucket in aMap:
        if bucket:
            for k, v in bucket:
                print k, v
                
print hash_key