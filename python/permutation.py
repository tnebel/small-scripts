def next_perm(nums):
  m = -1
  for i in range(len(nums)-1):
    if nums[i] < nums[i+1]:
      m = i
  if m < 0:
    return sorted(nums)
  k = 0
  for i in range(m+1, len(nums)):
    if nums[i] > nums[m]:
      k = i
  temp = nums[k]
  nums[k] = nums[m]
  nums[m] = temp
  nums[m+1:] = sorted(nums[m+1:])
  return nums

n = range(0,3)
print n
for i in range(14):
  n = next_perm(n)
  print n
