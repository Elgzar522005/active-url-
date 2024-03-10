import re
import requests

def print_available_links(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        https_pattern = re.compile(r'https://\S+')

        https_links = https_pattern.findall(content)

        print("Available links in the file:")
        for link in https_links:
            try:
                response = requests.head(link)
                if response.status_code == 200:
                    print(link)
            except requests.ConnectionError:
                pass 

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")

file_path = input("Enter the path to the file: ")

print_available_links(file_path)