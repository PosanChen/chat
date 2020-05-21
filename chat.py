def read_file(filename):
	lines = []
	with open(filename, 'r', encoding = 'utf-8-sig') as f:
			# utf-8-sig 這個編碼可以把\ufeff去掉
		for line in f:
			lines.append(line.strip()) #.strip() 把換行\n去掉
	return lines

def convert(lines): #把讀出來的清單lines傳入convert function
	new = []
	person = None #先宣告person的值是無None，否則如果下面的if判斷都沒有遇到，那person就會還沒定義，會當掉

	for line in lines:
		if line == 'Allen':
			person = 'Allen'
			continue
		elif line == 'Tom':
			person = 'Tom'
			continue
		if person: #意思就是，如果person有值，才會進入下一行加入清單動作
			new.append(person + ': ' + line)
		
	return new

def write_file(filename, lines):
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n')

def main():
	lines = read_file('input.txt')
	lines = convert(lines) #打開convert function
	write_file('output.txt', lines)
main() #程式進入點