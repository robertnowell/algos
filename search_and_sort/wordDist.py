import Queue
words = set(["damp", "lamp", "limp", "lime", "like"])
chars = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def transform(src, dest):
	current = src
	q = Queue.Queue()
	q.put((src, [src]))
	while not q.empty():
		test, arr = q.get()
		cur = list(test)
		# print(cur, arr)

		for c in chars:
			for i in range(len(cur)):
				tmp = list(cur)
				cur[i] = c
				if tmp != cur and "".join(cur) in words and cur not in arr:
					# import pdb; pdb.set_trace()
					if cur == dest:
						print("success")
						print arr + [cur]
						# return arr + [cur]
					# print("found cur in words", cur, tmp)
					q.put((cur, arr+[cur]))
				cur = list(tmp)

if __name__ == '__main__':
	transform(list("damp"), list("like"))