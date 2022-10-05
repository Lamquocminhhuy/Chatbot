import json
import requests

### Get all services
# response = requests.get("https://canthogarage.pythonanywhere.com/api/services/").json()
# text = "Hiện tại bên em có {} dịch vụ mời quý khách tham khảo ạ.".format(len(response))

# for i in range(len(response)):

#   text += "\n" + "- " + response[i]["name"]


# print(text)

### Get information of service

# service = "thay lốp xe"

# response = requests.get("https://canthogarage.pythonanywhere.com/api/service/" + service.replace("dịch vụ", "").strip()  )
# print(response.json()["status"])

# if (response.status_code) == 200:
#     responseData = response.json()
#     print(responseData)

## Post booking 

booking_data = {       
    "user": "Minh", 
    "email": "lamquocminhhuy@gmail.com", 
    "phone_number": "0896617857", 
    "timeblock": "9:00", 
    "service": 2, 
    "date": "2022-10-05"
}
print(booking_data)
r = requests.post("https://canthogarage.pythonanywhere.com/api/booking/", data = json.dumps(booking_data, indent = 4))
print(r.text)