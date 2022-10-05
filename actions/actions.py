import json
import requests
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import FollowupAction
from process_date import format_date, process_datetime

## Response all services when user ask for all services
class ActionRecommend(Action):

    def name(self) -> Text:
        return "action_ask_services"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        response = requests.get("https://canthogarage.pythonanywhere.com/api/services/").json()
        text = "Hiện tại bên em có {} dịch vụ mời quý khách tham khảo ạ.".format(len(response))
        url = "[Chi tiết](https://canthogarage.pythonanywhere.com/service/{})"

        for i in range(len(response)):
         
            text += "\n" + "- " + response[i]['name'] + " " + "(" + url.format(response[i]['id']) +")"
        
        dispatcher.utter_message(text)

        return []

## Response service price when user intent ask price
class ActionPrice(Action):

    def name(self) -> Text:
        return "action_ans_price"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
      
      
        print(str(tracker.latest_message['entities'][0]['value']) + " (hỏi giá)")
        service = str(tracker.latest_message['entities'][0]['value'])
        response = requests.get("https://canthogarage.pythonanywhere.com/api/service/" + service)
      
        if (response.status_code) == 200:
            responseData = response.json()
        
            text = "Dạ hiện tại dịch vụ {} có giá là {}k. Ngoài ra nếu quý khách đến trong hôm nay thì giá chỉ còn {}k ạ".format(responseData['name'], responseData['price'], int(responseData['price'])//2 )
        else:
            text = "Dạ hệ thống đang có tí trục trặc quý khách vui lòng phản hồi lại sau chốc lát ạ"


        dispatcher.utter_message(text)
        return []

## Response service deatail when user asked - call action_ask_services if service is not in database
class ActionResponseServiceDetail(Action):

    def name(self) -> Text:
        return "action_ans_service_detail"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
      
      
        # print(str(tracker.latest_message['entities'][0]['value']))
        try:
            service = str(tracker.latest_message['entities'][0]['value'])
        except: 
            service = "null"

        print(service + " (hỏi chi tiết dịch vụ)")
 
        response = requests.get("https://canthogarage.pythonanywhere.com/api/service/" + service.replace("dịch vụ", "").strip())
        if(response.status_code == 200):
            responseData = response.json()
            text = "Dạ là {}".format(responseData['description'].lower())
        else    :
            text = "Dạ garage bên em không có dịch vụ đó ạ."
          
            dispatcher.utter_message(text)
        
            return [FollowupAction("action_ask_services")]

        dispatcher.utter_message(text)
        return []
       
## Response service time in minutes or hours
class ActionAskTime(Action):

    def name(self) -> Text:
        return "action_ans_service_time"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
      
      
        # print(str(tracker.latest_message['entities'][0]['value']))
        service = str(tracker.latest_message['entities'][0]['value'])
        print(service + " (hỏi thời gian thực hiện")
        try:
            time_unit = str(tracker.latest_message['entities'][1]['value']) 
        except:
            time_unit = ""

        response = requests.get("https://canthogarage.pythonanywhere.com/api/service/" + service.replace("dịch vụ", "").strip())
        if(response.status_code == 200):
            responseData = response.json()
            if (time_unit == "tiếng"):
                text = "Dạ dịch vụ {} sẽ được bên garage làm trong khoảng {} tiếng ạ.".format(responseData['name'], int(responseData['time_todo'])//60)
            elif (time_unit == "phút" ):
                text = "Dạ dịch vụ {} sẽ được bên garage làm trong khoảng {} phút ạ.".format(responseData['name'], int(responseData['time_todo']))
            elif (time_unit == "giờ" ):
                text = "Dạ dịch vụ {} sẽ được bên garage làm trong khoảng {} giờ ạ.".format(responseData['name'], int(responseData['time_todo']//60))
            else:
                text = "Dạ thời gian hoàn thành dịch vụ {} sẽ tùy vào tình trạng xe ạ.".format(responseData['name'])
        else:
            text = "Dạ hệ thống đang có tí trục trặc quý khách vui lòng phản hồi lại sau chốc lát ạ"


        dispatcher.utter_message(text)
        return []

class ActionBookingForm(Action):

    def name(self) -> Text:
        return "action_booking_submit"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
      

        booking_data = {} # init 
        booking_data["user"] = tracker.get_slot("name") 
        booking_data["email"] = tracker.get_slot("email")
        booking_data["phone_number"] = tracker.get_slot("phone")


        if tracker.get_slot("service") and tracker.get_slot("time") != "":
            try:
                response = requests.get("https://canthogarage.pythonanywhere.com/api/service/" + tracker.get_slot("service").strip())

                responseData = response.json()

                booking_data["service"] = responseData["id"]
                dayofweek = ["thứ 2","thứ 3","thứ 4","thứ 5","thứ 6","thứ 7","chủ nhật", "thứ hai","thứ ba","thứ tư","thứ năm","thứ sau","thứ bảy"]

                if tracker.get_slot("date").strip().lower() == "ngày mai" or tracker.get_slot("date").strip().lower() == "hôm nay":

                    date_format = process_datetime.ngaymaihomnay(tracker.get_slot("date"))

                elif tracker.get_slot("date").strip().lower() in dayofweek:
                    print("Hello")
                    date_format = process_datetime.findDate(tracker.get_slot("date").strip().lower()) 
                else: 
                    date_format = format_date.regex_date(tracker.get_slot("date").strip().lower())


                time_format = process_datetime.process_time(tracker.get_slot("time").strip().lower())

           
                booking_data["date"] = date_format[0]
                booking_data["timeblock"] = time_format 
                #print(booking_data)
                r = requests.post("https://canthogarage.pythonanywhere.com/api/booking/", data = json.dumps(booking_data, indent = 4))

                text = "Em xin chốt lại thông tin đặt lịch của quý khách:\n- Tên khách hàng: {}\n- Ngày đặt: {} lúc {} giờ\n- Dịch vụ: {}\n- Email: {}\n- SĐT: {}\n"

                dispatcher.utter_message(text.format(booking_data["user"], booking_data["date"], booking_data["timeblock"], tracker.get_slot("service"), booking_data["email"], booking_data["phone_number"]))

            except:
                dispatcher.utter_message("Có tí trục trặc với hệ thống quý khách đặt lịch sau nha")

        return []