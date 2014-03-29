cnt = input("Input number: ");
cnt = int(cnt)
array = [[0]*cnt] * cnt;

num = 1
for tmp in range(cnt):
	for tmp2 in range(cnt):
		array[tmp][tmp2] = num;
		num = num + 1

tmp=0
tmp2=0
for tmp in range(cnt):
	for tmp2 in range(cnt):
		print(array[tmp][tmp2], end=' ')

	print("")