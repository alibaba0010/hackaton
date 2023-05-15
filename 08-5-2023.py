#  Python Code
import itertools
digits = [1, 8, 6, 7]

divisible_permutations = []

# Generate all permutations of the digits
for permutation in itertools.permutations(digits):
    num = int(''.join(map(str, permutation)))  # Convert permutation to an integer
    if num % 7 == 0:  # Check if number is divisible by 7
        divisible_permutations.append(num)  # Add to list of divisible permutations
    
if divisible_permutations:
    # Find smallest and largest permutation
    smallest = min(divisible_permutations)
    largest = max(divisible_permutations)
    
      # Calculate average of smallest and largest permutation
    average = (smallest + largest) / 2

    print(f"The smallest divisible permutation is {smallest}")
    print(f"The largest divisible permutation is {largest}")
    print(f"The average of the smallest and largest divisible permutations is {average}")
else:
    print("No permutation is divisible by 7")