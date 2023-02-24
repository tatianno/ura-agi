from unittest import TestCase
from ura_agi import Node


class NodeTestCase(TestCase):

    def test_node_class(self):
        node = Node('Vendas', 'CONTEXT-1', '100', '1')
        self.assertTrue(hasattr(node, 'name'))
        self.assertTrue(hasattr(node, 'context'))
        self.assertTrue(hasattr(node, 'extension'))
        self.assertTrue(hasattr(node, 'priority'))