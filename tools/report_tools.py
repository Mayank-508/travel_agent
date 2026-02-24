def generate_itinerary_report(destination: str, day_wise_plan: dict) -> str:
    """
    Generates a formatted markdown report for the generated itinerary.
    """
    report = f"# Multi-Agent Travel Itinerary: {destination}\n\n"
    for day, activities in day_wise_plan.items():
        report += f"## Day {day}\n"
        for activity in activities:
            report += f"- {activity}\n"
    
    return report
