#coding:UTF-8
import socket
import sys
import os
import commands
import threading

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

def listen(s, num):
    s.listen(num) #该参数只是限制,请求和接受这段时间内队列的大小,当请求来会添加到该队列,当accept之后,该队列会将其清除,所以限制不了客户端的个数,
                  #这个参数用于多并发
    print 'socket now listening'
    return s
def accept(s):
    (client_s, addr) = s.accept()
    print 'conected with '+addr[0] + ':' + str(addr[1]) 
    return client_s

def receive(s):
    msg = s.recv(2048)
    print('receive msg:'+msg)
    return msg

def send_msg(s, msg):
    length = len(msg)
    message = 'length:' + str(length)
    message = message + ';content:'+msg
    print('send msg is :' + message)
    s.sendall(message)

def close(s):
    s.close()

def reply(conn):
    global i
    send_msg(conn, 'connection success')
    msg = receive(conn)
    while('exit' != msg):
        status, output = commands.getstatusoutput(msg)
        send_msg(conn, output)
        msg = receive(conn)
    send_msg(conn, 'server is closed')
    close(conn)
    i=i-1
i = 0
def main():
    global i
    s = get_socket()
    bind(s, '0.0.0.0', 2541)
    listen(s, 3)
    while True:
        conn = accept(s)
        if i<=1: #限制客户端的个数
            t = threading.Thread(target=reply,args=(conn,))
            t.start()
            i = i + 1
        else:
            send_msg(conn,'')
            conn.close()
            print('connect num is full......')
            #break
    close(s) #关闭s禁止在链接

if __name__ == '__main__':
    main()