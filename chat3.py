#讀取資料 但字串的部分分割邏輯不同的處理
lines = []
with open('3.txt', 'r', encoding='utf-8-sig') as f :
	for line in f :
		lines.append(line.strip())
allen_word = 0
viki_word = 0
for line in lines :
	s = line.split(' ')
	time = s[0][:5]
	name = s[0][5:]
	