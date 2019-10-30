class Node(object):

    def __init__(self, data):

        self.data = data
        self.children = []
        self.parent = []
        self.visited = False
        self.physical = False
        self.core = False
        #print(data)
        
    def add_child(self, obj):
        self.children.append(obj)
        
    def add_parent(self, obj):
        self.parent.append(obj)
        obj.add_child(self)
        
    def get_data(self):
        return self.data
    
    def reset(self):
        self.visited = False
        
    def visit(self):
        self.visited = True
        
    def get_visit(self):
        return self.visited
    
    def physical(self):
        self.physical = True
        
    def core(self):
        self.core = True
    
class Tree:
    
    def __init__(self):
        
        self.nodes = []
        
    def add_node(self, node):
        self.nodes.append(node)
        
running = True
while running:
    print('Fat Tree Implementation')
    
    tree = Tree()

    oddcheck = True
    while oddcheck:
        k = input('Please enter K:')
        #print(k)
        if int(k) % 2 == 0:
            oddcheck = False
        else:
            print('K must be an even number')
    
        coreswitches = (int(k)/2)**2
        pods = k
        aggregateswitches = (int(k)/2)*int(k)
        edgeswitches = (int(k)/2)*int(k)
        physicalmachines = edgeswitches*(int(k)/2)

        print('Number of Core Switches: ', int(coreswitches))
        print('Number of PODs: ', pods)
        print('Number of Aggregate Switches: ', int(aggregateswitches))
        print('Number of Edge Switches: ', int(edgeswitches))
        print('Number of Physical Machines: ', int(physicalmachines))

    for x in range(int(coreswitches)):
        print('Core Switch', x)
        node = Node('CS' + str(x))
        #node.core()
        tree.add_node(node)
    
    j = 0
    z = 0
    for x in range(int(aggregateswitches)):
        print('Aggregate Switch', x)
        node = Node('AS' + str(x))
        tree.add_node(node)
        for y in range(int(int(k)/2)):
            #print('CS' + str(int(y + z)))
            par = 'CS' + str(int(y + z))
            for l in range(len(tree.nodes)):
                if(tree.nodes[l].data == par):
                    node.add_parent(tree.nodes[l])
                    #print('added parent')
        z = z + (int(k)/2)
        j = j + 1
        if j == (int(k)/2):
            z = 0
            j = 0
        
    j = 0   
    z = 0
    for x in range(int(edgeswitches)):
        print('Edge Switch', x)
        node = Node('ES' + str(x))
        tree.add_node(node)
        for y in range(int(int(k)/2)):
            #print('AS' + str(int(z + y)))
            par = 'AS' + str(int(z + y))
            for l in range(len(tree.nodes)):
                if(tree.nodes[l].data == par):
                    node.add_parent(tree.nodes[l])
        j = j + 1
        if j == (int(k)/2):
            z = z + (int(k)/2)
            j = 0
    
    y = 0
    z = 0
    for x in range(int(physicalmachines)):
        print('Physical Machine', x)
        node = Node('PM' + str(x))
        #node.physical()
        tree.add_node(node)
        #print('ES' + str(z))
        par = 'ES' + str(z)
        for l in range(len(tree.nodes)):
            if(tree.nodes[l].data == par):
                node.add_parent(tree.nodes[l])        
        y = y + 1
        if y == int(int(k)/2):
            z = z + 1
            y = 0
    
    for x in range(int(pods)):
        print('POD ', x , ' contains:')
        i = x*(int(k)/2)
        for y in range(int(int(k)/2)):
            print('Aggregate Switch', int(i))
            i = i+1
        i = x*(int(k)/2)
        for y in range(int(int(k)/2)):
            print('Edge Switch', int(i))
            i = i+1

    print('')
    print('')
    incheck = True
    while incheck:
        pmA = input('Please enter first Physical Machine designation:')
        pmB = input('Please enter second Physical Machine designation:')
        if (-1 < int(pmA) < int(physicalmachines)) and (-1 < int(pmB) < int(physicalmachines)):
            incheck = False
        else:
            print('Invalid input')
            
    for i in range(len(tree.nodes)):
        if tree.nodes[i].get_data() == 'PM' + str(int(pmA)):
            startNode = tree.nodes[i]
        if tree.nodes[i].get_data() == 'PM' + str(int(pmB)):
            endNode = tree.nodes[i]
    
    twoHop = False
    fourHop = False
    sixHop = False
    
    for i in range(len(startNode.parent)):
        for j in range(len(startNode.parent[i].parent)):
            for l in range(len(startNode.parent[i].parent[j].parent)):
                for m in range(len(endNode.parent)):
                    for n in range(len(endNode.parent[m].parent)):
                        for p in range(len(endNode.parent[m].parent[n].parent)):
                            if startNode.parent[i].parent[j].parent[l].get_data() == endNode.parent[m].parent[n].parent[p].get_data():
                                sixHop = True
                            
    
    for i in range(len(startNode.parent)):
        for j in range(len(startNode.parent[i].parent)):
            for l in range(len(endNode.parent)):
                for m in range(len(endNode.parent[l].parent)):
                    if startNode.parent[i].parent[j].get_data() == endNode.parent[l].parent[m].get_data():
                        fourHop = True
                        sixHop = False
                             
    for i in range(len(startNode.parent)):
        for j in range(len(endNode.parent)):
            if startNode.parent[i].get_data() == endNode.parent[j].get_data():
                twoHop = True
                fourHop = False
                sixHop = False
                
    if twoHop:
        print('The physical machines are on the same edge switch, 2 hops apart')
    if fourHop:
        print('The physical machines are on the same pod, 4 hops apart')
    if sixHop:
        print('The physical machines are not on the same pod, 6 hops apart')

        
    runagain = input('Run again?(y/n)')
    if runagain == 'n':
        running = False    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
