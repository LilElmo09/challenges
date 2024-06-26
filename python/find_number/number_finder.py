def finder(max, list):
    expected_sum = max*(max+1)//2
    real_sum = sum(list)
    return expected_sum - real_sum

list = [0,3,4,2,8,7,6,9,5]
max = max(list)
result = finder(max, list)
print(f'The missing number is: {result}')