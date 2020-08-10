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
	

def _get_client_delete(client_name):
	global clients
	#client = input('Which client do you want to delete?')
	id = search_client(client_name)
	if id != None:
		del clients[id]
	else:
		print('The client is not our client\'s list')


def search_client(client_name):
	global clients
	for id,client in enumerate(clients):
		if client['name'] != client_name:
			continue
		else:
			return id


def list_clients():
	global clients
	for i,client in enumerate(clients):
		print('{uid} | {name} | {company} | {email} | {position}'.format(uid=i,name=client['name'],company=client['company'],email=client['email'],position=client['position'] ))


def update_client(client_name):
	global clients
	id = search_client(client_name)
	if id != None:
		updated_client = _get_new_client()
		clients[id].update(updated_client)
	else:
		print('Client is not in clients list')


def _get_new_client():
	client = {
		'name': _get_client_field('name'),
		'company': _get_client_field('company'),
		'email':  _get_client_field('email'),
		'position': _get_client_field('position')
	} 
	return client


def _print_welcome():
	print('Welcome to Platzi Ventas')
	print('*'*50)
	print('What would you like to do today?')
	print('[C]reate client')
	print('[U]pdate client')
	print('[D]elete client')
	print('[S]earch client')
	print('*'*50)
	

def _get_client_field(field_name):
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
			'name': _get_client_field('name'),
			'company': _get_client_field('company'),
			'email': _get_client_field('email'),
			'position': _get_client_field('position')
		}
		create_client(client)
		list_clients()
	elif command == 'D':
		list_clients()
		client_name = _get_client_field('name')
		_get_client_delete(client_name)
		list_clients()
	elif command == 'U':
		list_clients()
		updated_client_name = _get_cliet_name()
		update_client(updated_client_name)
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


