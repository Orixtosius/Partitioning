from abc import ABC, abstractmethod
from ..partition import Partitioner


class Search(ABC):

    def __init__(self) -> None:
        self.partitioner = Partitioner()
        
    @abstractmethod
    def search(self) -> list:
        """"""