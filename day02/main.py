"""
https://adventofcode.com/2022/day/2

Let's go overboard!
"""

from typing import ClassVar, Dict, Type
from dataclasses import dataclass


@dataclass
class Hand:
    """
    The hand of a given player
    """

    score: int = 0


@dataclass
class Rock(Hand):
    """
    Rock beats scissors
    """

    score = 1


@dataclass
class Paper(Hand):
    """
    Paper beats rock
    """

    score = 2


@dataclass
class Scissors(Hand):
    """
    Scissors beats paper
    """

    score = 3


class Round:
    """
    A round of our game
    """

    loosers: ClassVar[Dict[Type[Hand], Type[Hand]]] = {
        Scissors: Rock,
        Rock: Paper,
        Paper: Scissors,
    }

    winners: ClassVar[Dict[Type[Hand], Type[Hand]]] = {
        Scissors: Paper,
        Rock: Scissors,
        Paper: Rock,
    }

    def __init__(self, opponent_letter: str, player_letter: str, problem: str = "a"):
        if opponent_letter not in "ABC":
            raise ValueError("Invalid opponent letter")
        if player_letter not in "XYZ":
            raise ValueError("Invalid player letter")
        if problem not in "ab":
            raise ValueError("Invalid problem")

        self.opponent_hand = self.create_hand(opponent_letter)
        if problem == "a":
            self.player_hand = self.create_hand(player_letter)
        else:
            self.player_hand = self.create_hand_for_outcome(player_letter)

    def create_hand_for_outcome(self, letter: str) -> Hand:
        """
        Convert the letter to the next letter in the alphabet
        """
        opponent_type = type(self.opponent_hand)
        if letter == "X":
            return self.winners[opponent_type]()
        if letter == "Y":
            return opponent_type()
        if letter == "Z":
            return self.loosers[opponent_type]()
        raise ValueError("Invalid letter")

    def round_score(self) -> int:
        """
        Return the score of the round
        """
        score = 0
        round_outcome = self.beats(self.player_hand, self.opponent_hand)
        if round_outcome == 1:
            score = 6
        elif round_outcome == 0:
            score = 3

        return score + self.player_hand.score

    @classmethod
    def create_hand(cls, letter: str) -> Hand:
        """
        Create a hand from a letter
        """
        return {
            "A": Rock,
            "B": Paper,
            "C": Scissors,
            "X": Rock,
            "Y": Paper,
            "Z": Scissors,
        }[letter]()

    @classmethod
    def beats(cls, hand1: Hand, hand2: Hand) -> int:
        """
        Return 1 if hand1 beats hand2, 0 if they are equal, -1 if hand2 beats hand1
        """
        if isinstance(hand1, type(hand2)):
            return 0

        if isinstance(hand2, cls.winners[type(hand1)]):
            return 1

        return -1


def main(filename, problem: str = "a"):
    """
    Main function
    """
    score = 0
    with open(filename, encoding="ascii") as handle:
        for line in handle.readlines():
            opponent_letter, player_letter = line.split()
            game_round = Round(opponent_letter, player_letter, problem)
            score += game_round.round_score()
    print(score)


if __name__ == "__main__":
    main("input_data.txt", "b")
