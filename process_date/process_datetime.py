import datetime
import pytz


timezone="Asia/Ho_Chi_Minh"

tz = pytz.timezone(timezone)
# Thời điểm hiện tại
now = datetime.datetime.now(tz=tz)
# Hôm nay
today = datetime.date(now.year, now.month, now.day)



def findDayByToken(token):
    if token == "hôm nay":
        date = today + datetime.timedelta(days=0)
    if token == "bữa nay":
        date = today + datetime.timedelta(days=0)
    if token == "ngày mai":
        date = today + datetime.timedelta(days=1)
    return [str(date)] 

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

    return daylist

def findDateOfWeek(nameOfDay):
    daylist = generate_daylist()
    data = nameOfDay.upper()

    for day in daylist:
        if data in day['day']:
            return [day['date']]
            
    return -1
    


