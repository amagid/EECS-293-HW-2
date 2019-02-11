from abc import ABC, abstractmethod
from parse_state import ParseState

class Symbol(ABC):

    @abstractmethod
    def parse(self, token_list):
        pass