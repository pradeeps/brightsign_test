import argparse
import requests
import os


def get_mac_company(mac_address, api_key):
    headers = {"X-Authentication-Token": api_key}
    url = f"https://api.macaddress.io/v1?search={mac_address}"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        return response.text


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "mac_address", help="Please input the MAC address to query Company name"
    )
    parser.add_argument(
        "--api_key",
        help="Please input the API_KEY if you are running the script standalone",
    )

    args = parser.parse_args()

    env_api_key = os.getenv("API_KEY")

    if args.api_key:
        api_key = args.api_key
    elif env_api_key:
        api_key = env_api_key
    else:
        print("API key required")
        exit(1)

    result = get_mac_company(args.mac_address, api_key)
    if result:
        print(f"Company name for the MAC address {args.mac_address} is {result}")
    else:
        print(f"{result}")
