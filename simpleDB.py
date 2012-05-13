import fileinput
import operator

class SimpleDB:

    def __init__(self):
        self.dict = {}
        self.commit_transaction_level = 0
        self.current_transaction_level = 0

    def set(self, name, value):
        if name in self.dict:
            self.dict[name][self.current_transaction_level] = value
        else:
            self.dict[name] = {self.current_transaction_level:value}

    def unset(self, name):
	    if name in self.dict:
		    self.dict[name][self.current_transaction_level] = 'NULL'

    def get(self, name):
        if name in self.dict and len(self.dict[name]) > 0:
            print max(self.dict[name].iteritems(), key=operator.itemgetter(0))[1]
        else:
            print 'NULL'

    def rollback(self):
        if self.current_transaction_level == self.commit_transaction_level:
            print 'INVALID ROLLBACK'
            return

        self.current_transaction_level = self.current_transaction_level - 1

        for name in self.dict:
            del_list = []
            for transaction in self.dict[name]:
                if transaction > self.current_transaction_level:
                    del_list.append(transaction)

            for transaction in del_list:
                    del self.dict[name][transaction]

    def begin(self):
        self.current_transaction_level = self.current_transaction_level + 1

    def commit(self):
        self.commit_transaction_level = self.current_transaction_level
	
    def equalto(self, value):
        equal_list = []
        for name in self.dict:
            dict_val = max(self.dict[name].iteritems(), key=operator.itemgetter(0))[1]
            if value==dict_val:
                equal_list.append(name)

        if len(equal_list) == 0:
            print 'NONE'
        else:
            print " ".join(equal_list)




def main(input_cmd):
    db = SimpleDB()

    for input in input_cmd:
        input = input.rstrip('\n')
        input = input.split(' ')

        command = input[0].lower()

        if command == 'set':
            db.set(input[1], input[2])
        elif command == 'unset':
            db.unset(input[1])
        elif command == 'get':
            db.get(input[1])
        elif command == 'equalto':
            db.equalto(input[1])
        elif command == 'begin':
            db.begin()
        elif command == 'commit':
            db.commit()
        elif command == 'rollback':
            db.rollback()
        elif command == 'end':
            return

if __name__=="__main__":
    main(fileinput.input())

