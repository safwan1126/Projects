from abc import ABC, abstractmethod
# abc = abstract base class
class AIPlatform(ABC):
    @abstractmethod
    def chat(self, prompt: str) -> str:
        """sends a prompt to the AI and returns the reponse text"""
        pass
