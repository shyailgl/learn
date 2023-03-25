# 编写服务端程序
import socket

if __name__ == '__main__':
    #     创建socket
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    tcp_server_socket.bind(("", 8080))
    tcp_server_socket.listen(128)
    #     获取浏览器http数据
    while True:
        client_socket, client_addr = tcp_server_socket.accept()
        client_request_data = client_socket.recv(1024).decode()
        print(client_request_data)
        request_dara=client_request_data.split(" ")
        print(request_dara)
        request_path=request_dara[1]
        with open("./static/"+request_path, 'rb') as f:
            file_data = f.read()
        response_line = "HTTP/1.1 200 OK\r\n"
        response_head = "Server:pwb\r\n"
        response_body = file_data
        response_data = (response_line + response_head + "\r\n").encode() + response_body
        client_socket.send(response_data)
        client_socket.close()
