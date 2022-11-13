import random

wall = 'STREET'
cell = 'ROAD'
unvisited = 'u'
height = 11
width = 27
maze = []

# Find number of surrounding cells
def surroundingCells(rand_wall):
    s_cells = 0
    if (maze[rand_wall[0]-1][rand_wall[1]] == 'ROAD'):
        s_cells += 1
    if (maze[rand_wall[0]+1][rand_wall[1]] == 'ROAD'):
        s_cells += 1
    if (maze[rand_wall[0]][rand_wall[1]-1] == 'ROAD'):
        s_cells +=1
    if (maze[rand_wall[0]][rand_wall[1]+1] == 'ROAD'):
        s_cells += 1

    return s_cells

def generate_city(height, width):
    # Denote all cells as unvisited
    for i in range(0, height):
        line = []
        for j in range(0, width):
            line.append(unvisited)
        maze.append(line)
    # Randomize starting point and set it a cell
    starting_height = int(random.random()*height)
    starting_width = int(random.random()*width)
    if (starting_height == 0):
        starting_height += 1
    if (starting_height == height-1):
        starting_height -= 1
    if (starting_width == 0):
        starting_width += 1
    if (starting_width == width-1):
        starting_width -= 1

    # Mark it as cell and add surrounding walls to the list
    maze[starting_height][starting_width] = cell
    walls = []
    walls.append([starting_height - 1, starting_width])
    walls.append([starting_height, starting_width - 1])
    walls.append([starting_height, starting_width + 1])
    walls.append([starting_height + 1, starting_width])

    # Denote walls in maze
    maze[starting_height-1][starting_width] = 'STREET'
    maze[starting_height][starting_width - 1] = 'STREET'
    maze[starting_height][starting_width + 1] = 'STREET'
    maze[starting_height + 1][starting_width] = 'STREET'
    while (walls):
        # Pick a random wall
        rand_wall = walls[int(random.random()*len(walls))-1]

        # Check if it is a left wall
        if (rand_wall[1] != 0):
            if (maze[rand_wall[0]][rand_wall[1]-1] == 'u' and maze[rand_wall[0]][rand_wall[1]+1] == 'ROAD'):
                # Find the number of surrounding cells
                s_cells = surroundingCells(rand_wall)

                if (s_cells < 2):
                    # Denote the new path
                    maze[rand_wall[0]][rand_wall[1]] = 'ROAD'

                    # Mark the new walls
                    # Upper cell
                    if (rand_wall[0] != 0):
                        if (maze[rand_wall[0]-1][rand_wall[1]] != 'ROAD'):
                            maze[rand_wall[0]-1][rand_wall[1]] = 'STREET'
                        if ([rand_wall[0]-1, rand_wall[1]] not in walls):
                            walls.append([rand_wall[0]-1, rand_wall[1]])


                    # Bottom cell
                    if (rand_wall[0] != height-1):
                        if (maze[rand_wall[0]+1][rand_wall[1]] != 'ROAD'):
                            maze[rand_wall[0]+1][rand_wall[1]] = 'STREET'
                        if ([rand_wall[0]+1, rand_wall[1]] not in walls):
                            walls.append([rand_wall[0]+1, rand_wall[1]])

                    # Leftmost cell
                    if (rand_wall[1] != 0):	
                        if (maze[rand_wall[0]][rand_wall[1]-1] != 'ROAD'):
                            maze[rand_wall[0]][rand_wall[1]-1] = 'STREET'
                        if ([rand_wall[0], rand_wall[1]-1] not in walls):
                            walls.append([rand_wall[0], rand_wall[1]-1])
                

                # Delete wall
                for wall in walls:
                    if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                        walls.remove(wall)

                continue

        # Check if it is an upper wall
        if (rand_wall[0] != 0):
            if (maze[rand_wall[0]-1][rand_wall[1]] == 'u' and maze[rand_wall[0]+1][rand_wall[1]] == 'ROAD'):

                s_cells = surroundingCells(rand_wall)
                if (s_cells < 2):
                    # Denote the new path
                    maze[rand_wall[0]][rand_wall[1]] = 'ROAD'

                    # Mark the new walls
                    # Upper cell
                    if (rand_wall[0] != 0):
                        if (maze[rand_wall[0]-1][rand_wall[1]] != 'ROAD'):
                            maze[rand_wall[0]-1][rand_wall[1]] = 'STREET'
                        if ([rand_wall[0]-1, rand_wall[1]] not in walls):
                            walls.append([rand_wall[0]-1, rand_wall[1]])

                    # Leftmost cell
                    if (rand_wall[1] != 0):
                        if (maze[rand_wall[0]][rand_wall[1]-1] != 'ROAD'):
                            maze[rand_wall[0]][rand_wall[1]-1] = 'STREET'
                        if ([rand_wall[0], rand_wall[1]-1] not in walls):
                            walls.append([rand_wall[0], rand_wall[1]-1])

                    # Rightmost cell
                    if (rand_wall[1] != width-1):
                        if (maze[rand_wall[0]][rand_wall[1]+1] != 'ROAD'):
                            maze[rand_wall[0]][rand_wall[1]+1] = 'STREET'
                        if ([rand_wall[0], rand_wall[1]+1] not in walls):
                            walls.append([rand_wall[0], rand_wall[1]+1])

                # Delete wall
                for wall in walls:
                    if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                        walls.remove(wall)

                continue

        # Check the bottom wall
        if (rand_wall[0] != height-1):
            if (maze[rand_wall[0]+1][rand_wall[1]] == 'u' and maze[rand_wall[0]-1][rand_wall[1]] == 'ROAD'):

                s_cells = surroundingCells(rand_wall)
                if (s_cells < 2):
                    # Denote the new path
                    maze[rand_wall[0]][rand_wall[1]] = 'ROAD'

                    # Mark the new walls
                    if (rand_wall[0] != height-1):
                        if (maze[rand_wall[0]+1][rand_wall[1]] != 'ROAD'):
                            maze[rand_wall[0]+1][rand_wall[1]] = 'STREET'
                        if ([rand_wall[0]+1, rand_wall[1]] not in walls):
                            walls.append([rand_wall[0]+1, rand_wall[1]])
                    if (rand_wall[1] != 0):
                        if (maze[rand_wall[0]][rand_wall[1]-1] != 'ROAD'):
                            maze[rand_wall[0]][rand_wall[1]-1] = 'STREET'
                        if ([rand_wall[0], rand_wall[1]-1] not in walls):
                            walls.append([rand_wall[0], rand_wall[1]-1])
                    if (rand_wall[1] != width-1):
                        if (maze[rand_wall[0]][rand_wall[1]+1] != 'ROAD'):
                            maze[rand_wall[0]][rand_wall[1]+1] = 'STREET'
                        if ([rand_wall[0], rand_wall[1]+1] not in walls):
                            walls.append([rand_wall[0], rand_wall[1]+1])

                # Delete wall
                for wall in walls:
                    if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                        walls.remove(wall)


                continue

        # Check the right wall
        if (rand_wall[1] != width-1):
            if (maze[rand_wall[0]][rand_wall[1]+1] == 'u' and maze[rand_wall[0]][rand_wall[1]-1] == 'ROAD'):

                s_cells = surroundingCells(rand_wall)
                if (s_cells < 2):
                    # Denote the new path
                    maze[rand_wall[0]][rand_wall[1]] = 'ROAD'

                    # Mark the new walls
                    if (rand_wall[1] != width-1):
                        if (maze[rand_wall[0]][rand_wall[1]+1] != 'ROAD'):
                            maze[rand_wall[0]][rand_wall[1]+1] = 'STREET'
                        if ([rand_wall[0], rand_wall[1]+1] not in walls):
                            walls.append([rand_wall[0], rand_wall[1]+1])
                    if (rand_wall[0] != height-1):
                        if (maze[rand_wall[0]+1][rand_wall[1]] != 'ROAD'):
                            maze[rand_wall[0]+1][rand_wall[1]] = 'STREET'
                        if ([rand_wall[0]+1, rand_wall[1]] not in walls):
                            walls.append([rand_wall[0]+1, rand_wall[1]])
                    if (rand_wall[0] != 0):	
                        if (maze[rand_wall[0]-1][rand_wall[1]] != 'ROAD'):
                            maze[rand_wall[0]-1][rand_wall[1]] = 'STREET'
                        if ([rand_wall[0]-1, rand_wall[1]] not in walls):
                            walls.append([rand_wall[0]-1, rand_wall[1]])

                # Delete wall
                for wall in walls:
                    if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                        walls.remove(wall)

                continue

        # Delete the wall from the list anyway
        for wall in walls:
            if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                walls.remove(wall)

    # Mark the remaining unvisited cells as walls
    for i in range(0, height):
        for j in range(0, width):
            if (maze[i][j] == 'u'):
                maze[i][j] = 'STREET'

    for i in range(1, height-1):
        for j in range(1, width-1):
            count = 0
            if maze[i][j] == 'STREET':
                count = 0
                if maze[i-1][j] == 'ROAD' and maze[i+1][j] == 'ROAD' and  maze[i][j+1] == 'STREET' and maze[i][j-1] == 'STREET':
                    maze[i][j] = 'ROAD'
                elif maze[i-1][j] == 'STREET' and maze[i+1][j] == 'STREET' and maze[i][j+1] == 'ROAD' and maze[i][j-1] == 'ROAD':
                    maze[i][j] = 'ROAD'
    return maze



 
ROADS = ['ROAD', 'START', 'END']

intersections = []

adj_list = {}
 
def find_intersections(entry, exit, maze):
    intersections.append(entry)
    intersections.append(exit)
    for i in range(1, height-1):
        for j in range(1, width-1):
            count = l = r = u = d = 0
            if maze[i][j] in ROADS:
                if  maze[i-1][j] in ROADS:
                    count += 1
                    u = 1
                if  maze[i+1][j] in ROADS:
                    count += 1
                    d = 1
                if  maze[i][j+1] in ROADS:
                    count += 1
                    r = 1
                if  maze[i][j-1] in ROADS:
                    count += 1
                    l = 1
                if count >= 3: #for intersections
                    intersections.append((i,j))
                if count == 2: #for turns
                    if (d == 1 and r == 1 and u == 0 and l == 0):
                        intersections.append((i,j))
                    if (d == 0 and r == 1 and u == 1 and l == 0):
                        intersections.append((i,j))
                    if (d == 0 and r == 0 and u == 1 and l == 1):
                        intersections.append((i,j))
                    if (d == 1 and r == 0 and u == 0 and l == 1):
                        intersections.append((i,j))
    return intersections
 
def adj_list_m(intersections, maze):
    for intersection in intersections:
        adj_list[intersection] = []

    for x in range(0, len(intersections)):  
        check = intersections[x]
        count = 0
        for j in range (check[1] + 1, width-1): #going right
            count += 1
            if (maze[check[0]][j] in ROADS):
                for y in range(0, len(intersections)):
                    if (check[0], j) == intersections[y]:
                        safety_data = {}
                        safety_data['safety_score'] = 10
                        # print(((check[0], j), count, safety_data))
                        adj_list[check].append(((check[0], j), count, safety_data))
        count = 0
        for j in range (check[1]-1, 0, -1): #going left
            count += 1
            if (maze[check[0]][j] in ROADS):
                for y in range(0, len(intersections)):
                    if (check[0], j) == intersections[y]:
                        safety_data = {}
                        safety_data['safety_score'] = 10
                        adj_list[check].append(((check[0], j), count, safety_data))
        count = 0
        for i in range (check[0]-1, 0, -1): #going up
            count += 1
            if (maze[i][check[1]] in ROADS):
                for y in range(0, len(intersections)):
                    if (i, check[1]) == intersections[y]:
                        safety_data = {}
                        safety_data['safety_score'] = 10
                        adj_list[check].append (((i, check[1]), count, safety_data))
        count = 0
        for i in range (check[0]+1, height): #going down
            count += 1
            if (maze[i][check[1]] in ROADS):
                for y in range(0, len(intersections)):
                    if (i, check[1]) == intersections[y]:
                        safety_data = {}
                        safety_data['safety_score'] = 10
                        adj_list[check].append (((i, check[1]), count, safety_data))
        
    return adj_list
 
def adjacency_list(maze, start, end):
    intersections = find_intersections(start, end, maze)
    return adj_list_m(intersections, maze)
 



from collections import defaultdict 
import heapq

class Graph:
    
    def __init__(self, V):
        '''
        Instantiate the Graph with the number of vertices of the graph.
        '''
        self.graph = defaultdict(list)
        self.V = V

    def addEdge(self, u, v, w):

        '''
        The Graph will be undirected and assumed to have positive weights.
        Dijkstra's algorithm fails when negative weights are introduced.
        '''
        self.graph[u].append([v, w])
        self.graph[v].append([u,w])

    def minDistance(self, dist, seen):
        min_d = float('inf')

        for v in range(self.V):
            if v not in seen and dist[v] < min_d:
                min_d = dist[v]
                min_vertex = v
        return min_vertex
    
    # def slow_dijkstra(self,source):
    #     dist = [float('inf')] * self.V
    #     seen = set()
    #     dist[source] = 0

    #     for _ in range(self.V):
    #         u = self.minDistance(dist, seen)
    #         seen.add(u)

    #         for node, weight in self.graph[u]:
    #             if node not in seen and dist[node] > dist[u] + weight:
    #                 dist[node] = dist[u] + weight

    #     self.printSolution(dist)


    def dijkstra_search(self, source, intersections):
        predecessor = {}

        dist = {}
        for intersection in intersections:
            dist[intersection] = float('inf')
        seen = set()
        heap = []
        dist[source] = 0

        heapq.heappush(heap, (source, dist[source]))

        while len(heap) > 0:
            node, weight = heapq.heappop(heap)
            seen.add(weight)

            for conn, w in self.graph[node]:
                if conn not in seen:
                    d = weight + w
                    if d < dist[conn]:
                        dist[conn] = d
                        heapq.heappush(heap, (conn, d))
                        predecessor[conn] = node
        
        return predecessor

    
    def printGraph(self):
        print(self.graph)

    def printSolution(self, dist, intersections):
        print('Vertex: \tDistance:')
        for node in intersections:
            print(node, '\t\t\t', dist[node])

    def send_params(self, al,intersections):
        for i in range (0, len(intersections)):
            temp_list = al[intersections[i]]
            for j in range (0, len(temp_list)):
                self.addEdge (intersections[i], temp_list[j][0], temp_list[j][1])


def init_graph(adj_list, intersections):
    G = Graph(len(intersections))
    G.send_params(adj_list, intersections)
    return G


# def printShortestPath(source, dest):
#     print("from: ", source)
#     print("to: ", dest)

#     predecessors = init_graph().dijkstra(source, intersections)

#     pred = dest
#     while pred != source:
#         print(pred, '<==', end=' ')
#         pred = predecessors[pred]
#     print(source)
# printShortestPath(intersections[0], intersections[-1])



def dijkstra(adj_list, start):
    intersections = []
    # intersections = adj_list.keys()
    for key in adj_list.keys():
        intersections.append(key)
    return init_graph(adj_list, intersections).dijkstra_search(start, intersections)

# def get_route_coordinates(maze, start, end):
#     route_coords = []
#     intersections = find_intersections (start, end, maze)
#     adj_list = adj_list_m (intersections, maze)
#     preds = dijkstra(adj_list, start)
#     temp1 = end
#     while preds[temp1] != start:
#         route_coords.append(temp1)
#         temp2 = preds[temp1]
#         if (temp1[0] == temp2[0]):
#             distance = temp1[1] - temp2[1]
#             if distance < 0: #moving right
#                 for j in range (temp1[1], temp2[1]+1):
#                     route_coords.append((temp1[0], j))
#             else: #moving left
#                 for j in range (temp1[1], temp2[1]-1, -1):
#                     route_coords.append((temp1[0], j))
#         else:
#             distance = temp1[0] - temp2[0]
#             if distance < 0: #moving up
#                 for i in range (temp1[0], temp2[0]-1, -1):
#                     route_coords.append((i, temp1[1]))
#             else:
#                 for i in range (temp1[0], temp2[0]+1):
#                     route_coords.append((i, temp1[1]))
#         temp1 = temp2
#     route_coords.append (start)
#     return route_coords

# maze = generate_city(30, 30)
# intersections = find_intersections((1, 1), (10, 10), maze)
# print(adj_list_m(intersections, maze))
# #print (dijkstra (adj_list_m(intersections, maze), intersections[0]))

# print(get_route_coordinates(generate_city(30,30),(1,1),(10,10)))