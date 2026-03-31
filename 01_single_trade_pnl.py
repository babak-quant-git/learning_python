def calculate_trade_value(price: float, volume: int, is_buy: bool) -> float:
    """Calculate trade cash flow."""

    return -price * volume if is_buy else price * volume


if __name__ == "__main__":
    trades: list[tuple[float, int, bool]] = [
        (100.0, 10, True),
        (100.0, 10, False),
        (12.5, 4, True),
    ]

    for price, volume, is_buy in trades:
        print(calculate_trade_value(price, volume, is_buy))
