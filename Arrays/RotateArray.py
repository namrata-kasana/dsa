def rotate_array_reversal(nums, k):
  """Rotates an array to the right by k steps using reversal."""
  k = k % len(nums)  # Handle k exceeding array length
  n = len(nums)
  def reverse(start, end):
    while start < end:
      nums[start], nums[end] = nums[end], nums[start]
      start += 1
      end -= 1

  # Reverse the entire array
  reverse(0, n - 1)
  # Reverse the first k-1 elements
  reverse(0,k-1)
  # Reverse the last k elements
  reverse(k,n - 1)

# Example usage
nums = [1, 2, 3, 4, 5]
k = 2
rotate_array_reversal(nums, k)
print(nums)  # Output: [4, 5, 1, 2, 3]