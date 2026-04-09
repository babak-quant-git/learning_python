from dataclasses import dataclass


@dataclass
class Order:
    price: float
    volume: int


def analyze_lob(bids: list[Order], asks: list[Order]) -> tuple[float, float]:
    """Calculate spread and mid-price from bid and ask orders."""

    best_bid = max(order.price for order in bids)
    best_ask = min(order.price for order in asks)

    spread = best_ask - best_bid
    mid_price = (best_ask + best_bid) / 2

    return spread, mid_price


if __name__ == "__main__":
    bids: list[Order] = [
        Order(price=100.5, volume=10),
        Order(price=101.2, volume=7),
        Order(price=99.9, volume=15),
    ]

    asks: list[Order] = [
        Order(price=101.8, volume=12),
        Order(price=102.4, volume=9),
        Order(price=101.5, volume=6),
    ]

    spread, mid_price = analyze_lob(bids, asks)

    print(f"Spread: {spread}")
    print(f"Mid-price: {mid_price}")
