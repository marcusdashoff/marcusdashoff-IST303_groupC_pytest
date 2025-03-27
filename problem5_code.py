import re

# THANKS TO https://regex101.com

def parse_time_expression(expression):
    if not isinstance(expression, str):
        raise ValueError("expression must be a string")

    expression = expression.lower()
    
    expression = expression.replace('noon', '12').replace('midnight', '0')
     
    # if normal number
    match = re.match(r'^(\d{1,2})$', expression)
    if match:
        hour = int(match.group(1))
        return (hour, 0)
     
    match = re.match(r'^(\d{1,2}):(\d{1,2})$', expression)
    if match:
        hour = int(match.group(1))
        minute = int(match.group(2))
        return (hour, minute)
    
    match = re.match(r'^(zero|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty|twenty one|twenty two|twenty three)$', expression)
    if match:
        words_to_numbers = {
            "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
            "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10,
            "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14,
            "fifteen": 15, "sixteen": 16, "seventeen": 17, "eighteen": 18,
            "nineteen": 19, "twenty": 20, "twenty one": 21, "twenty two": 22,
            "twenty three": 23
        }
        hour = words_to_numbers[match.group(1)]
        return (hour, 0)
    
    match = re.match(r'^(\d{1,2})(?::(\d{1,2}))?\s*(am|pm)$', expression)
    if match:
        hour = int(match.group(1))
        minute = int(match.group(2)) if match.group(2) else 0
        am_or_pm = match.group(3)
        if am_or_pm == 'pm' and hour != 12:
            hour += 12
        # i hate this special case. da heck!
        elif am_or_pm == 'am' and hour == 12:
            hour = 0
        hour = hour % 24
        return (hour, minute)

    match = re.match(r'^(quarter|half)\s+(past|to)\s+(\d{1,2})$', expression)
    if match:
        minute = 15 if match.group(1) == 'quarter' else 30
        hour = int(match.group(3))
        
        # well we have to back trace
        if match.group(2) == 'to':
            hour = (hour - 1) % 24
            minute = 60 - minute

        return (hour, minute)
    
    return None
    
    
    