class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}   #Each vertex object keeps track of vertices it is connected to

    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self,nbr):
        return self.connectedTo[nbr]

class Graph:        #Keep list of all vertices
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)   #create new vertex for this key
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.vertList

    def addEdge(self,f,t,cost=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())
    

def main():
    g=Graph()
    for i in range(6):  #for each key value create instance of vertex
        g.addVertex(i)
    print(g.vertList)
    print(g.getVertices())
    g.addEdge(0,1,14)
    print(g.getVertices())




if __name__ == '__main__':
    main()


''' Creating HASH MAP
class MyHashMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.my_dict={}


    def put(self, key, value):
        self.my_dict[key]=value


    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        if key in self.my_dict.keys():
            return self.my_dict[key]
        else:
            return -1


    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: void
        """
        self.my_dict.pop(key,None)



# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
'''