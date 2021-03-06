
# python3

class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        # store all strings in one list
        self.elems = [0] * bucket_count 
        for i in range(bucket_count):
            self.elems[i] = [] 

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
        return Query(input().split())

    def process_query(self, query):
        
        if query.type == "check":
            # use reverse order, because we append strings to the end
            self.write_chain(reversed(self.elems[query.ind]))
        else:
            try:
                ind = self._hash_func(query.s)
            except ValueError:
                ind = -1
            if query.type == 'find':
                if query.s in self.elems[ind]:
                    print('yes')
                else:
                    print('no')
            elif query.type == 'add':
                if query.s not in self.elems[self._hash_func(query.s)]:
                    self.elems[self._hash_func(query.s)].append(query.s)
            else:
                if ind != -1:
                    try:
                        xInd = self.elems[ind].index(query.s)
                    except ValueError:
                        xInd = -1
                    if xInd > -1: 
                        self.elems[ind].pop(xInd)

    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())

if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()
