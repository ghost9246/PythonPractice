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
			tmp2 = int(cnt/2)

			if cnt % 2 == 0:
				starCnt = 2
				for line in range(tmp2):

					for tmp in range(tmp2 - 1):
						print(" ", end='')

					for tmp in range(starCnt):
						print("*", end='')

					starCnt = starCnt + 2
					tmp2 = tmp2 - 1
					print("")

			else:
				starCnt = 1
				for line in range(tmp2 + 1):

					for tmp in range(tmp2):
						print(" ", end='')

					for tmp in range(starCnt):
						print("*", end='')

					starCnt = starCnt + 2
					tmp2 = tmp2 - 1
					print("")

		elif order == 3:
			tmp2 = int(cnt/2)

			if cnt % 2 == 0:
				starCnt = 2
				for line in range(tmp2):

					for tmp in range(tmp2 - 1):
						print(" ", end='')

					for tmp in range(starCnt):
						print("*", end='')

					starCnt = starCnt + 2
					tmp2 = tmp2 - 1
					print("")

				tmp2 = int(cnt/2)
				starCnt = cnt - 2
				for line in range(tmp2):

					for tmp in range(line + 1):
						print(" ", end='')

					for tmp in range(starCnt):
						print("*", end='')

					print("")
					starCnt = starCnt - 2

			else:
				starCnt = 1
				for line in range(tmp2 + 1):

					for tmp in range(tmp2):
						print(" ", end='')

					for tmp in range(starCnt):
						print("*", end='')

					starCnt = starCnt + 2
					tmp2 = tmp2 - 1
					print("")

				tmp2 = int(cnt/2)
				starCnt = cnt - 2
				for line in range(tmp2):

					for tmp in range(line + 1):
						print(" ", end='')

					for tmp in range(starCnt):
						print("*", end='')

					print("")
					starCnt = starCnt - 2

		elif order == 4:
			tmp2 = 1
			tmp3 = cnt-2
			for line in range(int(cnt/2)):
				for tmp in range(tmp2):
					print("*", end='')

				for tmp in range(tmp3):
					print(" ", end='')

				for tmp in range(tmp2):
					print("*", end='')

				print("");
				tmp2 = tmp2 + 1
				tmp3 = tmp3 - 2


			if cnt % 2 == 1:
				for tmp in range(cnt):
					print("*", end='')

				print("")
				tmp3 = 1

			else:
				tmp3 = 0

			tmp2 = int(cnt/2)

			for line in range(int(cnt/2)):
				for tmp in range(tmp2):
					print("*", end='')

				for tmp in range(tmp3):
					print(" ", end='')

				for tmp in range(tmp2):
					print("*", end='')

				print("");
				tmp2 = tmp2 - 1
				tmp3 = tmp3 + 2

			break

		else:
			print("Are you kidding me?");