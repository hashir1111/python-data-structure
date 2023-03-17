def bubble_sort(nums):
    for i in range(len(nums)-1,0,-1):
        for j in range(i):
            if nums[j]>nums[j+1]:
                a=nums[j]
                nums[j]=nums[j+1]
                nums[j+1]=a





nums=[]
start=int(input("enter starting range of the list:"))
end=int(input("enter the ending range of list:"))
for k in range(start,end+1):
    value=int(input("enter the values you want to append:"))
    nums.append(value)
print(nums)
print("VALUES ARE SORTED")
bubble_sort(nums)
print(nums)
