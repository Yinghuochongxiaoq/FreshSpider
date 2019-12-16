#pip install twilio 安装包
from twilio.rest import Client

account_sid = "AC646ce60346d5ae69004260e4b185cd4b"
auth_token = "63bfee3ec94c95df75e4c2d66a1d03b3"
client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+8618883257311",
    from_="+18508803122",
    body="早饭开始了"
)

print(message.sid)