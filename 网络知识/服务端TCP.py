import socket

if __name__ == '__main__':

    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    tcp_server_socket.bind(("",8888))
    tcp_server_socket.listen(128)
    conn_socket,ip_port=tcp_server_socket.accept()
    print(ip_port)
    recv_data=tcp_server_socket.recv(1024)
    print(recv_data)
    tcp_server_socket.send("数据收到".encode())
    conn_socket.close()
    tcp_server_socket.close()




