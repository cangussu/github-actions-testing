import random

def generate_and_shuffle_random_numbers(count, min_val, max_val):
    """
    Generates a list of random integers within a specified range and then shuffles it.

    Args:
        count (int): The number of random integers to generate.
        min_val (int): The minimum value for the random integers (inclusive).
        max_val (int): The maximum value for the random integers (inclusive).

    Returns:
        list: A shuffled list of random integers.
    """
    if count <= 0:
        return []
    if min_val > max_val:
        raise ValueError("min_val cannot be greater than max_val")

    random_numbers = [random.randint(min_val, max_val) for _ in range(count)]
    random.shuffle(random_numbers)
    return random_numbers

# Example usage
num_elements = 10
lower_bound = 1
upper_bound = 100

shuffled_list = generate_and_shuffle_random_numbers(num_elements, lower_bound, upper_bound)
print(f"Generated and shuffled list of {num_elements} random numbers between {lower_bound} and {upper_bound}:")
print(shuffled_list)
