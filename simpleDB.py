import fileinput
import operator


commit_transaction_level = 0
current_transaction_level = 0


dict = {}

def set(name, value):
	if name in dict:
		dict[name][current_transaction_level] = value
	else:
		dict[name] = {current_transaction_level:value}

def unset(name):
	if name in dict:
		dict[name][current_transaction_level] = 'NULL'

def get(name):

	if name in dict and len(dict[name]) > 0:
		print max(dict[name].iteritems(), key=operator.itemgetter(0))[1]
	else:
		print 'NULL'

def rollback():
	global current_transaction_level
	if current_transaction_level == commit_transaction_level:
		print 'INVALID ROLLBACK'
		return

	current_transaction_level = current_transaction_level - 1
	for name in dict:
		del_list = []
		for transaction in dict[name]:
			if transaction > current_transaction_level:
				del_list.append(transaction)

		for transaction in del_list:
			del dict[name][transaction]

def commit():
	global commit_transaction_level
	commit_transaction_level = current_transaction_level
	
def equalto(value):
	equal_list = []
	for name in dict:
		dict_val = max(dict[name].iteritems(), key=operator.itemgetter(0))[1]
		if value==dict_val:
			equal_list.append(name)

	if len(equal_list) == 0:
		print 'NONE'
	else:
		print " ".join(equal_list)


def main(input_cmd):
	global current_transaction_level

	for input in input_cmd:
		input = input.rstrip('\n')
		input = input.split(' ')

		command = input[0].lower()

		if command == 'set':
			set(input[1], input[2])
		elif command == 'unset':
			unset(input[1])
		elif command == 'get':
			get(input[1])
		elif command == 'equalto':
			equalto(input[1])
		elif command == 'begin':
			current_transaction_level = current_transaction_level + 1
		elif command == 'commit':
			commit()
		elif command == 'rollback':
			rollback()
		elif command == 'end':
			return
	

if __name__=="__main__":
	main(fileinput.input())	

