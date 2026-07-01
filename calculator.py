def get_choice():
   choice = int(input("Enter your choice: "))
   return choice

def get_numbers():
    nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
    return nums

def add(nums):
    total = 0
    for num in nums:
        total += num
    return total

def subtract(nums):
    total = nums[0]
    for i in range(1, len(nums)):
        total -= nums[i]
    return total

def multiply(nums):
    total = 1
    for num in nums:
        total *= num
    return total

def divide(nums):
    total = nums[0]
    for i in range(1, len(nums)):
        if nums[i] == 0:
            return "Error: Cannot divide by zero."
        else:
            total /= nums[i]
    return total

operations = {
    1: ("Add", add),
    2: ("Subtract", subtract),
    3: ("Multiply", multiply),
    4: ("Divide", divide)
}

def display_menu():
    print("Welcome to Simple Calculator!")
    for choice, operation in operations.items():
        print(f"{choice}. {operation[0]}")
    print("5. Exit")

def perform_operation(nums, choice):
    return operations[choice][1](nums)

def main():
  while True:
      display_menu()

      choice = get_choice()

      if choice == 5:
          print("Exiting...")
          break

      while choice not in operations:
          print("Invalid. Try again.")
          choice = get_choice()

      nums = get_numbers()

      result = perform_operation(nums, choice)

      print(result)

if __name__ == "__main__":
    main()