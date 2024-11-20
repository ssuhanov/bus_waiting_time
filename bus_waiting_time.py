def time_to_string(seconds):
    minutes = seconds // 60
    minutes_to_string = str(minutes)
    if minutes < 10:
        minutes_to_string = "0" + minutes_to_string

    seconds_remainder = seconds % 60
    seconds_to_string = str(seconds_remainder)
    if seconds_remainder < 10:
        seconds_to_string = "0" + seconds_to_string

    return minutes_to_string + ":" + seconds_to_string

BUS_TIME_INTERVAL_IN_MINUTES = 10
bus_time_interval_in_seconds = BUS_TIME_INTERVAL_IN_MINUTES * 60

RANGE_FOR_ANALYSIS_IN_MINUTES = 60
range_for_analysis_in_seconds = RANGE_FOR_ANALYSIS_IN_MINUTES * 60

for i in range(range_for_analysis_in_seconds):
    current_second = i+1
    print(time_to_string(current_second))
    if current_second % bus_time_interval_in_seconds == 0:
        print("BUS ARRIVED!")
