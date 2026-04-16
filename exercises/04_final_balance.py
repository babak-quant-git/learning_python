def final_balance(
    init_sum: int, interest_rate: float, years: int, round_num: int = 2
) -> float:
    """Return the balance after yearly compound interest."""

    balance: float = init_sum * (1 + interest_rate / 100) ** years

    return round(balance, round_num)
