

clients = 'pablo,ricardo'


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
	print('*'*50)
	


def _get_cliet_name():
	return input('What is the client name?')


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
	else:
		print('Invalid command')


