# Krypto-Nikita-Shrma
System requirements:
1.      Python 3
2.      FastAPI module – use pip install fastapi
3.      Uvicorn[standard] – use pip install "uvicorn[standard]”
Endpoints :
![image](https://user-images.githubusercontent.com/73489837/181866097-de312a92-1a93-4559-9352-670641d36991.png)


1.      GetAllAlerts (http://127.0.0.1:8000/getAllAlerts) : This is fetch all alerts with trigger price and status.

 ![WhatsApp Image 2022-07-30 at 7 33 34 AM](https://user-images.githubusercontent.com/73489837/181866168-ea59f0a9-4d69-44d8-b6fc-28b70e3ddbc8.jpeg)


2.      Create alert (http://127.0.0.1:8000/alerts/create?target_price=argument1&alert_name=argument2)
Arguments – “target_price” and “alert_name”
Users can provide trigger price in the target_price and name of alert in alert_name.

![WhatsApp Image 2022-07-30 at 7 33 42 AM](https://user-images.githubusercontent.com/73489837/181866201-69aa833c-4abc-4e4b-ad74-95cb4150eafd.jpeg)


3.      Delete alert (http://127.0.0.1:8000/alerts/delete?alert_name=argument1)
Argument – “alert_name”
User can provide alert name and it’s status will be updated to deleted

![WhatsApp Image 2022-07-30 at 7 33 50 AM](https://user-images.githubusercontent.com/73489837/181866225-d88f07ae-2ea1-47d9-b5fc-5b0967a1f29c.jpeg)


4.      Trigger alert(http://127.0.0.1:8000/alerts/trigger?alert_name=argument1)
Argument- “alert_name”
User can provide alert name and then this endpoint will look if trigger price is reached. Based on the check it will return different response.

![WhatsApp Image 2022-07-30 at 7 36 29 AM](https://user-images.githubusercontent.com/73489837/181866247-85c2efc5-4390-4489-9725-1a8fab49a0c1.jpeg)

To run the project:
1.      Run below command in Powershell:
uvicorn fastkrypto:app –reload
2.      Go to http://127.0.0.1:8000/docs in the browser. It will open a swagger UI, here we can execute the above endpoints.
 
To execute an endpoint:
Step 1

![WhatsApp Image 2022-07-30 at 7 36 37 AM](https://user-images.githubusercontent.com/73489837/181866267-758f99e3-b882-47bf-8ae8-94ab3d648ffe.jpeg)

Step 2
Putting arguments and then click on execute button

![WhatsApp Image 2022-07-30 at 7 36 44 AM](https://user-images.githubusercontent.com/73489837/181866279-cbc2f6dd-4535-4931-aafe-ee440c2ff39c.jpeg)

  
Possible enhancements:
1.      Add validation for dirty data in all endpoints
2.      Add functionality for sending mail
3.      Caching data while fetching from database. We can clear the cache key on any update on the data.
 

