
# Library imports
import uuid
import re

# Project imports
from licub.edge_node import EdgeNode


class LiCub:

    def __init__(self):
        self._id = re.sub(r"\d", "", uuid.uuid4().hex)[:4]
        self._edge_nodes = [EdgeNode(self), EdgeNode(self), EdgeNode(self), EdgeNode(self)]

    @property
    def id(self):
        return self._id

    @property
    def edge(self):
        return self._edge_nodes

    def where_is(self, node_id: str):
        for edge in self._edge_nodes:
            if edge.is_connected(node_id):
                return edge.id


