# python3

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]

def write_responses(result):
    print('\n'.join(result))


def process_queries(queries, contacts):
    result = []
    # Keep list of all existing (i.e. not deleted yet) contacts.

    for cur_query in queries:
        if cur_query.type == 'add':
            # if we already have contact with such number,
            # we should rewrite contact's name
            contacts[cur_query.number] = cur_query.name
            
            
        elif cur_query.type == 'del':
            contacts[cur_query.number] = None

            
        else:
            response = 'not found' if not contacts[cur_query.number] else contacts[cur_query.number]
            
            result.append(response)
    return result

if __name__ == '__main__':
    contacts = [None for i in range(10**7)]
    write_responses(process_queries(read_queries(), contacts))

# 12
# add 911 police
# add 76213 Mom
# add 17239 Bob
# find 76213
# find 910
# find 911
# del 910
# del 911
# find 911
# find 76213
# add 76213 daddy
# find 76213