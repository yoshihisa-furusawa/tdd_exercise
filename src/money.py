class Money:
    def __init__(self, amount: int, currency: str):
        self._amount = amount
        self._currency = currency

    def times(self, num: int) -> "Money":
        return Money(self._amount * num, self._currency)

    @property
    def amount(self):
        return self._amount

    @property
    def currency(self):
        return self._currency

    def __eq__(self, other: "Money") -> bool:
        return (self.amount == other.amount) & (self.currency == other.currency)

    @classmethod
    def dollar(cls, num: int) -> "Money":
        return Money(num, "USD")

    @classmethod
    def franc(cls, num: int) -> "Money":
        return Money(num, "CHF")

    def plus(self, other: "Money") -> "Money":
        return Money(self.amount + other.amount, self.currency)
