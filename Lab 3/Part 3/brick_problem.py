MAX_INT = 32767


def num_of_wc_runs(n, m):
	#n is the number of bricks, m is the number of settings
	brickTests = [[0 for i in range(m + 1)] for i in range(n + 1)] #bottom-up approach

	# Base cases
	for i in range(1, n + 1):
		brickTests[i][1] = 1 #"If there's only 1 setting, there is only 1 setting to test (crazy I know)
		brickTests[i][0] = 0 #We can assume with 0 settings we don't need to test

	# "Case 2" as described in lab manual
	for i in range(1, m + 1):
		brickTests[1][i] = i

	# Fill rest of the entries in table 
	for i in range(2, n + 1):
		for j in range(2, m + 1):
			brickTests[i][j] = MAX_INT
			for k in range(1, j + 1):
				placeholder = 1 + max(brickTests[i-1][k-1], brickTests[i][j-k])
				if placeholder < brickTests[i][j]:
					brickTests[i][j] = placeholder

	return brickTests[n][m]

def next_setting(n, m):
	tries = num_of_wc_runs(n, m)
	settings = []
	binary_search = m
	for _ in range(1, n-1): #we can mimic a binary search until there are 2 bricks left
		binary_search = binary_search // 2
		settings.append(binary_search)
		tries -= 1
	j = 1
	leftover_tries = num_of_wc_runs(2, binary_search)
	x = leftover_tries
	while j <= leftover_tries and x < binary_search:
		settings.append(x)
		x += (leftover_tries - j)
		j += 1
	return settings
	
def main():
    #Testing
    n = 5
    m = 100
    print("The number of trials needed in the worst case of", n, "bricks and", m, "test settings is:", (num_of_wc_runs(n, m)))
    settings = next_setting(n, m)
    print("The optimal test choices for k with", n, "bricks and", m, "test settings are:", next_setting(n,m))
	
main()

