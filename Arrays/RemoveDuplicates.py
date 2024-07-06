def remove_duplicates(nums):
  """
  Removes duplicates from a sorted array in-place and returns the new length.

  Args:
      nums: A list of sorted integers.

  Returns:
      The new length of the array without duplicates.
  """
  if not nums:
    return 0

  i = 1  # pointer to the next unique element
  for j in range(1, len(nums)):
    if nums[j] != nums[i-1]:
       nums[i] = nums[j]
       i += 1
  return i

# Example usage
nums = [9, 8, 8,7,7]
new_length = remove_duplicates(nums)
print(f"Array after removing duplicates: {nums[:new_length]}")