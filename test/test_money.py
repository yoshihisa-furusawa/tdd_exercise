from src.money import Money


def test_multiplication():
    """Test multiplication"""
    five = Money.dollar(5)
    assert Money.dollar(10) == five.times(2)
    assert Money.dollar(15) == five.times(3)


def test_equality():
    """test equality between objects"""
    assert Money.dollar(5) == Money.dollar(5)
    assert Money.dollar(5) != Money.dollar(6)


def test_currency():
    """test currency"""
    assert Money.dollar(1).currency == "USD"
    assert Money.franc(1).currency == "CHF"


def test_amount():
    """test amount"""
    assert Money.dollar(1).amount == 1


def test_equality_between_diff_objects():
    """test equality between objects"""
    assert Money.franc(5) != Money.dollar(5)


def test_sum_dollar():
    """test summation between objects"""
    dollar_1 = Money.dollar(5)
    dollar_2 = Money.dollar(5)
    summary = dollar_2.plus(dollar_1)
    assert Money.dollar(10) == summary
