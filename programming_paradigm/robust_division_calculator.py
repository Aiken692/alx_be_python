def safe_divide(numerator, denominator):
    """Perform division and handle errors for division by zero and non-numeric inputs."""
    try:
        # Convert inputs to float
        num = float(numerator)
        denom = float(denominator)

        # Check for division by zero
        if denom == 0:
            return "Error: Cannot divide by zero."
        
        # Perform division and format the result to 1 decimal place without unnecessary zeros
        result = num / denom
        return f"The result of the division is {result:.1f}".rstrip('0').rstrip('.')
    
    except ValueError:
        # Handle non-numeric input
        return "Error: Please enter numeric values only."
