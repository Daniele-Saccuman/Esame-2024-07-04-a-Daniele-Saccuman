from database.DAO import DAO
import networkx as nx

class Model:
    def __init__(self):
        self._listYear = []
        self._listShape = []
        self._grafo = nx.DiGraph()
        self._idMap = {}

    def getYears(self):
        self._listYears = DAO.getAllYears()
        return self._listYears

    def getShape(self, anno):
        self._listShape = DAO.getAllShapes(anno)
        return self._listShape

    def buildGraph(self, anno, shape):
        self._nodi = DAO.get_all_sightings(anno, shape)
        for s in self._nodi:
            self._idMap[s.id] = s

        self._grafo.add_nodes_from(self._nodi)
        self._archi = DAO.getAllEdges(anno, shape)

        for e in self._archi:
            if e[1] < e[3]:
                self._grafo.add_edge(self._idMap[e[0]], self._idMap[e[2]])
            elif e[1] > e[3]:
                self._grafo.add_edge(self._idMap[e[2]], self._idMap[e[0]])


    def getNumNodi(self):
        return len(self._grafo.nodes)

    def getNumArchi(self):
        return len(self._grafo.edges)

    def get_weakly_connected_components(self):
        # Ottiene le componenti debolmente connesse del grafo
        components = list(nx.weakly_connected_components(self._grafo))
        return components

    def getEdges(self):
        return list(self._grafo.edges())

    def getNodes(self):
        return list(self._grafo.nodes())




