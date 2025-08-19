from twilio.rest import Client

# Your Twilio Account SID and Auth Token from https://console.twilio.com/
account_sid = "AC83f5064c6436526612639e5206eac1e4"
auth_token = "c6cdd1aa0c7521542e4474f26e592149"
msg_service_sid = "MGc1f422505413a6da99d214023a77c8bb"  # starts with "MG"
api_key_sid = "SK31ba400dea33c2777f8ab5a31d0e30ce"   # From Console
api_key_secret = "LQW0RHmF2zr8L0GRRgpBEr7bsSsMsPma"    

client = Client(api_key_sid, api_key_secret, account_sid)

message = client.messages.create(
    messaging_service_sid=msg_service_sid,
    to="+818040832003",  # destination in E.164
    body="Hello from Twilio via Messaging Service 🚀"
)

print("SID:", message.sid)

