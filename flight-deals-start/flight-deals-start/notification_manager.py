from twilio.rest import Client
class NotificationManager:
    def __init__(self, account_sid, auth_token):
        self.client = Client(account_sid, auth_token)

    def send_message(self, flight):
        body = (f"Low price alert! Only €{flight["price"]} to fly from "
                f"{flight["departure_city"]}-{flight["departure_airport"]} "
                f"to {flight["destination_city"]}-{flight["destination_airport"]}, "
                f"from {flight["date_from"]} to {flight["date_to"]}")
        message = self.client.messages.create(
            from_="+12679332335",
            body=body,
            to="+447927462101",
        )
        print(message.status)



