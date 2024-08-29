import requests
from colorama import Fore,init
import sys

print(f"{Fore.GREEN}-" * 50)

# Initialize colorama with autoreset
init(autoreset=True)

# Get the IP address from the user
IP = input(f"{Fore.GREEN}Enter the IP address: ")

if IP == "":
	IP = "localhost"

try:
    # Check if the server is alive
    response = requests.get(f"https://{IP}", timeout=5)

    if response.status_code != None:
        print(f"{Fore.GREEN}-" * 50)
        print(f"{Fore.GREEN}Server is alive")

        # Server is alive, now send the POST request                                                       
        post_response = requests.post(f"https://{IP}")

        if post_response.text:
            # Continue with further processing
            print(f"{Fore.GREEN}OK")
            print(f"{Fore.GREEN}-" * 50)
            # Your code here
        else:
            # Handle the case where there is no text response
            print(f"{Fore.RED}Error, closing...")
            # Your code here
            sys.exit()

    else:
        print(f"{Fore.RED}Server Error")
        sys.exit()

except requests.ConnectionError:
    print(f"{Fore.RED}-" * 50)
    print(f"{Fore.RED}Error,Failed to connect to the server.")
    print(f"{Fore.RED}-" * 50)
    sys.exit()
except requests.Timeout:
    print(f"{Fore.RED}Error,Request timed out.")
    sys.exit()







def send_otp(phone_number):
    url = f'https://{IP}/send_number'
    data = {'number': phone_number}

    response = requests.post(url, json=data)
    return response.json()

def verify_otp(phone_number, otp):
    url = f'https://{IP}/verify_otp'
    data = {'number': phone_number, 'otp': otp}

    response = requests.post(url, json=data)
    return response.json()

def main():
    # Ask the user for the phone number
    n = input(f"{Fore.GREEN}Enter the phone number: ")
    
    phone_number = n[1:]

    # Send the OTP
    print(f"{Fore.GREEN}-" * 50)
    print(f"{Fore.GREEN}Sending OTP...")
    print(f"{Fore.GREEN}-" * 50)
    otp_response = send_otp(phone_number)
    #print(otp_response)
    print(f"{Fore.GREEN}✓✓ OTP sent to {n}")
    print(f"{Fore.GREEN}-" * 50)



    # Check if OTP was sent successfully
    if 'message' in otp_response and otp_response['message'] == 'OTP sent successfully':
        # Wait for the user to enter the OTP
        otp = input(f"{Fore.GREEN}Enter the OTP you received: ")
        print(f"{Fore.GREEN}-" * 50)
        print(f"{Fore.GREEN}wait⏳")
        

        # Verify the OTP
        verification_response = verify_otp(phone_number, otp)
        #print(verification_response)
        if "error" in verification_response:
        	print(f"{Fore.RED}-" * 75)
        	print(f"{Fore.RED}Failed")
        	print(f"{Fore.RED}-" * 75)
        else:
        	print(f"{Fore.GREEN}-" * 50)
        	print(f"{Fore.GREEN}2Go")
        	print(f"{Fore.GREEN}-" * 50)
    else:
        print(f"{Fore.RED}Failed to send OTP. Please check the number and try again.")

if __name__ == '__main__':
    main()
