import socket
import sys

try:
    number = sys.argv[1]
    while (not number.isdigit()) or int(number) < 1 or int(number) > 100:
        number = input("Please enter an integer between 1 and 100: ")
except IndexError:
    print("Please enter an integer between 1 and 100 as a command line argument")

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 8000  # Port to listen on (non-privileged ports are > 1023)
NAME = "Client of Yulun Wu"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    msg = NAME + " " + number
    s.sendall(bytes(msg, "utf-8"))
    data = s.recv(1024)

data_arr = data.decode("utf-8")
data_arr = data_arr.split(",")
server_name = data_arr[0]
server_number = int(data_arr[1])
print(f"The {NAME} sent {number} to the {server_name} and received an integer {server_number}. " \
      f"Sum of values: {server_number + int(number)}.")