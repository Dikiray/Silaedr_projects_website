from tqdm import tqdm

def task(x):
	m = 0
	n = 0
	for i in range(2, x-1):
		if x % i == 0:
			if m == 0:
				m = i
			elif n == 0:
				n = i
				break
	return m, n

for j in tqdm(range(174457, 174505)):
	m, n = task(j)
	if m*n == j:
		print("{} {}".format(m, n))