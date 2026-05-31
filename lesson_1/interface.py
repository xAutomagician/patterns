from abc import ABC, abstractmethod


class BaseCardMaker(ABC):
    @abstractmethod
    def make(self, data: float) -> str:
        ...

    @abstractmethod
    def _format(self, data: float) -> str:
        ...

    @abstractmethod
    def _get_lines(self, text: str) -> str:
        ...
