n = int(input("작업 수 : "))

m = int(input("작업 번호 : "))

priority = list(map(int,input("작업 우선순위 : ").split()))



in_printer = list(range(len(priority))) 

time = 0



while True:

    

    if priority[0] == max(priority): 

        time = time + 1

        if in_printer[0] == m:

            print(time,'분')

            break

        else:

            priority.pop(0)

            in_printer.pop(0)

    else:

        priority.append(priority.pop(0))

        in_printer.append(in_printer.pop(0))
        







 
          




