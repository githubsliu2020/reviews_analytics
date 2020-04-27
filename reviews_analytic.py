import time #導入計時模組

data= []   #建立data清單
count = 0
with open('reviews.txt','r') as f: #打開reviews.txt 並命名為f:
	for line in f: #將f:檔案裡面的每一行
		data.append(line) #加入data清單中
		count += 1 #count=count+1
		if count % 1000 == 0: #只要count 除以1000餘數是0
			print(len(data)) #列印出data清單的每一筆(會一筆一筆印)
print(len(data)) #印出data的總資料長度
#print(data[10])#印出data清單中的索引為10的資料

print ('檔案讀取完畢,總共有',len(data),'筆資料') # 

print(data[0])

#文字計數S
start_time = time.time() #把系統當時的時間記錄,使用time模組的time function
wc = {}
for d in data:    #d 是單留言 data是整筆留言清單
	words = d.split(' ')  #把每個字串用空白分開
	for word in words:    #把每一個words留言內的每個字
		if word in wc:    #如果這個字word在字典裡有出現過   
			wc[word] += 1  #查找字典中word這個字,如果有出現就加1
		else:
 			wc[word] = 1     #如果沒有出現過,就新增key進wc字典,次數為1
for word in wc:
	if wc[word] > 100000:   #如果重複的字詞出現超過100000次
		print(word, wc[word])
end_time = time.time()
print ('花了', end_time - start_time,'seconds' )

print(len(wc))
# #print(wc['Allen'])

while True:
	word = input(' 請問你想查什麼字:')
	if word == 'q':
		break
	if word in wc:
		print(word, '出現過的次數為',wc[word])
	else:
		print('這個字沒有出現過')

print('感謝使用本查詢功能')


sum_len = 0
for d in data:  #將data清單中每一筆留言d
	sum_len = sum_len + len(d) #把每一筆留言的長度都加回去上一筆 
print('留言的平均長度為',sum_len/len(data))

new =[] #建立new清單
for d in data: #將data中的每一筆留言d
	if len(d) < 100: #把每一個d留言長度大於100的
		new.append(d) #加進去new清單
print('一共有', len(new), '筆留言長長度小於100')
print(new[0]) #印出new清單中索引0的留言

good = [] #建立good清單
for d in data:
	if 'good' in d:   #如果在留言裡面有提到'good' 快寫法 good = [d for d in data if 'good' in d]
		good.append(d)
print('一共有',len(good),'筆留言提到good')
print(good[0])

