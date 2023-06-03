function get_solutions(target, min_primes, max_primes, primes):
    for i from 0 to target+1
		for j from 0 to max_primes+1
			dp[i][j] = 0
	
	dp[0][0] = 1
	
	for each p in primes:
		for current_total from 0 to target-p+1:
			for coin_count from 0 to max_primes:
				dp[current_total + p][coin_count + 1] += dp[current_total][coin_count]
	
	combinations = 0
	for coin_count from min_primes to max_primes + 1
		combinations += dp[target][coin_count]
	return combinations