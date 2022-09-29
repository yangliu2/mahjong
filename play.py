from mahjong.tile import Tile
from mahjong.hand import Hand
from mahjong.group import Group


def recognize_hand(raw_hand: str):
    """ Parse the raw hand input into hand object """

    # create hand based on the input list
    hand = Hand(raw_tiles=raw_hand)
    
    # Create groups and display
    groups = hand.breakdown_groups()
    [print(x) for x in groups]
    
    # Find the tiles that can complete each group
    complements = [x.complete_set() for x in groups]
    flattened_complements = [x for sub in complements for x in sub]
    [print(x) for x in flattened_complements]
    

def play():
    raw_hand = input("Please start by entering the hand you have: \n")
    recognize_hand(raw_hand=raw_hand)


def check_set():
    """ Find the tile that will complete the part of set """
    tiles = [Tile('f', 1), Tile('f', 1), Tile('f', 1)]
    parts = Group(tiles)
    complements = parts.complete_set()
    [print(x) for x in complements]


def main():
    play()
    # check_set()


if __name__ == "__main__":
    main()
