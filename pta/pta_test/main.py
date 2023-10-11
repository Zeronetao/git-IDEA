import socket
# 服务器对象
server = socket.socket()
'''
等同于：server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.AF_INET：使用IPV4；
socket.SOCK_STREAM：创建一个socket套接字。
'''

# 1.绑定服务器
server.bind(("0.0.0.0",8800))   #0.0.0.0是允许所有人来访问；8800是端口号

# 2.监听
server.listen(5)

while True:
    # 3.等待连接
    # accept是一个阻塞的方法（你不来我就不动！），等待连接，每建立一个连接就会创建一个单独的通道。
    # conn:通道参数；addr：通道地址。
    conn,addr=server.accept()

    # 4.接收数据
    data=conn.recv(1024)
    print(data)

    response="HTTP/1.1 200 OK\r\nContent-Type: text/html;charset=utf-8;\r\n\r\n<h1 style='color:black'>我很帅！<h1>"

    # 5.发送数据
    conn.send(response.encode())
    print("已经响应")

# 6.关闭
server.close()
