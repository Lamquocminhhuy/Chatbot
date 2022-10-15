import datetime
import calendar
import pytz


timezone="Asia/Ho_Chi_Minh"

tz = pytz.timezone(timezone)
# Thời điểm hiện tại
now = datetime.datetime.now(tz=tz)
# Hôm nay
today = datetime.date(now.year, now.month, now.day)

token = "tomorrow" ## get from bot


def ngaymaihomnay(token):
    if token == "hôm nay":
        date = today + datetime.timedelta(days=0)
    if token == "bữa nay":
        date = today + datetime.timedelta(days=0)
    if token == "ngày mai":
        date = today + datetime.timedelta(days=1)
    return [date] 


def generate_daylist():
    daylist = []
    today = datetime.date.today()
    map = {
    "MONDAY": ["THỨ 2", "THỨ HAI"],
    "TUESDAY": ["THỨ 3", "THỨ BA"],
    "WEDNESDAY": ["THỨ 4", "THỨ TƯ"],
    "THURSDAY": ["THỨ 5", "THỨ NĂM"],
    "FRIDAY": ["THỨ 6", "THỨ SÁU"],
    "SATURDAY": ["THỨ 7", "THỨ BẢY"],
    "SUNDAY": ["CHỦ NHẬT", "CN"]
    }   
    for i in range(7):
        day = {}
        curr_day = today + datetime.timedelta(days=i)
        weekday = curr_day.strftime("%A").upper()

        day["date"] = str(curr_day)
        day['day'] = map[weekday]

        if day["day"] != "SATURDAY":  
            daylist.append(day)
    
    # print(daylist)
    return daylist
    
def findDate(nameOfDay):
    daylist = generate_daylist()
    data = nameOfDay.upper()


    
    for day in daylist:
        if data in day['day']:
            return [day['date']]
            
    return -1
    
user_input = "Thứ 6"


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
            