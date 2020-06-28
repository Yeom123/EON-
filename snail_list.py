n = int(input("수 입력 :"))

def snail(n): 
  dal=[[0 for i in range(n)] for i in range(n)] #빈배열생성 
  i=0;j=-1;val=0;way=1        #i는행,j는열,val는숫자,way는 방향 
  while True: 
      for p in range(0,n): 
          val+=1 
          j+=way
          dal[i][j]=val 
      n=n-1                       
      if n<=0:break 
      for m in range(0,n): 
          val+=1 
          i+=way 
          dal[i][j]=val
      way*=-1 
  return dal 

snail_list = snail(n) 
for i in range(len(snail_list[0])): 
  print(snail_list[i]) 



