from mahjong.suit import SuitEnum
from mahjong.tile import Tile
from mahjong.hand import Hand


def recognize_hand(raw_hand: str, 
                   split_interval: int = 2):
    """ Parse the raw hand input into hand object """

    # split the raw input every split interval length for the shortest input
    # e.g. 1w2b -> [1w, 2b]
    raw_tiles = [raw_hand[i:i + split_interval] 
                 for i in range(0, len(raw_hand), split_interval)]

    # create hand based on the input list
    hand = Hand(raw_tiles=raw_tiles)
    

def play():
    raw_hand = input("Please start by entering the hand you have: \n")
    recognize_hand(raw_hand=raw_hand)


def main():
    play()


if __name__ == "__main__":
    main()