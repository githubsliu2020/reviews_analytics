data= []   #建議data清單
count = 0
with open('reviews.txt','r') as f: #打開reviews.txt 並命名為f:
	for line in f: #將f:檔案裡面的每一行
		data.append(line) #加入data清單中
		count += 1 #count=count+1
		if count % 1000 == 0 : #只要count 除以1000餘數是0
				print(len(data)) #列印出data清單的每一筆(會一筆一筆印)
print(len(data)) #印出data的總資料長度

print (data[0]) #印出data清單中的索引為0的資料