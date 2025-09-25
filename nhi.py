
# 1. 
import numpy as np

# 2. 
my_numbers = list(range(0, 11))
print("Dãy số:", my_numbers)


# 3. 
print("Các số lẻ trong dãy từ 0 đến 10:", end=" ")
for i in range(0, 11):
    if i % 2 != 0:
        print(i, end=" ")
print()  # xuống dòng

# 4. 
list_comprehension = [i for i in range(0, 11) if i % 2 == 0]
print("Các số chẵn trong dãy từ 0 đến 10:", list_comprehension)

# 5. 
print("Kiểu dữ liệu số lẻ:", type(1))  
print("Kiểu dữ liệu số chẵn:", type(list_comprehension))
