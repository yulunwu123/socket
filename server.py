import random
import socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 56283  # Port to listen on (non-privileged ports are > 1023)
NAME = "Server of Yulun Wu"
SERVER_NUMBER = random.randint(1, 100)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))

    while True:
        s.listen()
        conn, addr = s.accept()
        with conn:
            while True:
                data = conn.recv(1024)
                if not data:
                    break

                msg_str = data.decode("utf-8")
                msg_arr = msg_str.split(" ")
                client_number = int(msg_arr[-1])
                sum = client_number + SERVER_NUMBER
                msg_arr.pop()  # remove the last element (number)
                client_name = " ".join(msg_arr)
                print(f"The {NAME} is communicating with the {client_name}")
                print(f"Client's number: {client_number}")
                print(f"Server's number: {SERVER_NUMBER}")
                print(f"Sum: {sum}")

                data_to_client = NAME + ", " + str(SERVER_NUMBER)  # sends server name & server's chosen # to client
                conn.sendall(bytes(data_to_client, "utf-8"))

    # while True:
    #     try:
    #         clientsocket, address = s.accept()
    #     except:
    #         continue
    #     print("Connection from", address[0])
    #
    #     with clientsocket:
    #         while True:
    #             data = clientsocket.recv(1024)
    #             if not data:
    #                 break
    #             print("Is Communicating")



