import hashlib
from datetime import datetime
import os


def calculate_hash(file_path):
    with open(file_path, "rb") as file:
        file_data = file.read()

    return hashlib.sha256(file_data).hexdigest()


def write_log(message):
    with open("integrity_log.txt", "a") as log_file:
        log_file.write(message + "\n")


file_path = input("Enter file path: ")

baseline_file = "baseline_hash.txt"

try:
    current_hash = calculate_hash(file_path)
    check_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if not os.path.exists(baseline_file):
        with open(baseline_file, "w") as file:
            file.write(current_hash)

        message = f"{check_time} | BASELINE CREATED | {file_path}"

        print("\nBaseline created successfully.")
        print("File:", file_path)
        print("SHA-256 Hash:", current_hash)
        print("Check time:", check_time)

        write_log(message)

    else:
        with open(baseline_file, "r") as file:
            original_hash = file.read().strip()

        print("\nFile:", file_path)
        print("Check time:", check_time)

        print("\nOriginal SHA-256 Hash:")
        print(original_hash)

        print("\nCurrent SHA-256 Hash:")
        print(current_hash)

        if current_hash == original_hash:
            message = f"{check_time} | NO CHANGE | {file_path}"

            print("\n[+] File integrity verified. No changes detected.")

        else:
            message = f"{check_time} | MODIFIED | {file_path}"

            print("\n[!] WARNING: File has been modified!")

        write_log(message)

except FileNotFoundError:
    print("\n[!] Error: File not found.")

except PermissionError:
    print("\n[!] Error: Permission denied. Unable to access the file.")

except OSError as error:
    print(f"\n[!] Error while accessing the file: {error}")