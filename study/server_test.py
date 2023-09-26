from socket import *
from select import *
import sys
import logging
from time import ctime

# log기록을 남기기 위한 변수
logger = logging.getLogger("ServerTest")
#log level debug(), info(), warning(), error() 그리고 critical()
logger.setLevel(logging.DEBUG)


#log file로 저장
#logging.basicConfig(filename='example.log',level=logging.DEBUG)
#log에 시간 표시
#logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
#logging.basicConfig(format='%(asctime)s %(message)s')
#logformat = logging.basicConfig(format='%(asctime)s %(message)s')
logformat = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

#log를 consol로, # create console handler and set level to debug
con = logging.StreamHandler()
con.setLevel(logging.DEBUG)
con.setFormatter(logformat)
logger.addHandler(con)

#log를 file로
fp = logging.FileHandler(filename='server_test.log', mode='w', encoding=None, delay=False)
fp.setLevel(logging.DEBUG)
fp.setFormatter(logformat)
logger.addHandler(fp)


logger.info("Start Server System")

# 소켓 객체를 만들고..
serverSocket = socket(AF_INET, SOCK_STREAM)

# 서버 정보를 바인딩
serverSocket.bind(('0.0.0.0', 3000))

# 요청을 기다림(listen)
serverSocket.listen(1)

connection_list = [serverSocket]

# 무한 루프를 시작
while connection_list:
    try:
        logger.info("요청을 기다립니다.")

        # select 로 요청을 받고, 10초마다 블럭킹을 해제하도록 함
        read_socket, write_socket, error_socket = select(connection_list, [], [], 1)

        for sock in read_socket:
            # New Connect
            if sock == serverSocket:
                clientSocket, addr_info = serverSocket.accept()
                connection_list.append(clientSocket)
                logger.info("클라이언트(%s) 연결" % addr_info[0])
            # Data Rx
            elif sock == clientSocket:
                try:
                    data = sock.recv(1024)
                    if data:
                        logger.info("데이터: %s" % data)
                        if data[0] > 2:
                            logger.warning("garbage closed")
                        else:
                            logger.info("response ok")
                            sock.send(data[0:14])
                    else:
                        logger.warning("no data closed")
                    connection_list.remove(clientSocket)
                    sock.close()
                except:
                    connection_list.remove(clientSocket)
                    sock.close()

            else:
                logger.warning("unknown socket:%s" % sock)
                connection_list.remove(sock)
                sock.close()


    except KeyboardInterrupt:
        # 부드럽게 종료하기
        serverSocket.close()
        sys.exit()        