for item in 'Python':
    print(item)
for item in range(10):
    print(item)
for item in range(5,10):
    print(item)
for item in range(5,10,2):
    print(item)
prices=[10,20,30]
for item in range(len(prices)):
    print(prices[item])
total=0
for item in range(len(prices)):
    total+=prices[item]
print(f"Total:{total}")