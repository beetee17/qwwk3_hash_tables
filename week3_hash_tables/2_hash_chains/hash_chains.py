# python3

class Query:

    def __init__(self, query):
        self.type = query[0]
        self.s = query[1]


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        # store all strings in one list
        self.elems = [[] for i in range(bucket_count)]

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def write_search_result(self, was_found):
        print('yes' if was_found else 'no')

    def write_chain(self, chain):
        print(' '.join(chain))

    def read_query(self):
        # print(input().split())
        return Query(input().split())

    def process_query(self, query):
        # print(query,type, query.s)
        if query.type == "check":
            
            ind = int(query.s)
   
         
            self.write_chain(cur for cur in self.elems[ind])
            return
        
        _hash = self._hash_func(query.s)
      
        chain = self.elems[_hash]
      
        
        # ind will be -1 if query not in hash table
        ind = -1

        if chain:
            for i in range(len(chain)):
                if chain[i] == query.s:
                    ind = i

        if query.type == 'find':
            self.write_search_result(ind != -1)

        elif query.type == 'add':
            # This hash table does not allow duplicate entries 
            # i.e adding 'test' twice is the same as adding it once
            if ind == -1:
                # insert into beginning of chain
                if len(chain) > 0:
                   
                    self.elems[_hash] = [query.s] + self.elems[_hash]

                else:
                   
                    self.elems[_hash] = [query.s]
                       
        else:
            if ind != -1:
                self.elems.pop(ind)

    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())

if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()

# 5 
# 12
# add world
# add HellO
# check 4
# find World
# find world
# del world
# check 4
# del HellO
# add luck
# add GooD
# check 2
# del good