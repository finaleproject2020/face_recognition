from twilio.rest import Client
account_sid='AC1f00baff608ec9f894f64b47b3c0ebc4'
auth_token='bb512b4d02d68603b2ffe8e2016a8093'
client = Client(account_sid, auth_token)
my_msg=''.join(['Rahul here.......\n' for i in range(20)])
client.api.account.messages.create(
    to="+91866001755",
    from_="+19852511899",
    body=my_msg)
