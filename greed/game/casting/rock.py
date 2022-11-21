from game.casting.actor import Actor


class Rock(Actor):
    """A stationary graphic character that does not move
    
    The responsibility of the Artifact is to be discovered by the robot as it looks for the kitten

    Attributes:
        _position (int): current location
        _message (string): message to display
        _text(string): text to attach to the artifacts
        _font_size(int): font size to use
        _color(color): color of the text
    """

    def __init__(self):
        """Constructs a new Artifact"""
        self._position = (0, 0)
        self._score = 0
        self._text = ""
        self._font_size = 18
        self._color = ()
      

    def get_position(self):
        """Get's the artifacts position from Actor class
        returns: Artifacts position on board
         """
        return self._position

    def set_score(self, score):
        """Updates the score for each artifact
            args: 
            message(string): text to display when artifact is discovered
            """
        self._score = score

    def get_score(self):
        """Gets current score
        returns:
        message about artifact
        """
        return self._score

    def set_text(self, text):
       """Updates the text to the given value
       returns:
            text for the artifact
            """
       self._text = text

    def set_font_size(self, font_size):
        """Updates the font size for the artifacts
        args:
        font-size(int): given font size
        """
        self._font_size = font_size

    def set_color(self, color):
        """Updates the color of the artifact
        args:
        color(color): the color of the artifact
        """
        self._color = color

    def set_position(self, position):
        """Updates the position of the artifact
        args:
        position: inherited from actor class
        """
        self._position = position
        return self._position
