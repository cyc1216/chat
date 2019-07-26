#讀取對話紀錄後 計算每個說了幾個字 發了幾個貼圖 發了幾張圖片
def read_file(filename):
    chat = []
    with open(filename, 'r', encoding='utf-8-sig') as f:
        chat = [c.strip() for c in f ]
    return chat

def convert(chat):#計算每個人的對話字數, 貼圖數,圖片數
    person = None #預設person為空
    allen_word_count = 0
    allen_sticker_count = 0
    allen_photo_count = 0
    viki_word_count = 0
    viki_sticker_count = 0
    viki_photo_count = 0
    for line in chat:
        s= line.split(' ')
        time = s[0]
        name = s[1]
        if name == 'Allen':
            if s[2] == '貼圖':
                allen_sticker_count += 1
            elif s[2] == '圖片':
                allen_photo_count +=1 
            else:
                for m in (s[2:]):
                    allen_word_count += len(m)
        elif name == 'Viki':
            if s[2] == '貼圖':
                viki_sticker_count += 1
            elif s[2] == '圖片':
                viki_photo_count +=1 
            else:
                for m in (s[2:]):
                 viki_word_count += len(m)
    print('allen said', allen_word_count, 'words',',sent', allen_sticker_count, 'stickers and sent', allen_photo_count, 'photo')
    print('viki said', viki_word_count, 'words',',sent', viki_sticker_count, 'stickers and sent', viki_photo_count, 'photo')
def write_file(filename, chat):
    with open(filename, "w", encoding='utf-8') as f :
        for line in chat:
            f.write(line + '\n')

def main():
    chat = read_file('[LINE]Viki.txt') 
    chat = convert(chat)
    #write_file('aa.txt', chat)
main()