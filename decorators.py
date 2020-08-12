PASSWORD = '12345'


def password_required(func):
	def wrapper():
		password = input('What is your password?')
		if password == PASSWORD:
			return func()
		else:
			print('Password incorrect')
	return wrapper


@password_required
def needs_password():
	print ('The password is correct')


def upper(func):
	def wrapper(*args, **kwargs):
		result = func(*args, **kwargs)
		return result.upper()
	print("1")
	return wrapper

@upper
def say_my_name(name):
	return 'Hi, {}'.format(name)


if __name__ == '__main__':
	print(say_my_name('David'))