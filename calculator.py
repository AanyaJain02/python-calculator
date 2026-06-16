choice = 0
while choice != 5:
  print("1. Add")
  print("2. Subtract")
  print("3. Multiply")
  print("4. Division")
  print("5. Exit")
  choice = int(input("Enter your choice: "))
  if choice == 5:
     print("Exiting program...")
  elif choice > 5 or choice < 1:
     print("Invalid")
  else:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    match choice:
          case 1:
            print("Result:", a + b)
          case 2:
            print("Result:", a - b)
          case 3:
            print("Result:", a * b)
          case 4:
            if b == 0:
               print("Error")
            else:
               print("Result:", a / b)