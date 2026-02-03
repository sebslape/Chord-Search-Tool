def get_ordinal(num):
    if num >= 11 and num <= 13:
        return f"{num}th"
    
    last_digit = num % 10
    suffixes = ["th", "st", "nd", "rd", "th"]

    return f"{num}{suffixes[min(last_digit, 4)]}"