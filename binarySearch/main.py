lst = [1,6,5,4,3,2,9,8,7,10]
lst.sort()
first = 0
last = len(lst)-1
mid = (first + last)//2
item = int(input("Enter the number to be searched:"))
found = False
while(first<=last and not found):
    mid = (first + last)//2
    if lst[mid] == item:
        print(f"Item found at location {mid+1}")
        found = True
    else:
        if item < lst[mid]:
            last = mid - 1
        else:
            first = mid + 1

if found == False:
    print("Number not found")

