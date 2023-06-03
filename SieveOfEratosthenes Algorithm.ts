function sieve_of_eratosthenes(n)
	for i from 0 to n+1:
		is_prime[i] = True
	primes_list = [1]
	p = 2
	while p * p <= n:
		if is_prime[p] is True:
			while j < n+1:
				is_prime[j] = False
				j = j + p
			p = p + 1
		for p from 2 to n+1:
			if is_prime[p] is True:
				add p to primes_list
	return primes_list