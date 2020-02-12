import random
from itertools import permutations

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
        
def migrate(nodeA, nodeB, mu, f):
        
    mbn = nodeA.get_mb()
    nodeA.set_mb(-1)
    nodeB.set_mb(mbn)
    dist = distance(nodeA, nodeB)
    cost = int(dist) * int(mu)
    print('mb' + str(mbn) + ' migrates from ' + nodeA.get_data() + ' to ' + nodeB.get_data() + ', ' + str(dist) + ' hops at total cost ' + str(cost))
    f.write('mb' + str(mbn) + ' migrates from ' + nodeA.get_data() + ' to ' + nodeB.get_data() + ', ' + str(dist) + ' hops at total cost ' + str(cost) +'\n')    
        
def distance(startNode, endNode):
    
    if startNode.get_data() == endNode.get_data():
        return 0
    
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
        
    if 'PM' in startNode.get_data() and 'CS' in endNode.get_data():
        
        return 3
        
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
        
    if 'ES' in startNode.get_data() and 'CS' in endNode.get_data():
        
        return 2
        
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
        
    if 'AS' in startNode.get_data() and 'CS' in endNode.get_data():
        
        if endNode in startNode.parent:
            return 1
        
        else:
            return 3
        
    if 'CS' in startNode.get_data() and 'CS' in endNode.get_data():
        
        if endNode in startNode.children[0].parent:
            return 2
        
        else:
            return 4
        
    if 'CS' in startNode.get_data() and 'AS' in endNode.get_data():
        
        if startNode in endNode.parent:
            return 1
        
        else:
            return 3
        
    if 'CS' in startNode.get_data() and 'ES' in endNode.get_data():
        
        return 2
        
    if 'CS' in startNode.get_data() and 'PM' in endNode.get_data():
        
        return 3
        
running = True
while running:
    f = open("FatTree.txt", "w+")
    f.write('Fat Tree Implementation\n')
    print('Fat Tree Implementation')
    
    tree = Tree()
    '''
    oddcheck = True
    while oddcheck:
        
        k = input('Please enter K:')
        pairs = input('Please input number of VM pairs:')
        freq = input('Plese input maximum communication frequency:')
        mb = input('Please enter number of Middle Boxes:')
        mu = input('Please enter migration coefficient:')
        #print(k)
        if int(k) % 2 == 0:
            oddcheck = False
        else:
            print('K must be an even number')
        
    '''    
    k = 4
    pairs = 20
    freq = 1000
    mb = 3
    mu = 250
    
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
        
    f.write('Number of Core Switches: ' +  str(int(coreswitches)) + '\n')
    f.write('Number of PODs: ' + str(pods))
    f.write('Number of Aggregate Switches: ' + str(int(aggregateswitches)) + '\n')
    f.write('Number of Edge Switches: ' + str(int(edgeswitches)) + '\n')
    f.write('Number of Physical Machines: ' +  str(int(physicalmachines)) + '\n')

    for x in range(int(coreswitches)):
        print('Core Switch', x)
        f.write('Core Switch' + str(x) + '\n')
        node = Node('CS' + str(x))
        #node.core()
        tree.add_node(node)
    
    j = 0
    z = 0
    for x in range(int(aggregateswitches)):
        print('Aggregate Switch', x)
        f.write('Aggregate Switch' + str(x) + '\n')
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
        f.write('Edge Switch' + str(x) +'\n')
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
        f.write('Physical Machine' + str(x) +'\n')
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
        f.write('POD ' + str(x) + ' contains:\n')
        i = x*(int(k)/2)
        for y in range(int(int(k)/2)):
            print('Aggregate Switch', int(i))
            f.write('Aggregate Switch' + str(int(i)) + '\n')
            for z in range(len(tree.nodes)):
                if tree.nodes[z].data == 'AS' + str(int(i)):
                    tree.nodes[z].set_pod(x)
                    #print(tree.nodes[z].get_data() + ' placed')
            i = i+1
        i = x*(int(k)/2)
        for y in range(int(int(k)/2)):
            print('Edge Switch', int(i))
            f.write('Edge Switch' + str(int(i)) + '\n')
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
            f.write('Middle Box ' + str(mbp) + ' placed on ' + switch.get_data() + '\n')
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
            f.write('VM pair ' + str(numpair) + ' between ' + switchA.get_data() + ' and ' + switchB.get_data() + ' at frequency ' + str(fr) + '\n')
            numpair = numpair + 1
    
    print('')
    totsum = 0  
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
        
        for x in range(int(len(tree.nodes))):
                if tree.nodes[x].get_mb() == 0:
                    mbnodeZero = tree.nodes[x]
        
        for x in range(int(len(tree.nodes))):
                if tree.nodes[x].get_mb() == 1:
                    mbnodeOne = tree.nodes[x]
                    
       
    
        while mbcheck < int(mb):
        
            for x in range(int(len(tree.nodes))):
                if tree.nodes[x].get_mb() == mbcheck:
                    mbnodeB = tree.nodes[x]
                
            sum = sum + distance(mbnodeA, mbnodeB)
            #print('Distance from ' + str(mbnodeA.get_data()) + ' to ' + str(mbnodeB.get_data()) + ' is ' + str(distance(mbnodeA, mbnodeB)))
            #f.write('Distance from ' + str(mbnodeA.get_data()) + ' to ' + str(mbnodeB.get_data()) + ' is ' + str(distance(mbnodeA, mbnodeB)) +'\n')
        
            mbnodeA = mbnodeB
            mbcheck = mbcheck + 1
        
        sum = sum + distance(mbnodeA, pmB)
        costsum = int(sum * int(tree.pairs[paircount].get_frequency()))
        totsum = totsum + costsum
        '''
        print('Distance from ' + str(mbnodeA.get_data()) + ' to ' + str(pmB.get_data()) + ' is ' + str(distance(mbnodeA, pmB)))
        print('Total distance for pair ' + str(paircount) + ' is ' + str(int(sum)))
        print('Total cost for pair ' + str(paircount) + ' is ' + str(int(sum * int(tree.pairs[paircount].get_frequency()))))
        print('')
        f.write('Distance from ' + str(mbnodeA.get_data()) + ' to ' + str(pmB.get_data()) + ' is ' + str(distance(mbnodeA, pmB)) + '\n')
        f.write('Total distance for pair ' + str(paircount) + ' is ' + str(int(sum)) + '\n')
        f.write('Total cost for pair ' + str(paircount) + ' is ' + str(int(sum * int(tree.pairs[paircount].get_frequency()))) + '\n')
        f.write('\n')
        '''
        paircount = paircount + 1
    
    print('Total cost of all pairs: ' + str(int(totsum)))
    print('')
    print('')
    print('')
    
    ogpos = []      #save original positions
    
    mbcount = 0
    while mbcount < int(mb):
        for a in range(len(tree.nodes)):
            if tree.nodes[a].get_mb() == mbcount:
                ogpos.append(tree.nodes[a])
        mbcount = mbcount + 1
    
    #trying all permutations
    
    for k in range(len(tree.nodes)):
        if tree.nodes[k].get_mb() != -1:
            tree.nodes[k].set_mb(-1)
    
    for i in range(len(tree.nodes)):
        if tree.nodes[i].get_mb() == 0:
            tree.nodes[i].set_mb(0)
            
    lowcost = 0
    lowperm = []
    switchlist = []
    
    for i in range(len(tree.nodes)):
        if 'CS' in tree.nodes[i].get_data() or 'AS' in tree.nodes[i].get_data() or 'ES' in tree.nodes[i].get_data():
            switchlist.append(tree.nodes[i])
    
    perm = list(permutations(switchlist, mb))
    
    for i in range(len(perm)):
        for j in range(len(perm[i])):
            perm[i][j].set_mb(j)
            #print('mb ' + str(j) + ' set at ' + str(perm[i][j].get_data()))
        #print('')    
        
        totsum = 0  
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
        
            for x in range(int(len(tree.nodes))):
                    if tree.nodes[x].get_mb() == 0:
                        mbnodeZero = tree.nodes[x]
        
            for x in range(int(len(tree.nodes))):
                    if tree.nodes[x].get_mb() == 1:
                        mbnodeOne = tree.nodes[x]
                    
       
    
            while mbcheck < int(mb):
        
                for x in range(int(len(tree.nodes))):
                    if tree.nodes[x].get_mb() == mbcheck:
                        mbnodeB = tree.nodes[x]
                
                sum = sum + distance(mbnodeA, mbnodeB)
                #print('Distance from ' + str(mbnodeA.get_data()) + ' to ' + str(mbnodeB.get_data()) + ' is ' + str(distance(mbnodeA, mbnodeB)))
                #f.write('Distance from ' + str(mbnodeA.get_data()) + ' to ' + str(mbnodeB.get_data()) + ' is ' + str(distance(mbnodeA, mbnodeB)) +'\n')
        
                mbnodeA = mbnodeB
                mbcheck = mbcheck + 1
        
            sum = sum + distance(mbnodeA, pmB)
            costsum = int(sum * int(tree.pairs[paircount].get_frequency()))
            totsum = totsum + costsum
            '''
            print('Distance from ' + str(mbnodeA.get_data()) + ' to ' + str(pmB.get_data()) + ' is ' + str(distance(mbnodeA, pmB)))
            print('Total distance for pair ' + str(paircount) + ' is ' + str(int(sum)))
            print('Total cost for pair ' + str(paircount) + ' is ' + str(int(sum * int(tree.pairs[paircount].get_frequency()))))
            print('')
            f.write('Distance from ' + str(mbnodeA.get_data()) + ' to ' + str(pmB.get_data()) + ' is ' + str(distance(mbnodeA, pmB)) + '\n')
            f.write('Total distance for pair ' + str(paircount) + ' is ' + str(int(sum)) + '\n')
            f.write('Total cost for pair ' + str(paircount) + ' is ' + str(int(sum * int(tree.pairs[paircount].get_frequency()))) + '\n')
            f.write('\n')
            '''
            paircount = paircount + 1
        
        if lowcost == 0:
            lowcost = totsum
            lowperm = perm[i]
            print('cost of ' + str(lowcost) + ' found')

            for k in range(mb):
                for l in range(len(tree.nodes)):
                    if tree.nodes[l].get_mb() == k:
                        print('mb' + str(k) + ' ' + str(tree.nodes[l].get_data())) 
            print('')
        if totsum < lowcost:
            lowcost = totsum
            lowperm = perm[i]
            print('cost of ' + str(lowcost) + ' found')

            for k in range(mb):
                for l in range(len(tree.nodes)):
                    if tree.nodes[l].get_mb() == k:
                        print('mb' + str(k) + ' ' + str(tree.nodes[l].get_data()))
            print('')
            
        for k in range(len(tree.nodes)):
            if tree.nodes[k].get_mb != -1:
                tree.nodes[k].set_mb(-1)
    
    
    '''
    #for migration of single mb
    mincost = totsum
    mbcount = 0
    minmig = []
    while mbcount < int(mb):
        
        for a in range(len(tree.nodes)):
            if mbcount == tree.nodes[a].get_mb():
                ognode = tree.nodes[a]
        
        for b in range(len(tree.nodes)):
            if 'ES' in tree.nodes[b].get_data() and tree.nodes[b].get_mb() == -1 or 'AS' in tree.nodes[b].get_data() and tree.nodes[b].get_mb() == -1:
                tree.nodes[b].set_mb(mbcount)
                ognode.set_mb(-1)
                
                totsum = 0  
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
        
                    for x in range(int(len(tree.nodes))):
                        if tree.nodes[x].get_mb() == 0:
                            mbnodeZero = tree.nodes[x]
        
                    for x in range(int(len(tree.nodes))):
                        if tree.nodes[x].get_mb() == 1:
                            mbnodeOne = tree.nodes[x]
                    
       
    
                    while mbcheck < int(mb):
        
                        for x in range(int(len(tree.nodes))):
                            if tree.nodes[x].get_mb() == mbcheck:
                                mbnodeB = tree.nodes[x]
                
                        sum = sum + distance(mbnodeA, mbnodeB)
                        #print('Distance from ' + str(mbnodeA.get_data()) + ' to ' + str(mbnodeB.get_data()) + ' is ' + str(distance(mbnodeA, mbnodeB)))
                        #f.write('Distance from ' + str(mbnodeA.get_data()) + ' to ' + str(mbnodeB.get_data()) + ' is ' + str(distance(mbnodeA, mbnodeB)) +'\n')
        
                        mbnodeA = mbnodeB
                        mbcheck = mbcheck + 1
        
                    sum = sum + distance(mbnodeA, pmB)
                    costsum = int(sum * int(tree.pairs[paircount].get_frequency()))
                    totsum = totsum + costsum
                    
                    
                    print('Distance from ' + str(mbnodeA.get_data()) + ' to ' + str(pmB.get_data()) + ' is ' + str(distance(mbnodeA, pmB)))
                    print('Total distance for pair ' + str(paircount) + ' is ' + str(int(sum)))
                    print('Total cost for pair ' + str(paircount) + ' is ' + str(int(sum * int(tree.pairs[paircount].get_frequency()))))
                    print('')
                    f.write('Distance from ' + str(mbnodeA.get_data()) + ' to ' + str(pmB.get_data()) + ' is ' + str(distance(mbnodeA, pmB)) + '\n')
                    f.write('Total distance for pair ' + str(paircount) + ' is ' + str(int(sum)) + '\n')
                    f.write('Total cost for pair ' + str(paircount) + ' is ' + str(int(sum * int(tree.pairs[paircount].get_frequency()))) + '\n')
                    f.write('\n')
                    
                    
                    paircount = paircount + 1
    
                #print('Total cost of all pairs: ' + str(int(totsum)))
                comcost = totsum
                migcost = (int(distance(ognode, tree.nodes[b])) * int(mu))
                totsum = totsum + (int(distance(ognode, tree.nodes[b])) * int(mu))
                tree.nodes[b].set_mb(-1)
                ognode.set_mb(mbcount)
                if totsum < mincost:
                    minmig.clear()
                    minmig.append(ognode)
                    minmig.append(tree.nodes[b])
                    mincost = totsum
                    print('lower cost found: ' + str(mincost) + ' ' + str(minmig[0].get_data()) + ' migrates to ' + str(minmig[1].get_data()) + ' Communication cost: ' + str(comcost) + ' Migration cost: ' + str(migcost))
        mbcount = mbcount + 1
    
    if len(minmig) != 0:
        print('By migrating mb' + str(minmig[0].get_mb()) + ' from ' + str(minmig[0].get_data()) + ' to ' + str(minmig[1].get_data()) + ' a cost of ' + str(mincost) + ' can be achieved')           
    else:
        print('No lower cost found')
      
    totsum = 0
    mbcount = 0
    #ogpos = []
    
    print('')
    print('')
    print('') 
    
    while mbcount < int(mb):
        for a in range(len(tree.nodes)):
            if tree.nodes[a].get_mb() == mbcount:
                #ogpos.append(tree.nodes[a])
                tree.nodes[a].set_mb(-1)
        mbcount = mbcount + 1

    mbcount = 1
    sumdist = 0
    lowdist = -1
    lowmig = int(mu) * 7
    migsum = 0
    
    for a in range(len(tree.nodes)):
        if 'ES' in tree.nodes[a].get_data() or 'AS' in tree.nodes[a].get_data() or 'CS' in tree.nodes[a].get_data():
            for b in range(len(tree.pairs)):
                pma = tree.pairs[b].get_a()
                sumdist = sumdist + int(distance(tree.nodes[a], pma))
            print(tree.nodes[a].get_data() + ' ' + str(sumdist))
            if lowdist == -1:
                lowdist = sumdist
                lownode = tree.nodes[a]
                print(lowdist)
            if sumdist <= lowdist:
                lowdist = sumdist
                print(lowdist)
                if distance(ogpos[0], tree.nodes[a]) < distance(ogpos[0], lownode):
                    lownode = tree.nodes[a]
        sumdist = 0
        
    lownode.set_mb(0)    
    migcost = distance(ogpos[0], lownode) * int(mu)
    
    print('Best choice for first mb is ' + str(lownode.get_data()))
    
    lowdist = -1
    sumdist = 0
    
    for a in range(len(tree.nodes)):
        if 'ES' in tree.nodes[a].get_data() and tree.nodes[a].get_mb() == -1 or 'AS' in tree.nodes[a].get_data() and tree.nodes[a].get_mb() == -1 or 'CS' in tree.nodes[a].get_data() and tree.nodes[a].get_mb() == -1:
            for b in range(len(tree.pairs)):
                pmb = tree.pairs[b].get_b()
                sumdist = sumdist + distance(tree.nodes[a], pmb)
            print(tree.nodes[a].get_data() + ' ' + str(sumdist))
            if lowdist == -1:
                lowdist = sumdist
                lownode = tree.nodes[a]
            if sumdist <= lowdist:
                lowdist = sumdist
                if distance(ogpos[0], tree.nodes[a]) < distance(ogpos[0], lownode):
                    lownode = tree.nodes[a]
        sumdist = 0
        
    lownode.set_mb(int(mb) - 1)    
    migcost = distance(ogpos[int(mb) - 1], lownode) * int(mu) + migcost
    
    print('Best choice for last mb is ' + str(lownode.get_data()))
    
    while mbcount < (int(mb) - 1):
        for i in range(len(tree.nodes)):
            if tree.nodes[i].get_mb() == (mbcount - 1):
                prevnode = tree.nodes[i]
        for a in range(len(tree.nodes)):
            if 'ES' in tree.nodes[a].get_data() and tree.nodes[a].get_mb() == -1 or 'AS' in tree.nodes[a].get_data() and tree.nodes[a].get_mb() == -1 or 'CS' in tree.nodes[a].get_data() and tree.nodes[a].get_mb() == -1:
                if distance(prevnode, tree.nodes[a]) == 1 or distance(prevnode, tree.nodes[a]) == 2:
                    if distance(ogpos[mbcount], tree.nodes[a]) * int(mu) < lowmig:
                        lowmig = distance(ogpos[mbcount], tree.nodes[a]) * int(mu)
                        mignode = tree.nodes[a]
                        mignode.set_mb(mbcount)
                    
        print('mb' + str(mbcount) + ' placed at ' + str(mignode.get_data()))
        migsum = migsum + (distance(ogpos[mbcount], mignode) * int(mu))
        lowmig = int(mu) * 7
        mbcount = mbcount + 1
        
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
        
        for x in range(int(len(tree.nodes))):
                if tree.nodes[x].get_mb() == 0:
                    mbnodeZero = tree.nodes[x]
        
        for x in range(int(len(tree.nodes))):
                if tree.nodes[x].get_mb() == 1:
                    mbnodeOne = tree.nodes[x]
                    
       
    
        while mbcheck < int(mb):
        
            for x in range(int(len(tree.nodes))):
                if tree.nodes[x].get_mb() == mbcheck:
                    mbnodeB = tree.nodes[x]
                
            sum = sum + distance(mbnodeA, mbnodeB)
            #print('Distance from ' + str(mbnodeA.get_data()) + ' to ' + str(mbnodeB.get_data()) + ' is ' + str(distance(mbnodeA, mbnodeB)))
            #f.write('Distance from ' + str(mbnodeA.get_data()) + ' to ' + str(mbnodeB.get_data()) + ' is ' + str(distance(mbnodeA, mbnodeB)) +'\n')
        
            mbnodeA = mbnodeB
            mbcheck = mbcheck + 1
        
        sum = sum + distance(mbnodeA, pmB)
        costsum = int(sum * int(tree.pairs[paircount].get_frequency()))
        totsum = totsum + costsum
        
        
        print('Distance from ' + str(mbnodeA.get_data()) + ' to ' + str(pmB.get_data()) + ' is ' + str(distance(mbnodeA, pmB)))
        print('Total distance for pair ' + str(paircount) + ' is ' + str(int(sum)))
        print('Total cost for pair ' + str(paircount) + ' is ' + str(int(sum * int(tree.pairs[paircount].get_frequency()))))
        print('')
        f.write('Distance from ' + str(mbnodeA.get_data()) + ' to ' + str(pmB.get_data()) + ' is ' + str(distance(mbnodeA, pmB)) + '\n')
        f.write('Total distance for pair ' + str(paircount) + ' is ' + str(int(sum)) + '\n')
        f.write('Total cost for pair ' + str(paircount) + ' is ' + str(int(sum * int(tree.pairs[paircount].get_frequency()))) + '\n')
        f.write('\n')
        
        
        paircount = paircount + 1
    
    print('Total cost of all pairs: ' + str(int(totsum) + migsum + migcost) + ' including a migration cost of: ' + str(migsum + migcost))
    '''                

      
    runagain = input('Run again?(y/n)')
    if runagain == 'n':
        running = False 
        
    f.close()   
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
