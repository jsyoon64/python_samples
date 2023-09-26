# -*- coding: utf8 -*-

# socket 과 select 모듈 임포트
from socket import *
from select import *
import sys
import logging
from time import ctime

# log기록을 남기기 위한 변수
logger = logging.getLogger("Leni")
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)
logger.info("Start Server System")

# 호스트, 포트와 버퍼 사이즈를 지정
HOST = ''
PORT = 36789
BUFSIZE = 1024
ADDR = (HOST, PORT)

# 소켓 객체를 만들고..
serverSocket = socket(AF_INET, SOCK_STREAM)

# 서버 정보를 바인딩
serverSocket.bind(ADDR)

# 요청을 기다림(listen)
serverSocket.listen(10)
connection_list = [serverSocket]
print('==============================================')
print('영화 서버를 시작합니다. %s 포트로 접속을 기다립니다.' % str(PORT))
print('==============================================')

# 무한 루프를 시작
while connection_list:
    try:
        logger.debug("INFO : 요청을 기다립니다.")

        # select 로 요청을 받고, 10초마다 블럭킹을 해제하도록 함
        read_socket, write_socket, error_socket = select(connection_list, [], [], 10)

        for sock in read_socket:
            # 새로운 접속
            if sock == serverSocket:
                clientSocket, addr_info = serverSocket.accept()
                connection_list.append(clientSocket)
                logger.debug("INFO : [%s] 클라이언트(%s)가 새롭게 연결 되었습니다." % (ctime(), addr_info[0]))

                # 서버소켓이 아닌 경우 방문을 환영한다는 message를 전송한다 - - - - - - - - - - - - - My Part
                if connection_list[-1] != serverSocket: 
                    connection_list[-1].send("[%s] 방문을 환영합니다. 반가워요 ^u^" %ctime()) 
                # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - My Part

                # 전체 클라이언트로 응답을 돌려줌 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - Original
                '''for socket_in_list in connection_list:
                    if socket_in_list != serverSocket and socket_in_list != sock:
                        try:
                            socket_in_list.send('[%s] 새로운 방문자가 대화방에 들어왔습니다. 반가워요~ 짝짝짝!' % ctime())
                        except Exception as e:
                            socket_in_list.close()
                            connection_list.remove(socket_in_list)'''
                # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - Original

            # 접속한 사용자(클라이언트)로부터 새로운 데이터 받음
            else:
                data = sock.recv(BUFSIZE)
                if data:
                    logger.debug("INFO : [%s] 클라이언트로부터 [%s] 전달 받았습니다." % (ctime(), data))



                    # 접속한 Client에게 서버가 메시지를 전송한다 - - - - - - - - - - - - - My Part
                    sock.send("Hi Client?")
               	  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - My Part


                    # 서버소켓이 아니며 자기자신이닌 연결 소켓들에게 메시지를 전체 전송하는 부분 - - - - - - - - - - - - - - - - - - - - - - - - - - - - Original
                    '''for socket_in_list in connection_list:
                        if socket_in_list != serverSocket and socket_in_list != sock:
                            try:
                                socket_in_list.send('[%s] %s' % (ctime(), data))
                                print('[INFO][%s] 클라이언트로 데이터를 전달합니다.' % ctime())
                            except Exception as e:
                                print(e.message)
                                socket_in_list.close()
                                connection_list.remove(socket_in_list)
                                continue'''
                    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - Original
                    	
                else:
                    connection_list.remove(sock)
                    sock.close()
                    logger.debug("INFO : [%s] 사용자와의 연결이 끊어졌습니다." % ctime())
                    
    except KeyboardInterrupt:
        # 부드럽게 종료하기
        serverSocket.close()
        sys.exit()