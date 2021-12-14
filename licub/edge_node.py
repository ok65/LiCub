

class EdgeNode:

    def __init__(self, parent):
        self._parent = parent
        self._connected = None

    def connect_to(self, node: 'EdgeNode'):
        self._connected = node
        node._connected = self

    def is_connected(self, node_id: str):
        if self._connected:
            return self._connected.parent.id == node_id
        return False

    @property
    def id(self):
        return "{}:{}".format(self._parent.id, self._parent._edge_nodes.index(self))

    @property
    def parent(self):
        return self._parent

    @property
    def connected(self):
        return self._connected

    def __repr__(self):
        return "EdgeNode({})".format(self.id)