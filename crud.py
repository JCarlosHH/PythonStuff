import sys


clients = 'Bill,Bev,Ben,Mike,Stan,Richie,Eddie,'


def create_client(client_name):
	global clients
	#clients += client_name
	if client_name not in clients:
		clients += client_name
	else:
		print('Client already is in the client\'s list')
	_add_comma()


def delete_client(client_name):
	global clients
	if client_name in clients:
		clients = clients.replace(client_name,'')
	else:
		print('Client is not in clients list')


def search_client(client_name):
	global clients
	clients = clients.lower()
	clients_list = clients.split(',')
	client_name.lower()
	for client in clients_list:
		if client != client_name:
			continue
		else:
			return True


def _add_comma():
	global clients
	clients += ','


def list_clients():
	global clients
	print(clients)


def update_client(client_name, updated_client_name):
	global clients
	if client_name in clients:
		clients = clients.replace(client_name + ',', updated_client_name + ',')
	else:
		print('Client is not in clients list')


def _print_welcome():
	print('Welcome to Platzi Ventas')
	print('*'*50)
	print('What would you like to do today?')
	print('[C]reate client')
	print('[U]pdate client')
	print('[D]elete client')
	print('[S]earch client')
	print('*'*50)
	

def _get_cliet_name():
	client_name = None
	while not client_name:
		client_name = input('What is the client name?')
		if client_name == 'exit':
			client_name = None
			break
	if not client_name:
		sys.exit()
	return client_name


if __name__ == '__main__':
	_print_welcome()

	command = input()
	command = command.upper()

	if command == 'C':
		client_name = _get_cliet_name()
		create_client(client_name)
		list_clients()
	elif command == 'D':
		list_clients()
		client_name = _get_cliet_name()
		delete_client(client_name)
		list_clients()
	elif command == 'U':
		list_clients()
		client_name = _get_cliet_name()
		updated_client_name = input('What is the updated client name?')
		update_client(client_name, updated_client_name)
		list_clients()
	elif command == 'S':
		client_name = _get_cliet_name()
		found = search_client(client_name)
		if found:
			print('The client is in the client\'s list')
		else:
			print('The client: {} is not in our client\'s list'.format(client_name))
	else:
		print('Invalid command')


