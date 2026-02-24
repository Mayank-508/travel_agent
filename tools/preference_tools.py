def extract_user_preferences(user_input: str) -> dict:
    """
    Parses natural language user input into structured travel preferences.
    """
    print(f"[Tool: extract_user_preferences] Parsing input: '{user_input}'")
    
    # Simulated extraction
    return {
        "destination": "Tokyo",
        "budget": 2000,
        "duration": 5,
        "interests": ["Sushi", "Temples", "Technology"]
    }
