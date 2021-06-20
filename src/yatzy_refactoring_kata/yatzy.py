class Yatzy:

    def __init__(self, *dice):
        self.dice: list[int] = [*dice]
        self.dice.sort(reverse=True)
        self._uniq = set(self.dice)

    def chance(self):
        return sum(self.dice)

    def yatzy(self):
        if len(self._uniq) == 1:
            return 50
        return 0

    def _die_count(self, die: int):
        return self.dice.count(die)

    def _die_score(self, die: int):
        return self._die_count(die) * die

    def ones(self):
        return self._die_count(1)

    def twos(self):
        return self._die_score(2)

    def threes(self):
        return self._die_score(3)

    def fours(self):
        return self._die_score(4)

    def fives(self):
        return self._die_score(5)

    def sixes(self):
        return self._die_score(6)

    def score_pair(self):
        for die in self.dice:
            if self.dice.count(die) == 2:
                return die * 2
        return 0

    def two_pair(self) -> int:
        score: int = 0
        pairs_found: int = 0
        for die in range(6, 0, -1):
            if self.dice.count(die) == 4:
                return die * 4
            if self.dice.count(die) >= 2:
                pairs_found += 1
                score += die * 2
            if pairs_found == 2:
                return score
        return 0

    def number_of_kind(self, min_amount: int) -> int:
        for die in self.dice:
            if self.dice.count(die) >= min_amount:
                return die * min_amount
        return 0

    def four_of_a_kind(self):
        return self.number_of_kind(4)

    def three_of_a_kind(self):
        return self.number_of_kind(3)

    def smallStraight(self):
        if self.is_straight(small=True):
            return 15
        return 0

    def largeStraight(self):
        if self.is_straight(small=False):
            return 20
        return 0

    def is_straight(self, small: bool) -> bool:
        uniq = len(self._uniq)
        if uniq == 6:
            return True
        if small:
            return uniq == 5 and 6 not in self.dice

        return uniq == 5 and 1 not in self.dice


    def fullHouse(self):
        three_of_a_kind = self.three_of_a_kind()
        used_die: int = three_of_a_kind // 3
        for die in range(6, 0, -1):
            if die == used_die:
                continue
            if self.dice.count(die) >= 2:
                return three_of_a_kind + die * 2
        return 0

