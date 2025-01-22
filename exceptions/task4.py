def alarm_clock(day, vacation):
    try:
        if not 0 <= day <= 6:
            raise ValueError("Invalid day value.")
        if vacation:
            if day in [0, 6]:
                return "off"
            else:
                return "10:00"
        else:
            if day in [0, 6]:
                return "10:00"
            else:
                return "7:00"
    except ValueError as e:
        return f"Error: {str(e)}"

print(alarm_clock(1, False))  # '7:00'
print(alarm_clock(5, False))  # '7:00'
print(alarm_clock(0, False))  # '10:00'
print(alarm_clock(0, True))   # 'off'
print(alarm_clock(3, True))   # '10:00'
