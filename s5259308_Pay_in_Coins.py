from timeit import default_timer as timer
import sys


# SieveOfEratosthenes function that creates a list of all primes less than the upper parameter
def sieve_of_eratosthenes(n):
    is_prime = [True for _ in range(n + 1)]  # Initialize an array to mark numbers
    primes_list = [1]  # create a list to store prime numbers starting with 1
    p = 2
    while p * p <= n:
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False  # mark all i values that aren’t prime to False
        p += 1
    for p in range(2, n + 1):  # add all numbers that are prime to primes_list
        if is_prime[p]:
            primes_list.append(p)
    return primes_list


# function that finds all possible combinations of primes that sum to amount.
# uses an iterative, dynamic programming approach
def get_solutions(target, min_primes, max_primes, primes):
    dp_solutions = [[0] * (max_primes + 1) for _ in range(target + 1)]  # 2D array to store solutions
    dp_solutions[0][0] = 1  # set the base case, dp[0][0] to 1 where the sum is 0 and the number of primes used is 0

    for p in primes:  # iterate through each prime in primes
        for current_total in range(target - p + 1):  # iterate through target (amount - current prime + 1)
            for coin_count in range(max_primes):
                # add prime to dp using the previous calculation made without the prime added.
                dp_solutions[current_total + p][coin_count + 1] += dp_solutions[current_total][coin_count]

    combinations = 0
    for coin_count in range(min_primes, max_primes + 1):  # iterate through solutions that use min->max amount of coins
        combinations += dp_solutions[target][coin_count]  # add to combination counter
    return combinations


if __name__ == '__main__':
    input_file = open(str(sys.argv[1]))  # open specified input file given from command line argument
    output_file = open("output.txt", "w")  # open file for output
    for line in input_file:  # iterate through lines in input_file
        user_parameters = line.split()
        amount = int(user_parameters[0])
        min_coins = int(user_parameters[1]) if len(user_parameters) > 1 else 0
        max_coins = int(user_parameters[2]) if len(user_parameters) > 2 else min_coins if len(user_parameters) > 1 else amount
        prime_numbers = sieve_of_eratosthenes(amount)  # create list of primes

        start = timer()  # start timer
        combinations = get_solutions(amount, min_coins, max_coins, prime_numbers)  # calculate all possible combinations
        end = timer()  # stop timer

        print("\nInput: ", amount, min_coins, max_coins)
        print("Total number of valid combinations: ", combinations)
        print(f"{end - start:.6f} seconds")
        output_file.write(str(combinations) + "\n")
    input_file.close()
    output_file.close()

