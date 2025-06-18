# TriBrute - ZIP Password Brute Force Tool

*Nếu bạn quên mật khẩu, hãy thử khôi phục nó như một hacker - với mục đích học tập và đạo đức.  
"If you forgot the password, recover it like a hacker – for educational and ethical purposes only.

---

# Giới thiệu | Introduction

TriBrute là một công cụ đơn giản viết bằng Python dùng để brute-force (thử mật khẩu liên tục) trên các file ZIP,... được bảo vệ bằng mật khẩu.  
Công cụ hoạt động bằng cách tự động nhập từng mật khẩu từ một danh sách vào cửa sổ yêu cầu mật khẩu của file ZIP,...

*TriBrute is a simple brute-force tool written in Python to recover password-protected ZIP files,...  
*It works by automatically typing passwords from a wordlist into the ZIP file's GUI password prompt.

---

# Tính năng chính | Features

- Tự động nhập mật khẩu vào giao diện giải nén ZIP,...
- Sử dụng wordlist tuỳ chỉnh hoặc công khai
- Viết hoàn toàn bằng Python, không phụ thuộc công nghệ phức tạp
- Dễ dùng cho người mới học bảo mật

- Automatically types passwords into the ZIP extract GUI
- Supports custom or public password wordlists
- Pure Python, no advanced dependencies
- Beginner-friendly for cybersecurity learners

---

# Cấu trúc thư mục | Project Files

| Tệp tin / File Name                    | Mô tả / Description                       |
|----------------------------------------|-------------------------------------------|
| TriBrute.py                            | Mã nguồn chính / Main Python script       |
| award.zip                              | File ZIP có mật khẩu để kiểm thử / Test ZIP file |
| 10-million-password-list-top-10000.txt | Danh sách mật khẩu mẫu / Password wordlist |
| requirements.txt                       | Các thư viện cần cài đặt / Required packages |

---

# Cài đặt & Sử dụng | Installation & Usage

*Bước 1: Tải dự án
Step 1: Clone the project

```bash
git clone https://github.com/0xTriSec/TriBrute.git
cd TriBrute
===
*Bước 2: Cài đặt thư viện cần thiết
Step 2: Install required packages
pip install -r requirements.txt
===
*Bước 3: Chạy công cụ sau khi mở cửa sổ yêu cầu mật khẩu của file ZIP
Step 3: Open your ZIP file password dialog, then run the tool
python TriBrute.py
===
⚠️ Legal & Ethical Notes
+Use TriBrute only on files you own or have explicit permission to test.
+Brute-forcing without consent violates laws (e.g., Vietnam's Cybersecurity Law 2018).
+This tool is a proof-of-concept for learning – misuse is your responsibility.
