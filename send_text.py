from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC0a6e858ede1ab1c5c2d9a435ccdab5fc"
# Your Auth Token from twilio.com/console
auth_token  = "ad945a57b743a87d6383e70797b2d08b"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+917017575013", 
    from_="+13362030331",
    body="Hello from, Anuj Singh!")

print(message.sid)
