'''
使用字典实现图

a ----- b
|       |
|       |
c ----- d  ----  e

'''

class graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = []
        self.gdict = gdict

    #获取图的顶点
    def getVer(self):
        return list(self.gdict.keys())

    #获取所有的边
    def findEdges(self):
        edgename = []
        for verval in self.gdict:
            for nxtv in self.gdict[verval]:
                if {nxtv, verval} not in edgename:
                    edgename.append({nxtv, verval})
        return edgename


    #添加一个顶点，也就是在字典里加一个key
    def addVer(self, vval):
        if vval not in self.gdict:
            self.gdict[vval] = []

    #添加边
    def addEdge(self, edge):
        edge = set(edge)
        (vval1, vval2) = tuple(edge)
        if vval1 in self.gdict:
            self.gdict[vval1].append(vval2)
        else:
            self.gdict[vval1] = [vval2]

graph_elements = { "a" : ["b","c"],
          "b" : ["a", "d"],
          "c" : ["a", "d"],
          "d" : ["e"],
          "e" : ["d"]
         }

# Print the graph
g = graph(graph_elements)
print(g.getVer())
g.addVer('f')
print(g.getVer())
print(g.findEdges())
g.addEdge({'a','e'})
g.addEdge({'a','c'})
print(g.findEdges())
