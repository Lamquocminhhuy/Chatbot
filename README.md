
## Garage Chabot
With Rasa Open Source
## Commands

```
rasa run actions
rasa shell 
rasa run -m models --enable-api --cors "*" --debug
```

### Install Rasa and Rasa X
```
pip3 install rasa==2.8.2
pip3 install rasa-sdk==2.8.1
pip3 install rasa-x==0.39.3 --extra-index-url https://pypi.rasa.com/simple
```
#### If error occur, install these libs
```
pip3 install SQLAlchemy==1.3.22
pip3 install sanic-jwt==1.6.0
```
Links: https://forum.rasa.com/t/rasa-x-runs-with-several-errors-warnings/49006/8

### Featured
1. Ask all services
2. Get time working of garage
3. Get specific services information (description, price, time_todo)
4. Chitchat
5. Booking (in progress)
