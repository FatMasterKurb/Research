import random

class Node(object):

    def __init__(self, data):

        self.data = data
        self.children = []
        self.parent = []
        self.pod = -1
        self.mb = -1
        self.pair = []
        self.frequency = -1
        #print(data)
        
    def add_child(self, obj):
        self.children.append(obj)
        
    def add_parent(self, obj):
        self.parent.append(obj)
        obj.add_child(self)
        
    def get_data(self):
        return self.data
    
    def set_pod(self, n):
        self.pod = n
        
    def get_pod(self):
        return self.pod

    def set_mb(self, n):
        self.mb = n
        
    def get_mb(self):
        return self.mb
    
    def set_pair(self, n):
        self.pair.append(n)
    
    def get_pair(self):
        return self.pair

    def set_frequency(self, n):
        self.frequency = n
    
    def get_frequency(self):
        return self.frequency
    
class Vmpair:
    
    def __init__(self, id, f, pma, pmb):
        self.id = id
        self.frequency = f
        self.pma = pma
        self.pmb = pmb
        
    def get_a(self):
        return self.pma
    
    def get_b(self):
        return self.pmb
    
    def get_frequency(self):
        return self.frequency
    
class Tree:
    
    def __init__(self):
        
        self.nodes = []
        self.pairs = []
    
    def add_node(self, node):
        self.nodes.append(node)
        
    def add_pair(self, vmpair):
        self.pairs.append(vmpair)    
        
def distance(startNode, endNode):
    
    if 'PM' in startNode.get_data() and 'PM' in endNode.get_data(): #pm to pm
    
        noHop = False   
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
                
        if startNode.get_data() == endNode.get_data():
            noHop = True
            twoHop = False
            fourHop = False
            sixHop = False
                
        if noHop:           #works
            return 0
        if twoHop:          #works
            return 2
        if fourHop:         #works
            return 4
        if sixHop:          #works
            return 6
        
    if 'PM' in startNode.get_data() and 'ES' in endNode.get_data():
        
        if endNode in startNode.parent:         #works
            return 1
        
        if startNode.parent[0].get_pod() == endNode.get_pod():      #works
            return 3
        
        else:                           #works
            return 5
        
    if 'PM' in startNode.get_data() and 'AS' in endNode.get_data():
        
        if startNode.parent[0].get_pod() == endNode.get_pod():      #works      
            return 2
        
        else:                           #works
            return 4
        
    if 'ES' in startNode.get_data() and 'ES' in endNode.get_data():
        
        if startNode.get_data() == endNode.get_data():      #works
            return 0
        
        if startNode.get_pod() == endNode.get_pod():    #works    
            return 2
        
        else:           #works        
            return 4
        
    if 'ES' in startNode.get_data() and 'AS' in endNode.get_data():
        
        if startNode.get_pod() == endNode.get_pod():    #works
            return 1
        
        else:               #works
            return 3
        
    if 'ES' in startNode.get_data() and 'PM' in endNode.get_data():
        
        if startNode in endNode.parent:     #works
            return 1
        
        if startNode.get_pod() == endNode.parent[0].get_pod():          #works
            return 3
        
        else:                       #Works
            return 5
        
    if 'AS' in startNode.get_data() and 'AS' in endNode.get_data():
        
        if startNode.get_data() == endNode.get_data():       #works   
            return 0
        
        if startNode.get_pod() == endNode.get_pod():        #works
            return 2
        
        if startNode.parent[0] in endNode.parent:           #works
            return 2
        
        else:           #works
            return 4
        
    if 'AS' in startNode.get_data() and 'ES' in endNode.get_data():
        
        if startNode in endNode.parent:     #works
            return 1
        
        else:                   #works
            return 3
        
    if 'AS' in startNode.get_data() and 'PM' in endNode.get_data():
        
        if startNode.get_pod() == endNode.parent[0].get_pod():              #Works
            return 2
        
        else:                   #works
            return 4
        
        
        
running = True
while running:
    print('Fat Tree Implementation')
    
    tree = Tree()

    oddcheck = True
    while oddcheck:
        k = input('Please enter K:')
        pairs = input('Please input number of VM pairs:')
        freq = input('Plese input maximum communication frequency')
        mb = input('Please enter number of Middle Boxes:')
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
            for z in range(len(tree.nodes)):
                if tree.nodes[z].data == 'AS' + str(int(i)):
                    tree.nodes[z].set_pod(x)
                    #print(tree.nodes[z].get_data() + ' placed')
            i = i+1
        i = x*(int(k)/2)
        for y in range(int(int(k)/2)):
            print('Edge Switch', int(i))
            for z in range(len(tree.nodes)):
                if tree.nodes[z].data == 'ES' + str(int(i)):
                    tree.nodes[z].set_pod(x)
                    #print(tree.nodes[z].get_data() + ' placed')
            i = i+1
            

    print('')
    
    mbp = 0
    while mbp < int(mb):
        switch = random.choice(tree.nodes)
        if 'ES' in switch.get_data() and switch.get_mb() == -1 or 'AS' in switch.get_data() and switch.get_mb() == -1:
            switch.set_mb(mbp)
            print('Middle Box ' + str(mbp) + ' placed on ' + switch.get_data())
            mbp = mbp + 1
    
    print('')
    
    numpair = 0
    while numpair < int(pairs):
        switchA = random.choice(tree.nodes)
        switchB = random.choice(tree.nodes)
        if 'PM' in switchA.get_data() and 'PM' in switchB.get_data():
            fr = random.randint(0,int(freq))
            vmpair = Vmpair(numpair, fr, switchA, switchB)
            tree.add_pair(vmpair)
            print('VM pair ' + str(numpair) + ' between ' + switchA.get_data() + ' and ' + switchB.get_data() + ' at frequency ' + str(fr))
            numpair = numpair + 1
    
    print('')
        
    paircount = 0
    while paircount < int(pairs):
        
        pmA = tree.pairs[paircount].get_a()
        pmB = tree.pairs[paircount].get_b()
           
        for i in range(len(tree.nodes)):
            if tree.nodes[i].get_data() == pmA:
                startNode = tree.nodes[i]
            if tree.nodes[i].get_data() == pmB:
                endNode = tree.nodes[i]
        
        sum = 0
        mbcheck = 0
        mbnodeA = pmA
    
        while mbcheck < int(mb):
        
            for x in range(int(len(tree.nodes))):
                if tree.nodes[x].get_mb() == mbcheck:
                    mbnodeB = tree.nodes[x]
                
            sum = sum + distance(mbnodeA, mbnodeB)
            print('Distance from ' + str(mbnodeA.get_data()) + ' to ' + str(mbnodeB.get_data()) + ' is ' + str(distance(mbnodeA, mbnodeB)))
        
            mbnodeA = mbnodeB
            mbcheck = mbcheck + 1
        
        sum = sum + distance(mbnodeA, pmB)
        print('Distance from ' + str(mbnodeA.get_data()) + ' to ' + str(pmB.get_data()) + ' is ' + str(distance(mbnodeA, pmB)))
        print('Total distance for pair ' + str(paircount) + ' is ' + str(int(sum)))
        print('Total cost for pair ' + str(paircount) + ' is ' + str(int(sum * int(tree.pairs[paircount].get_frequency()))))
        print('')
        paircount = paircount + 1
        
    runagain = input('Run again?(y/n)')
    if runagain == 'n':
        running = False    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
