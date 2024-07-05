def containsDuplicate(nums):
  """
  Checks if an array contains duplicate elements using a dictionary.

  Args:
      nums: A list of integers.

  Returns:
      True if there are duplicates, False otherwise.
  """
  # Create an empty dictionary to store seen elements.
  seen = {}
  for num in nums:
    # Check if the current number is already in the dictionary.
    if num in seen:
      return True
    # If not seen before, add it to the dictionary.
    seen[num] = True
  return False

print(containsDuplicate([1,1,2]))