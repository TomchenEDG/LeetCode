quicksort(test,left=0, right=9)

def quicksort(test, left=0, right=9)
	if left < right: | if 0 < 9:
	p = partiion(v, left, right)| p = parttion(test, 0, 9)
	key = v[left] | key = 21
	low = left    | low = 0
	high = right  | high = 9
	while low < high: | while 0 < 9: True
		while (low < high) and (v[high] >= key):| while (0 < 9) and (14 >= 21): Flase
			high -= 1 | high = high - 1 = 8
		v[low] = v[high]  | 14赋值给21：          [14, 4, 1, 3, 9, 20, 25, 6, 21, 14]
		while (low < high) and (v[low] <= key): | while (0 < 9) and (14 <= 21): True
			low += 1 | low = 0 + 1 = 1
		v[high] = v[low] | 25的位置赋值给14     ：[14, 4, 1, 3, 9, 20, 25, 6, 21, 25]
		v[low] = key  | 25的位置赋值21 ：	  [14, 4, 1, 3, 9, 20, 21, 6, 21, 25]
	return low

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]

print quicksort(test, left = 0, right = len(test) - 1)