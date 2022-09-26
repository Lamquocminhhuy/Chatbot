from typing import Any, Text, Dict, List
from urllib import request, response

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests



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
      
      
        print(str(tracker.latest_message['entities'][0]['value']))
        service = str(tracker.latest_message['entities'][0]['value'])
        response = requests.get("https://canthogarage.pythonanywhere.com/api/service/" + service)
      
        if (response.status_code) == 200:
            responseData = response.json()
        
            text = "Dạ hiện tại dịch vụ {} có giá là {}k. Ngoài ra nếu quý khách đến trong hôm nay thì giá chỉ còn {}k ạ".format(responseData['name'], responseData['price'], int(responseData['price'])/50 )
        else:
            text = "Dạ hệ thống đang có tí trục trặc quý khách vui lòng phản hồi lại sau chốc lát ạ"


        dispatcher.utter_message(text)
        return []


