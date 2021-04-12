import random
start = int(input('請輸入開始值: '))
end = int(input('請輸入結束值: '))
r = random.randint(start, end)
count = 0
while True:
	n = int(input('請輸入數字: '))
	if n > r:
		print('比答案大')
		count +=1
	elif n < r:
		print('比答案小')
		count +=1
	else:
		print('答對了')
		break
print('總共猜了', count, '次')