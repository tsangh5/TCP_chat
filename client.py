import socket
import threading

nickname = input('Choose your nickname: ')
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('119.246.244.88', 3000))

def recieve():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'SEND NICKNAME':
                client.send(nickname.encode('ascii'))
            else:
                print(message)  
        except:
            print('ERROR')
            client.close()
            break

def write():
    while True:
        message = f"{nickname}: {input('')}"
        client.send(message.encode('ascii'))

recieve_thread = threading.Thread(target=recieve)
recieve_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()