import sys


clients = [
	{
		'name':'Bev',
		'company': 'Google',
		'email': 'bev@google.com',
		'position': 'Software Engineer'
	},
	{
		'name':'Bill',
		'company': 'Google',
		'email': 'bill@google.com',
		'position': 'Data Engineer'
	}
]


def create_client(client):
	global clients
	if client not in clients:
		clients.append(client)
	else:
		print('Client already is in the client\'s list')
	

def delete_client(client_name):
	global clients
	if client_name in clients:
		clients.remove(client_name)
	else:
		print('Client is not in clients list')


def search_client(client_name):
	global clients
	for client in clients:
		if client != client_name:
			continue
		else:
			return True


def _add_comma():
	global clients
	clients += ','


def list_clients():
	global clients
	for i,client in enumerate(clients):
		print('{}: {}'.format(i,client['name']))


def update_client(client_name, updated_client_name):
	global clients
	if client_name in clients:
		index = clients.index(client_name)
		clients[index] = updated_client_name
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
	

def _get_cliet_field(field_name):
	field = None
	while not field:
		field = input('What is the client {}?'.format(field_name))
	return field


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
		client = {
			'name': _get_cliet_field('name'),
			'company': _get_cliet_field('company'),
			'email': _get_cliet_field('email'),
			'position': _get_cliet_field('position')
		}
		create_client(client)
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


