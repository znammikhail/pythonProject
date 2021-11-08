from collections import deque

def person_is_seller(name):
    return len(str(name)) == 3

def search():     # поиск в ширину. сначала нужно составить словарь в виде графа. потом пользуемся очередью(queue)
    search_queue = deque()
    search_queue += graph['I']
    searched = [] # уже просмотренных сюда
    while search_queue:
        person = search_queue.popleft() # смотрим первого(аналогия со стеком)
        if not person in searched:
            if person_is_seller(person):
                print(str(person) + ' первое трехзначное число')
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False

graph = dict()

graph['I'] = [1,2,3]
graph[1] = [12,13]
graph[2] = [22]
graph[3] = [31]
graph[12] = [123]
graph[13] = []
graph[22] = []
graph[31] = []
graph[123] = []


search()

