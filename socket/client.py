#coding:UTF-8

import socket
import sys
import time

def get_socket():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print('socket create success')
        return s
    except socket.error, msg:
        print('create socket fail, error code:'+str(msg[0])+',error message:'+msg[1])
        sys.exit()

def bind(s, ip, port):
    try:
        s.bind((ip, port))
        print('bing success, ip:'+ip+', port:'+str(port))
        return s
    except socket.error, msg:
        print('bing failed, error code:'+str(msg[0]))+', error msg:'+msg[1]
        sys.exit()

def connect(s, ip, port):
    s.connect((ip, port))
    print('socket connect success, ip:'+ip+',port:'+str(port))
    return s

def send_message(s, msg):
    try:
        s.sendall(msg)
        print('message send success')
    except socket.error:
        print('send msg fail')
        sys.exit()

def receive(s):
    i=1
    sum_length = 0
    true_length = 0
    reply_content = ''
    while True:
        reply = s.recv(2480)
        if len(reply) == 0:
            s.close()
            return -1
        if i==1:
            true_length = int(reply.split(';')[0].split(':')[1])
            reply = reply.split(';')[1][8:]
            if true_length == 0:
                s.close()
                return -1
        sum_length = sum_length + len(reply)
        reply_content = reply_content + reply
        if sum_length >= true_length:
            break
        i = i + 1
    print(reply_content)
    return 1

def close(s):
    s.close()

def main():
    count = 0
    while count < 3:
        s = get_socket()
        bind(s, '172.30.28.219', 2550)
        s = connect(s, '172.30.28.219', 2541)
        if receive(s) == 1:
            break
        time.sleep(5)
        count+=1
    if count == 3:
        print('connect fail')
        sys.exit()
    command_text = raw_input('pleae input command:')
    print('this command is '+command_text)
    while('exit' != command_text):
        if(len(command_text) != 0):
            send_message(s, command_text)
            receive(s)
        command_text = raw_input('pleae input command:')
        print('this command is '+command_text)
    send_message(s, 'exit')
    print('this is over')
    close(s)

if __name__ == '__main__':
    main()