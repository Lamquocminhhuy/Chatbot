
def process_time(time):
    time_dict = {
    "8:00": ["8 giờ", "8h"],
    "9:00": ["9 giờ", "9h"],
    "10:00": ["10 giờ", "10h"],
    "11:00": ["11 giờ", "11h"],
    "1:00": ["1 giờ", "1h"],
    "2:00": ["2 giờ", "2h"],
    "3:00": ["3 giờ", "3h"],
    "4:00": ["4 giờ", "4h"],
    "5:00": ["5 giờ", "5h"],
    }
    
    for t in time_dict:
        if time in time_dict[t]:
            return t
            