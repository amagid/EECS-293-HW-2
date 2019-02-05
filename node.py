'''
Node base class
'''

from abc import ABC, abstractmethod

class Node(ABC):

    # toList method returns subtree under this node as a Collection
    @abstractmethod
    def toList(self):
        pass
