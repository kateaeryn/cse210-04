from game.casting.actor import Actor

class Artifact(Actor):
    """A graphic character that falls down the screen
    
    The responsibility of the Artifact is to provide attributes for rock and gem

    Attributes:
        super: inheritance from Actor class
        score(int): integer to store the score
    """

    def __init__(self):
        """Constructs a new Artifact"""
        super().__init__()
        self._score = 0

    def calculate_score(self):
        """Calculates the score if the artifact the robot finds is a gem or rock
        
        returns:
            score
        """
        score = 0
        if (self.get_text() == "*"):
            score = 1
        else:
            score = -1
        return score



   