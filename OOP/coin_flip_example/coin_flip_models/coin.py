class Coin:
    # Define valid coin types and their corresponding monetary values (in dollars)
    VALID_COINS: dict[str, float] = {
        "nickel": 0.05,
        "dime": 0.10,
        "quarter": 0.25,
        "loonie": 1.00,
        "toonie": 2.00,
    }

    def __init__(self, name: str) -> None:
        # Convert to lowercase to make it case-insensitive (e.g., "Quarter" vs "quarter")
        normalized_name = name.lower()
        
        if normalized_name not in self.VALID_COINS:
            valid_options = ", ".join(self.VALID_COINS.keys())
            raise ValueError(f"Invalid coin type: '{name}'. Must be one of: {valid_options}")
            
        self.name: str = normalized_name
        self.value: float = self.VALID_COINS[normalized_name]

    # Representation of our object when we print it out in a string.
    def __str__(self) -> str:
        return self.name.title()

    def __repr__(self) -> str:
        return f"Coin('{self.name}')"

    # Two coins are considered equal if values (or names) match
    def __eq__(self, other: "Coin") -> bool:
        if not isinstance(other, Coin):
            return NotImplemented
        return self.value == other.value

    # A coin is "greater than" another if it is worth more
    def __gt__(self, other: "Coin") -> bool:
        if not isinstance(other, Coin):
            return NotImplemented
        return self.value > other.value

    # A coin is "less than" another if it is worth less
    def __lt__(self, other: "Coin") -> bool:
        if not isinstance(other, Coin):
            return NotImplemented
        return self.value < other.value