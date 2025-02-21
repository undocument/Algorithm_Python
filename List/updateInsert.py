integer =[1,2,4,5,7]

print(integer)

print(integer.insert(1,4))




def convert_to_military_time(time_str):
    # Extract hour, minutes, seconds, and AM/PM part
    hour, minute, second_am_pm = time_str[:-2].split(':')
    am_pm = time_str[-2:]

    # Convert hour to integer
    hour = int(hour)

    # Handle AM/PM conversion
    if am_pm == "AM":
        if hour == 12:
            hour = 0  # Midnight case: 12AM -> 00
    else:  # PM case
        if hour != 12:
            hour += 12  # Convert PM hours except 12PM

    # Format the military time
    return f"{hour:02}:{minute}:{second_am_pm}"

# Example usage
time_12hr = "07:05:45PM"
time_24hr = convert_to_military_time(time_12hr)
print(time_24hr)