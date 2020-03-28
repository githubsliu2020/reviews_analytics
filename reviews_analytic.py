data= []   #建議data清單
count = 0
with open('reviews.txt','r') as f: #打開reviews.txt 並命名為f:
	for line in f: #將f:檔案裡面的每一行
		data.append(line) #加入data清單中
		count += 1 #count=count+1
		if count % 10000 == 0 : #只要count 除以10000餘數是0
				print(len(data)) #列印出data清單的每一筆(會一筆一筆印)
print(len(data)) #印出data的總資料長度
print(data[10])#印出data清單中的索引為10的資料

print ('檔案讀取完畢,總共有',len(data),'筆資料') # 

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

