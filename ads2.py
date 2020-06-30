import time, math, heapq, random

CITY_NUM = 10

neighbours= [[] for i in range(CITY_NUM)]
distances = [None for i in range(CITY_NUM)]
distances_from_start = [None for i in range(CITY_NUM)]
cities = []
bfs_distance = [None for i in range(CITY_NUM)]
dfs_reach = [None for i in range(CITY_NUM)]

method_distances = [[0 for i in range(CITY_NUM)] for j in range(CITY_NUM)]
minimum = []
town = []
rep = []
greedyVisited= []


class city:
    def __init__(self, id=0, dist=0, x=0, y=0):
        self.id=id
        self.dist=dist
        self.x=x
        self.y=y
    def __gt__(self, node):
        return self.dist > node.dist

    def __eq__(self,node):
        return self.id == node.id

    def __ne__(self, node):
        return self.id != node.id

class Edge:
    def __init__(self, to=None, dist=None):
        self.to = to
        self.dist = dist

    def __lt__(self, edge):
        if self.dist == None or edge.dist == None:
            return "NONE"
        return self.dist<edge.dist


def get_distance( start,finish):
    return math.sqrt((start.x-finish.x)**2 + (start.y - finish.y)**2)


def intersecting(start_visit, visit_finish):
    global CITY_NUM
    for i in range(CITY_NUM):
        if (start_visit[i] and visit_finish[i]):
            return i
        return -1

def printroute(startparent,finishparent,start,finish,intersectcity):
    route = []
    route.append(intersectcity)
    i = intersectcity
    while(i != start):
        route.append(startparent[i])
        i = startparent[i]
    route.reverse()
    i = intersectcity
    while(i!= finish):
        route.append(finishparent[i])
        i = finishparent[i]
    print("Route: ", end =" ")
    for it in route:
        print(it, end = " ")
    print()

def BFS_util(start, target):
    global CITY_NUM

    start_visited = [None for i in range(CITY_NUM)]
    to_visited = [None for i in range(CITY_NUM)]
    start_parent = [None for i in range(CITY_NUM)]
    to_parent = [None for i in range(CITY_NUM)]
    startdist = [None for i in range(CITY_NUM)]
    todist = [None for i in range(CITY_NUM)]

    intersect_city = -1
    start_q = to_q = []

    for i in range(CITY_NUM):
        start_visited[i] = False
        to_visited[i] = False

    heapq.heappush(start_q, start)
    start_visited[start.id] = True

    start_parent[start.id] = -1

    heapq.heappush(to_q, target)
    to_visited[target.id] = True

    to_parent[target.id] = -1

    for i in range(CITY_NUM):
        startdist[i] = float("inf")
        todist[i] = float("inf")

    startdist[start.id] = 0
    todist[target.id] = 0
    while (start_q and to_q):
        start_q, start_visited, start_parent, startdist = bfs_loop(start_q, start_visited, start_parent, startdist)
        intersect_city = intersecting(start_visited, to_visited)
        if intersect_city == -1:
            to_q, to_visited, to_parent, todist = bfs_loop(to_q, to_visited, to_parent, todist)
        intersect_city = intersecting(start_visited, to_visited)
        if intersect_city != -1:
            printroute(start_parent, to_parent, start.id, target.id, intersect_city)
            return True
    return False

def bfs_loop(q,visited,parent,distance):
    city = heapq.heappop(q)
    for edge in neighbours[city.id]:
        if not visited[edge.to.id]:
            parent[edge.to.id] = city.id
            visited[edge.to.id] = True
            heapq.heappush(q, edge.to)
        if distance[edge.to.id] > city.dist + edge.dist:
            distance[edge.to.id] = city.dist + edge.dist
            parent[edge.to.id] = city.id
            visited[edge.to.id] = True
            heapq.heappush(q, edge.to)
    return q, visited, parent, distance

def dijkstra_util(start):
    global distances,cities,neighbours
    for i in range(CITY_NUM):
        distances[i] = float("inf")

    distances[start] = 0
    cities[start].dist = 0
    q = []
    heapq.heappush(q, cities[start])

    while (q):
        node = heapq.heappop(q)
        if distances[node.id] != node.dist:
            continue
        for edge in neighbours[node.id]:
            if distances[edge.to.id] > node.dist+edge.dist:
                distances[edge.to.id] = node.dist+edge.dist
                heapq.heappush(q, city(edge.to.id, distances[edge.to.id], edge.to.x, edge.to.y))

def dijkstra_algorithm(start,target):
    global distances_from_start
    dijkstra_util(start.id)
    for i in range(CITY_NUM):
        distances_from_start[i] = distances[i]

    dijkstra_util(target.id)
    print ("Shortest route: ",end = "")
    for j in range(CITY_NUM):
        if distances_from_start[j] + distances[j] == distances_from_start[target.id]:
            print(j, end=" ")

    print("Distance: " + str(distances_from_start[target.id]))
def bfs(start):
    global bfs_distance
    for i in range(CITY_NUM):
        bfs_distance[i] = float("inf")
    bfs_distance[start.id] = 0
    start.dist = 0
    q = []
    heapq.heappush(q, start)

    while (q):
        node = heapq.heappop(q)
        if (bfs_distance[node.id] != node.dist):
            continue
        for edge in neighbours[node.id]:
            if bfs_distance[edge.to.id] > node.dist+edge.dist:
                bfs_distance[edge.to.id] = node.dist+edge.dist
                heapq.heappush(q, city(edge.to.id, bfs_distance[edge.to.id], edge.to.x, edge.to.y))


def nextPermutation(L):
    n = len(L)

    i = n - 2
    while i >= 0 and L[i] >= L[i + 1]:
        i -= 1

    if i == -1:
        return False

    j = i + 1
    while j < n and L[j] > L[i]:
        j += 1
    j -= 1

    L[i], L[j] = L[j], L[i]
    left = i + 1
    right = n - 1

    while left < right:
        L[left], L[right] = L[right], L[left]
        left += 1
        right -= 1
    return True

def dfs(city):
    global dfs_reach
    dfs_reach[city.id]= True
    for edge in neighbours[city.id]:
        if not dfs_reach[edge.to.id]:
            dfs(edge.to)


def BFS_DFS_METHOD(start):

    dfs(start)
    for i in dfs_reach:
        if not i:
            print("Not all cities are connected")
            return False
    for i in cities:
        bfs(i)
        for j in range(CITY_NUM):
            method_distances[i.id][j] = bfs_distance[j]

    vertex = []
    for i in range(CITY_NUM):
        if i is not start.id:
            vertex.append(i)

    minRoute = path = ""

    minPath = float("inf")

    while True:

        current_weight = 0
        k = start.id
        path = ""
        for i in vertex:
            current_weight += method_distances[k][i]
            k = i
            path += str(k)
            path += " "
        current_weight += method_distances[k][start.id]
        if (minPath > current_weight):
            minPath = current_weight
            minRoute = str(start.id)
            minRoute += " "
            minRoute += path
            minRoute += str(start.id)
        if nextPermutation(vertex):
            break
    print("BFS cost:", minPath)
    return True

def find_Rep(city):
    global rep
    if (city == rep[city.id]):
        return city
    rep[city.id] = find_Rep(rep[city.id])
    return rep[city.id]

def union_rep(city,edge):
    if find_Rep(city) != find_Rep(edge.to):
        print(city.id, " ", edge.to.id, " ", edge.dist)
    rep[find_Rep(city).id] = find_Rep(edge.to)

def greedMethod(node, endCity, currentCost=0):
    global distances
    minPath = float("inf")
    minId = -1
    for i in range(CITY_NUM):
        if (i != node.id and i !=endCity.id):
            if (minPath>method_distances[node.id][i] and cities[i] not in greedyVisited):
                minPath= method_distances[node.id][i]
                minId = i

    if(minId<0):
        greedyVisited.append(endCity)
        return currentCost+method_distances[node.id][endCity.id]
    currentCost += method_distances[node.id][minId]
    next = cities[minId]
    greedyVisited.append(next)
    return greedMethod(next, endCity, currentCost)

def TSM(start):
    if (BFS_DFS_METHOD(start)):
        pass
    print("Greedy cost: ", greedMethod(start, start))
    print("Greedy path: ", start.id, end = " ")
    for i in greedyVisited:
        print(i.id, end=" ")
    print()

radius = 100
for i in range(CITY_NUM):
    cities.append(city(i, 0, random.randint(-radius, radius), random.randint(-radius, radius)))
    #print(cities[-1].id, "= (", cities[-1].x, ",", cities[-1].y, ")")

print("1. EVERY CITY IS CONNECTED DIRECTLY")
print("2. SOME OF ROADS ARE LOCKED")
choice = int(input())

while(choice != 1 and choice !=2):
    choice = int(input())
probability = 20

for i in cities:
    for j in cities:
        if (j.id > i.id):
            if choice == 1:
                neighbours[i.id].append(Edge(j, get_distance(i, j)))
                neighbours[j.id].append(Edge(i, get_distance(i, j)))
                #print(i.id, "\t", j.id, "\t", get_distance(i, j))
            else:
                if random.randint(0,100) > probability:
                    neighbours[i.id].append(Edge(j, get_distance(i, j)))
                    neighbours[j.id].append(Edge(i, get_distance(i, j)))
                    #print(i.id, "\t", j.id, "\t", get_distance(i, j))
cityStart = 0
last = CITY_NUM - 1
TSM(cities[cityStart])

print("From", cityStart, "to", last)
if (BFS_util(cities[cityStart], cities[last])):
    dijkstra_algorithm(cities[cityStart], cities[last])