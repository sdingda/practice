def Josephus(n,m):
	people = list(range(1,n+1)) #给n个人编号放到表people中,从下标为0的人开始
	cur = 0
	kill=[]
	for i in range(n):  #for循环用来控制内部循环执行次数(0~n-1)
		count=0
		while count<m:
			if people[cur]!= 0:
				count += 1
			if count == m:
				kill.append(people[cur])
				people[cur] = 0  #把退出的人的编号置0
			cur = (cur+1) % n    # 下一个人重新开始从0计数。
	return kill

if __name__ == '__main__':
	josephus=Josephus(41,3)
	#死亡顺序
	print (josephus)
	#倒数第3个人
	print(josephus[-1])
	#最后三个人
	print(josephus[-3:])


def ysf(n,k,m):
	p=list(range(1,n+1))
	t=k-1
	killsort=[]

	for i in range(1,n+1):
		t=(t+m-1)%len(p)
		killsort.append(p.pop(t))

	print(killsort)
	print(killsort[-1])
	print(killsort[-3:])

ysf(41,4,3)


