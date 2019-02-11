'''
Node base class
'''

from abc import ABC, abstractmethod

class Node(ABC):

    # to_list method returns subtree under this node as a Collection
    @abstractmethod
    def to_list(self):
        pass
