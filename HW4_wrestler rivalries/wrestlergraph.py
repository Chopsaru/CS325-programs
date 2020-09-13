class Vertex:
    def __init__(self, name, rivalries):
        self.name = name
        self.rivals = []
        self.team = 0; # 1 for babyface, 2 for heel, 0 for none
        for i in rivalries:
            for r in i:
                if (r not in self.rivals) and (self.name in i):
                    self.rivals.append(r)
        if self.name in self.rivals:
            self.rivals.remove(self.name)

def isBipartite(graph):
    visited = []
    queue = []
    heels = []
    babyfaces = []
    for vertex in graph:
        if graph[vertex].name not in visited:

            queue.append(graph[vertex].name)
            graph[vertex].team = 1
            babyfaces.append(graph[vertex].name)

            while queue:
                node = queue.pop(0)
                if node not in visited:
                    visited.append(node)
                    rivals = graph[node].rivals

                    for rival in rivals:
                        if graph[node].team == graph[rival].team:
                            return 'Impossible'
                        elif graph[rival].team == 0:
                            if graph[node].team == 1:
                                graph[rival].team = 2
                                if graph[rival].name not in heels:
                                    heels.append(graph[rival].name)
                            elif graph[node].team == 2:
                                graph[rival].team = 1
                                if graph[rival].name not in babyfaces:
                                    babyfaces.append(graph[rival].name)
                        queue.append(rival)

    result = "Yes Possible \n" + "Babyfaces: " + str(babyfaces) + "\n" + "Heels: " + str(heels) + "\n"
    return result


# Open data file
inFile = input("Enter the input file including extension: ")
data = open(inFile)

# Create a list of lists to be sorted
master_list = []

graph = {}

# import from file
for line in data:
    master_list.append(list(map(str, line.split())))

# parse wrestlers data from masterlist
numWresters = int(master_list[0][0])
wrestlers = [];
for i in range(1, numWresters + 1):
    wrestlers.append(master_list[i][0])

# parse rivalries data from masterlist
numRivalries = int(master_list[numWresters + 1][0])
rivalries = []
for i in range(numWresters + 2, numRivalries+2+numWresters):
    rivalries.append(master_list[i])

# add verticies into graph list
for i in range(numWresters):
    graph[wrestlers[i]] =  Vertex(wrestlers[i], rivalries)

print(isBipartite(graph))