import os
import pymysql
from urllib.request import urlopen

# SECURITY ISSUE: Database credentials are hardcoded. Consider using environment variables or a secure secrets manager.
db_config = {
    'host': 'mydatabase.com',
    'user': 'admin',
    'password': 'secret123'
}

def get_user_input():
    # SECURITY ISSUE: User input is not validated or sanitized.
    user_input = input('Enter your name: ')
    return user_input

def send_email(to, subject, body):
    # SECURITY ISSUE: os.system is vulnerable to command injection. Use the subprocess module with proper escaping.
    os.system(f'echo {body} | mail -s "{subject}" {to}')

def get_data():
    # SECURITY ISSUE: HTTP is insecure. Use HTTPS to avoid MITM (Man-in-the-Middle) attacks.
    url = 'http://insecure-api.com/get-data'
    data = urlopen(url).read().decode()
    return data

def save_to_db(data):
    # SECURITY ISSUE: SQL Injection vulnerability. Never insert data directly into SQL queries. Use parameterized queries instead.
    query = f"INSERT INTO mytable (column1, column2) VALUES ('{data}', 'Another Value')"
    connection = pymysql.connect(**db_config)
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    cursor.close()
    connection.close()

if __name__ == '__main__':
    user_input = get_user_input()
    data = get_data()
    save_to_db(data)
    send_email('admin@example.com', 'User Input', user_input)