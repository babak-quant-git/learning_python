def calculate_net_pnl(trades: list[tuple[float, int, bool]], fee_rate: float) -> float:
    """Calculate aggregate net PnL for a list of trades, including trading fees."""
    total_pnl: float = 0.0

    for price, volume, is_buy in trades:
        gross_cash_flow = -price * volume if is_buy else price * volume
        fee = price * volume * fee_rate
        net_cash_flow = gross_cash_flow - fee
        total_pnl += net_cash_flow

    return total_pnl


if __name__ == "__main__":
    trades: list[tuple[float, int, bool]] = [
        (100.0, 10, True),
        (110.0, 10, False),
        (50.0, 4, True),
    ]
    fee_rate: float = 0.001

    print(round(calculate_net_pnl(trades, fee_rate), 4))
