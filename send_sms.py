from twilio.rest import Client

# Your Twilio Account SID and Auth Token from https://console.twilio.com/
account_sid = "AC40ecb3017d3bf1607d435d0c87b03390"
auth_token = "bd44e3b64307ebc1f754f2c04aed4b24"
msg_service_sid = "MGe6221776f15adb440663a3adc7060ff2"  # starts with "MG"
client = Client(account_sid, auth_token)



message = client.messages.create(
    messaging_service_sid=msg_service_sid,
    to="+818040832003",  # destination in E.164
    body="Hello from Twilio via Messaging Service 🚀"
)

print("SID:", message.sid)

