

clients = 'pablo,ricardo,'

def create_client(client_name):
    global clients

    if client_name not in clients:
        clients += client_name
        _add_comma()
    else:
        print('client already is in the client \'s list')
def list_clients():
    global clients
    print(clients)

def _add_comma():
    global clients

    clients += ','

def _print_welcome():
    print('Welcome to Jhonas ventas')
    print('*' * 50)
    print('what would you like to do today?')
    print('[C]create client')
    print('[D]create client')

# punto de entrada
if __name__ == '__main__':
    _print_welcome()

    command = input()

    if command == 'C':
        client_name = input('what is the client name')
        create_client(client_name)
        list_clients()
    elif command == 'D':
        pass
    else:
        print('el comando es invalido')
    
