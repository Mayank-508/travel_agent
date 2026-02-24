def estimate_trip_cost(destination: str, duration: int, hotel_cost_per_night: float, transport_cost: float) -> str:
    """
    Estimates the total trip cost including a safety buffer.
    """
    total_cost = (duration * hotel_cost_per_night) + transport_cost
    buffer_cost = total_cost * 1.1 # 10% safety buffer
    return f"Estimated trip cost to {destination} for {duration} days is ${buffer_cost:.2f} (includes 10% buffer)."
