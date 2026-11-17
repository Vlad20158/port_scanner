import socket
def scan_port(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    try:
        result = s.connect_ex((ip,port))
        if result == 0:
            print(f"Порт {port} - открыт")
        else:
            print(f"Порт {port} - закрыт")

    except socket.error as e:
        pass

    finally:
        s.close()

if __name__ == "__main__":
    ip = input("Введите IP или домен:")
    try:
        target_ip = socket.gethostbyname(ip)
    except socket.gaierror:
        print("Ошибка,неверный IP или домен")
        exit()

    start_port = int(input("Введите начальный порт для сканирования:"))
    end_port = int(input("Введите конечный порт для сканирования:"))
    print("Vlanter|---Начинаю сканирование---|Vlanter")

    for port in range(start_port, end_port + 1):
        scan_port(target_ip,port)