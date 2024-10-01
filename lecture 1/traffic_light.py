def next_color(col: str)->str:
    """Takes a light color and returns the next one in a row.
    "red"->"orange"->"green"
    """
    if col=="red":
        return "orange"
    elif col=="orange":
        return "green"
    else:
        return "red"

def is_valid_color(col: str)->bool:
    """Checks if the color can be a traffic light color."""
    return col=="red" or col=="orange" or col=="green"

print(is_valid_color("red") == True)
print(is_valid_color("green") == True)
print(is_valid_color("orange") == True)
print(is_valid_color("orange") == False)