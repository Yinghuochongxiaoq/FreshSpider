#pip install twilio 安装包
from twilio.rest import Client

account_sid = ""
auth_token = ""
client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+861888888888888888888",
    from_="+1888888888888803122",
    body="早饭开始了"
)

print(message.sid)
