from datetime import datetime
import utils

print("Md Waliul Bari")
print(datetime.now())

result_add = utils.add(5, 3)
result_subtract = utils.subtract(20, 2)
result_multiply = utils.multiply(10, 2)
result_division = utils.divide(10, 1)

print(f"Addition Result: {result_add}")
print(f"Subtraction Result: {result_subtract}")
print(f"Addition Result: {result_multiply}")
print(f"Subtraction Result: {result_division}")