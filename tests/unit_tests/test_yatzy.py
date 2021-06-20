from yatzy_refactoring_kata.yatzy import Yatzy

def test_chance_scores_sum_of_all_dice():
    expected = 15
    actual = Yatzy(2, 3, 4, 5, 1).chance()
    assert expected == actual
    assert 16 == Yatzy(3, 3, 4, 5, 1).chance()


def test_yatzy_scores_50():
    expected = 50
    actual = Yatzy(4, 4, 4, 4, 4).yatzy()
    assert expected == actual
    assert 50 == Yatzy(6, 6, 6, 6, 6).yatzy()
    assert 0 == Yatzy(6, 6, 6, 6, 3).yatzy()


def test_1s():
    assert Yatzy(1, 2, 3, 4, 5).ones() == 1
    assert 2 == Yatzy(1, 2, 1, 4, 5).ones()
    assert 0 == Yatzy(6, 2, 2, 4, 5).ones()
    assert 4 == Yatzy(1, 2, 1, 1, 1).ones()
    assert 5 == Yatzy(1, 1, 1, 1, 1).ones()


def test_2s():
    assert 4 == Yatzy(1, 2, 3, 2, 6).twos()
    assert 10 == Yatzy(2, 2, 2, 2, 2).twos()
    assert 0 == Yatzy(1, 4, 3, 5, 6).twos()


def test_threes():
    assert 3 == Yatzy(3, 2, 1, 2, 5).threes()
    assert 6 == Yatzy(1, 2, 3, 2, 3).threes()
    assert 12 == Yatzy(2, 3, 3, 3, 3).threes()


def test_fours_test():
    assert 12 == Yatzy(4, 4, 4, 5, 5).fours()
    assert 8 == Yatzy(4, 4, 5, 5, 5).fours()
    assert 4 == Yatzy(4, 5, 5, 5, 5).fours()


def test_fives():
    assert 10 == Yatzy(4, 4, 4, 5, 5).fives()
    assert 15 == Yatzy(4, 4, 5, 5, 5).fives()
    assert 20 == Yatzy(4, 5, 5, 5, 5).fives()


def test_sixes_test():
    assert 0 == Yatzy(4, 4, 4, 5, 5).sixes()
    assert 6 == Yatzy(4, 4, 6, 5, 5).sixes()
    assert 18 == Yatzy(6, 5, 6, 6, 5).sixes()


def test_one_pair():
    assert 6 == Yatzy(3, 4, 3, 5, 6).score_pair()
    assert 10 == Yatzy(5, 3, 3, 3, 5).score_pair()
    assert 12 == Yatzy(5, 3, 6, 6, 5).score_pair()
    assert 0 == Yatzy(1, 2, 3, 4, 5).score_pair()


def test_two_Pair():
    assert 16 == Yatzy(3, 3, 5, 4, 5).two_pair()
    assert 18 == Yatzy(3, 3, 6, 6, 6).two_pair()
    assert 0 == Yatzy(3, 3, 6, 5, 4).two_pair()


def test_three_of_a_kind():
    assert 9 == Yatzy(3, 3, 3, 4, 5).three_of_a_kind()
    assert 15 == Yatzy(5, 3, 5, 4, 5).three_of_a_kind()
    assert 9 == Yatzy(3, 3, 3, 3, 5).three_of_a_kind()
    assert 0 == Yatzy(1, 2, 3, 4, 5).three_of_a_kind()


def test_four_of_a_knd():
    assert 12 == Yatzy(3, 3, 3, 3, 5).four_of_a_kind()
    assert 20 == Yatzy(5, 5, 5, 4, 5).four_of_a_kind()
    assert 12 == Yatzy(3, 3, 3, 3, 3).four_of_a_kind()
    assert 0 == Yatzy(3, 3, 3, 2, 1).four_of_a_kind()


def test_smallStraight():
    assert 15 == Yatzy(1, 2, 3, 4, 5).smallStraight()
    assert 15 == Yatzy(2, 3, 4, 5, 1).smallStraight()
    assert 0 == Yatzy(1, 2, 2, 4, 5).smallStraight()


def test_largeStraight():
    assert 20 == Yatzy(6, 2, 3, 4, 5).largeStraight()
    assert 20 == Yatzy(2, 3, 4, 5, 6).largeStraight()
    assert 0 == Yatzy(1, 2, 2, 4, 5).largeStraight()


def test_fullHouse():
    assert 18 == Yatzy(6, 2, 2, 2, 6).fullHouse()
    assert 0 == Yatzy(2, 3, 4, 5, 6).fullHouse()
