from twilio.rest import Client

print("Enter 'x' for exit.");
print("Enter any two numbers: ");
num1 = input();
if num1 == 'x':
    exit();
else:
    num2 = input();
    number1 = int(num1);
    number2 = int(num2);
    count = 0;
    if number1 > number2:
    	largest = number1;
    	count = 1;
    elif number1 < number2:
    	largest = number2;
    	count = 1;
    else:
        print("\nBoth the numbers are equal to each other.");
    if count == 1:
        print("\nLargest of the given two numbers is", largest);
        account_sid = 'AC6f360c53ed36540386f12a136cf90075'
        auth_token = 'fc6eb168bbf9038c10027d5847d9b2a5'
        client = Client(account_sid, auth_token)
        
        message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+12023183287',
                     to='+919145581103'
                 )
        print(message.sid)