while 1:
	order = input("input type(1~4, 0): ")
	order = int(order)

	if(order > 5 or order < 0):
		print("Are you kidding me?")

	else:
		cnt = input("Input number: ");
		cnt = int(cnt)

		if order == 1:
			for line in range(cnt):
	
				for tmp in range(cnt-line-1):
					print(" ", end='')

				for tmp in range(line+1):
					print("*", end='')

				print("")

		elif order == 2:
			tmp2 = 1
			for line in range(int(cnt/2)):
	
				for tmp in range(line):
					print(" ", end='')

				for tmp in range(tmp2):
					print("*", end='')

				tmp2 = tmp2+2
				print("")

		elif order == 3:
			print("◇")

		elif order == 4:
			print("▷◁")

		else:
			break