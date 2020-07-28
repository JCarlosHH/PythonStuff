import random


def generate_pass():
	capital_letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
	lowercase_letters = ['a','q','w','e','r','t','y','b','c','z','p']
	numbers = ['1','2','3','4','5','6','7','8','9','0']
	symbols = ['!',"?",'%','#']
        
	characters = capital_letters + lowercase_letters + numbers + symbols
	password = []
	for i in range(10):
		character_random = random.choice(characters)
		password.append(character_random)
	password = ''.join(password)
	return password

def run():
	password = generate_pass()
	print ("Your new password is: " + password )


if __name__ == '__main__':
	run()
