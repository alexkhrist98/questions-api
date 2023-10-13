"""В этом модуле находится точка входа в приложение"""

from infrastructure.server import Server

def main() -> None:
    server = Server() 
    server.run() 

if __name__ == "__main__":
    main() 
