import requests
import time
from tabulate import tabulate

# Example list of subdomains to check
subdomains = [
    "http://www.google.com",            # Should be up
    "http://drive.google.com",          # Should be up
    "http://nonexistent.google.com",    # Should be down (fake subdomain)
    "http://www.github.com",            # Should be up
    "http://api.github.com",            # Should be up
    "http://nonexistent.github.com",    # Should be down (fake subdomain)
    "http://www.facebook.com",          # Should be up
    "http://nonexistent.facebook.com"   # Should be down (fake subdomain)
]

def check_status(subdomains):
    status_data = []
    for subdomain in subdomains:
        try:
            response = requests.get(subdomain, timeout=5)
            status = "Up" if response.status_code == 200 else f"Down (Status Code: {response.status_code})"
        except requests.exceptions.RequestException as e:
            status = f"Down (Error: {e})"
        
        status_data.append([subdomain, status])
    
    return status_data

def display_status(status_data):
    print("\nSubdomain Status:\n")
    print(tabulate(status_data, headers=["Subdomain", "Status"], tablefmt="pretty"))

def main():
    while True:
        status_data = check_status(subdomains)
        display_status(status_data)
        print("\nUpdating status in 60 seconds...\n")
        time.sleep(60)

if __name__ == "__main__":
    main()
