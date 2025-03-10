# class for uno cards
# =============================================================================

class Card(object):
    """
    Args:
        color (str): Color of the card
        number (int): number on the card
        special (str): type of card if special (i.e. reverse, skip, draw four, wild)

    """

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        """ Defines how the object will be printed
        """
    
        return f"{self.rank} of {self.suit}"
    

if __name__ == "__main__":
    c1 = Card('Hearts',4)
    print(c1)

    c2 = Card('Spades','Ace')
    print(c2)