def server(HOST: str):
    import socket
    import sys
    import cv2
    import pickle
    import numpy as np
    import struct 
    import zlib

    HOST=HOST
    PORT=8485

    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print('Socket created')

    s.bind((HOST,PORT))
    print('Socket bind complete')
    s.listen(10)
    print('Socket now listening')

    conn,addr=s.accept()

    data = b""
    payload_size = struct.calcsize(">L")
    while True:
        while len(data) < payload_size:
            data += conn.recv(4096)
        packed_msg_size = data[:payload_size]
        data = data[payload_size:]
        msg_size = struct.unpack(">L", packed_msg_size)[0]
        while len(data) < msg_size:
            data += conn.recv(4096)
        frame_data = data[:msg_size]
        data = data[msg_size:]

        frame=pickle.loads(frame_data, fix_imports=True, encoding="bytes")
        frame = cv2.imdecode(frame, cv2.IMREAD_COLOR)
        cv2.imshow('ImageWindow',frame)
        cv2.waitKey(1)

def client(HOST: str,formula: str):
    import cv2
    import io
    import socket
    import struct
    import time
    import pickle
    import zlib
    from cryptogen import encrypt,decrypt

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, 8485))
    connection = client_socket.makefile('wb')

    cam = cv2.VideoCapture(0)

    cam.set(3, 320);
    cam.set(4, 240);

    img_counter = 0

    encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]

    while True:
        ret, frame = cam.read()
        if formula=='gotham':
            frame=encrypt.gotham(frame,'F')

        elif formula=='krypton':
            frame=encrypt.krypton(frame,'F')

        elif formula=='atlantis':
            frame=encrypt.atlantis(frame,'F')

        elif formula=='oa':
            frame=encrypt.oa(frame,'F')

        elif formula=='starling':
            frame=encrypt.starling(frame,'F')

        else:
            pass

        result, frame = cv2.imencode('.jpg', frame, encode_param)
        data = pickle.dumps(frame, 0)
        size = len(data)
        client_socket.sendall(struct.pack(">L", size) + data)
        img_counter += 1
        cv2.waitKey()
        cv2.destroyAllWindows()
    cam.release()