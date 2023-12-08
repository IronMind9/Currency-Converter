import requests

initial_currency = input("Enter the initial currency: ")
target_currency = input("Enter the target currency: ")

while True:
    try:
        amount = float(input("Enter the amount: "))
        if amount <= 0:
            print("The amount must be greater than zero.")
            continue
        break
    except ValueError:
        print("Please enter a numeric value for the amount.")

url = f"https://api.apilayer.com/fixer/convert?to={target_currency}&from={initial_currency}&amount={amount}"

payload = {}
headers = {
    "apikey": "3KTEhcDI23OEo7gkizedfOaF0t2sGMgk"
}

response = requests.get(url, headers=headers, data=payload)

status_code = response.status_code

if status_code != 200:
    print(f"Sorry, there was a problem. Status code: {status_code}")
    print(response.text)  # Print the response text for more details
    quit()

result = response.json()
converted_amount = result['result']
print(f'{amount} {initial_currency} = {converted_amount} {target_currency}') 

