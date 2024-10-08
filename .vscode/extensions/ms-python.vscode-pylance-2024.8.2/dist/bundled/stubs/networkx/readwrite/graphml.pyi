import warnings
from collections import defaultdict

from ..classes.graph import Graph
from ..utils import open_file

__all__ = [
    "write_graphml",
    "read_graphml",
    "generate_graphml",
    "write_graphml_xml",
    "write_graphml_lxml",
    "parse_graphml",
    "GraphMLWriter",
    "GraphMLReader",
]

def write_graphml_xml(
    G: Graph,
    path,
    encoding="utf-8",
    prettyprint=True,
    infer_numeric_types: bool = False,
    named_key_ids=False,
    edge_id_from_attribute=None,
): ...
def write_graphml_lxml(
    G: Graph,
    path,
    encoding="utf-8",
    prettyprint=True,
    infer_numeric_types: bool = False,
    named_key_ids=False,
    edge_id_from_attribute=None,
): ...
def generate_graphml(
    G: Graph,
    encoding="utf-8",
    prettyprint=True,
    named_key_ids=False,
    edge_id_from_attribute=None,
): ...
def read_graphml(path, node_type=..., edge_key_type=..., force_multigraph=False): ...
def parse_graphml(graphml_string: str, node_type=..., edge_key_type=..., force_multigraph=False): ...

class GraphML:
    NS_GRAPHML: str = ...
    NS_XSI: str = ...
    # xmlns:y="http://www.yworks.com/xml/graphml"
    NS_Y: str = ...
    SCHEMALOCATION = ...

    def construct_types(self): ...

    # This page says that data types in GraphML follow Java(TM).
    #  http://graphml.graphdrawing.org/primer/graphml-primer.html#AttributesDefinition
    # true and false are the only boolean literals:
    #  http://en.wikibooks.org/wiki/Java_Programming/Literals#Boolean_Literals
    convert_bool: dict = ...

    def get_xml_type(self, key): ...

class GraphMLWriter(GraphML):
    def __init__(
        self,
        graph=None,
        encoding="utf-8",
        prettyprint=True,
        infer_numeric_types=False,
        named_key_ids=False,
        edge_id_from_attribute=None,
    ): ...
    def __str__(self): ...
    def attr_type(self, name, scope, value): ...
    def get_key(self, name, attr_type, scope, default): ...
    def add_data(self, name, element_type, value, scope="all", default=None): ...
    def add_attributes(self, scope, xml_obj, data, default): ...
    def add_nodes(self, G: Graph, graph_element): ...
    def add_edges(self, G: Graph, graph_element): ...
    def add_graph_element(self, G): ...
    def add_graphs(self, graph_list): ...
    def dump(self, stream): ...
    def indent(self, elem, level=0): ...

class IncrementalElement:
    def __init__(self, xml, prettyprint): ...
    def append(self, element): ...

class GraphMLWriterLxml(GraphMLWriter):
    def __init__(
        self,
        path,
        graph=None,
        encoding="utf-8",
        prettyprint=True,
        infer_numeric_types=False,
        named_key_ids=False,
        edge_id_from_attribute=None,
    ): ...
    def add_graph_element(self, G): ...
    def add_attributes(self, scope, xml_obj, data, default): ...
    def __str__(self): ...
    def dump(self): ...

# default is lxml is present.
write_graphml = ...

class GraphMLReader(GraphML):
    def __init__(self, node_type=..., edge_key_type=..., force_multigraph=False): ...
    def __call__(self, path=None, string=None): ...
    def make_graph(self, graph_xml, graphml_keys, defaults, G=None): ...
    def add_node(self, G: Graph, node_xml, graphml_keys, defaults): ...
    def add_edge(self, G: Graph, edge_element, graphml_keys): ...
    def decode_data_elements(self, graphml_keys, obj_xml): ...
    def find_graphml_keys(self, graph_element): ...
