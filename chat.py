def read_file(filename):
    chat = []
    with open(filename, 'r', encoding='utf-8-sig') as f:
        chat = [c.strip() for c in f ]
    return chat

def convert(chat):
    new = []
    person = None #預設person為空
    for line in chat:
        if line == 'Allen':
            person = line
            continue
        elif line == 'Tom':
            person = line
            continue
        if person: #如果person有值
            new.append(person + ': ' + line)
    return new

def write_file(filename, chat):
	with open(filename, "w", encoding='utf-8') as f :
		for line in chat:
			f.write(line + '\n')

def main():
    chat = read_file('input.txt') 
    chat = convert(chat)
    print(chat)
    write_file('aa.txt', chat)
main()