def twoSum(nums, target):
  """
  Finds the indices of two numbers in an array that add up to a target.

  Args:
      nums: A list of integers.
      target: The target sum.

  Returns:
      A list containing the indices of the two numbers, or an empty list if not found.
  """
  # Create a dictionary to store seen elements and their indices.
  seen = {}
  for i, num in enumerate(nums):
    # Check if the complement (target - num) exists in the dictionary.
    complement = target - num
    if complement in seen:
      # Found a pair! Return the indices.
      return [seen[complement], i]
    # If not found, add the current number and its index to the dictionary.
    seen[num] = i
  # No match found, return an empty list.
  return []

# Example usage
nums = [2, 7, 11, 15]
target = 9
indices = twoSum(nums, target)
print(indices)  # Output: [0, 1] (or [1, 0] as any order is valid)