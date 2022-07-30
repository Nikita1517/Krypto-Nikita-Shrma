from fastapi import FastAPI
import requests
import json

app = FastAPI()


#Function to load all data from JSON file
def load_data():
    with open('sample.json') as f:
        return json.load(f)

json_data=load_data()

#Function to save data into the JSON file
def save_data(json_data):
    with open('sample.json', 'w') as f:
        json.dump(json_data, f, indent=4)

#Function to return status and price of an alert
def get_alert_status_and_price(alert_name):
    resultList=[json_data[alert_name][0],json_data[alert_name][1]]
    return resultList

#Function to get all alerts from JSON
def get_all_alerts_data():
    return(json_data)

#Function to insert/update data in JSON file
def append_to_json(alert_name,alert_data):
    Dict={alert_name:alert_data}
    json_data[alert_name]=alert_data
    save_data(json_data)

#Function to delete data from JSON file. Keeping for future use
def delete_from_json(alert_name):
    del json_data[alert_name]
    save_data(json_data)

Dict = {}


@app.get("/")
def read_root():
    return {"Nikita Sharma": "VIT"}

@app.get("/getAllAlerts")
def get_All_Alerts():
    return get_all_alerts_data()

@app.get("/alerts/create")
def alert_create(target_price, alert_name):
    alert_data=[target_price,"Created"]
    append_to_json(alert_name,alert_data)
    return Dict

@app.get("/alerts/delete")
def alert_delete(alert_name):
    alert_data=get_alert_status_and_price(alert_name)
    if(alert_data[1]=="Deleted"):
        return("Alert is already deleted")
    alert_data[1]="Deleted"
    # delete_from_json(alert_name), removed this line to not deleted and just update the status
    append_to_json(alert_name,alert_data)
    return "Status updated to Delete"


@app.get("/alerts/trigger")
def alert_trigger(alert_name):
    URL = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=USD&order=market_cap_desc&per_page=100&page=1&sparkline=false"
    response = requests.get(URL).json()
    current_price=response[0]['current_price']
    alert_data=get_alert_status_and_price(alert_name)

    if(alert_data[1]=="Deleted"):
        return("Alert is already deleted")
    message="No message"
    if(current_price==int(alert_data[0])):
        message = "Successfully sent an E-Mail"
        alert_data[1]="Triggered"
        append_to_json(alert_name,alert_data)
    else:
        message ="Current price is not same to trigger price"
    
    resultDict={"Current Price":current_price,"Trigger Price":int(alert_data[0]),"Status":alert_data[1],"Message":message}
    return resultDict