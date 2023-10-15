#Task 1
# N = int(input("Enter a positive integer N: "))
# even_number = 2
# while even_number <= N:
#     print(even_number, end=" ")
#     even_number += 2  # Increment by 2 to get the next even number


#Task 2
# print()  # Print a newline to separate the output from the input prompt
# try:
#     N = int(input("Enter a positive integer N: "))
    
#     if N <= 0:
#         print("Please enter a positive integer.")
#     else:
#         even_number = 2
#         while even_number <= N:
#             print(even_number, end=" ")
#             even_number += 2  # Increment by 2 to get the next even number
#         print()  # Print a newline to separate the output from the input prompt
# except ValueError:
#     print("Invalid input. Please enter a valid positive integer.")


#Task 3
# while True:
#     try:
#         number = int(input("Enter a number: "))
#         if number == 42:
#             print("You entered the magic number 42! Exiting the program.")
#             break
#     except ValueError:
#         print("Invalid input. Please enter a valid number.")
# print("Program has terminated.")


#Task 4
# try:
#     # Ask the user to enter a string
#     user_input = input("Enter a string: ")
#     count_a = user_input.lower().count("a")
#     print(f"The number of 'a's in the string is: {count_a}")
# except Exception as e:
#     print(f"An error occurred: {e}")


#Task 5
# try:
#     num_str = input("Enter a number: ")
#     num = int(num_str)
#     digit_sum = 0
#     for digit in num_str:
#         if digit.isdigit():  # Check if the character is a digit
#             digit_sum += int(digit)

#     # Print the sum of digits
#     print(f"The sum of the digits in the number is: {digit_sum}")

# except ValueError:
#     print("Invalid input. Please enter a valid number.")


#Task 6
# try:
#     N = int(input("Enter a positive integer N:"))

#     if N <= 0:
#         print("Please enter a positive integer.")
#     else:
#         a, b = 0, 1
#         count = 0
#         while count < N:
#             print(a, end=" ")
#             a, b = b, a + b  # Calculate the next Fibonacci number
#             count += 1

# except ValueError:
#     print("Invalid input. Please enter a valid positive integer.")


#Task 7
# try:
#     user_input = input("Enter a string: ")
#     reversed_string = user_input[::-1]
#     print("Reversed string:", reversed_string)
# except Exception as e:
#     print(f"An error occurred: {e}")


#Task 8
# try:
#     total_odd_sum = 0
#     while True:
#         num_str = input("Enter a number (or 'q' to quit): ")
        
#         if num_str == 'q':
#             break 
        
#         num = int(num_str)
        
#         if num % 2 == 0:
#             continue 
        
#         total_odd_sum += num
    
#     print(f"Sum of odd numbers entered: {total_odd_sum}")

# except ValueError:
#     print("Invalid input. Please enter a valid number or 'q' to quit.")


#Task 9
# import random
# target_number = random.randint(1, 100)

# try:
#     while True:
#         user_guess = int(input("Guess the number (between 1 and 100): "))

#         if user_guess == target_number:
#             print("Congratulations! You guessed the correct number.")
#             break  # End the game when the user guesses correctly
#         elif user_guess < target_number:
#             print("Too small. Try again.")
#         else:
#             print("Too large. Try again.")

# except ValueError:
#     print("Invalid input. Please enter a valid number.")


#Task 10
# try:
#     user_input = input("Enter a string: ")
#     cleaned_input = user_input.replace(" ", "").lower()
#     if cleaned_input == cleaned_input[::-1]:
#         print("The entered string is a palindrome.")
#     else:
#         print("The entered string is not a palindrome.")
# except Exception as e:
#     print(f"An error occurred: {e}")


#Task 11
# try:
#     X = float(input("Enter the base (X): "))
#     Y = int(input("Enter the exponent (Y): "))
#     result = 1
#     count = 0
#     while count < abs(Y):
#         if Y > 0:
#             result *= X
#         else:
#             result /= X
#         count += 1
#     print(f"{X} to the power of {Y} is: {result}")
# except (ValueError, ZeroDivisionError) as e:
#     print("Invalid input. Please enter valid numbers for X and Y.")
# except Exception as e:
#     print(f"An error occurred: {e}")


#Task 12
# try:
#     N = int(input("Enter a positive integer N: "))
    
#     if N <= 1:
#         print("N should be greater than 1.")
#     else:
#         print("Prime numbers from 1 to", N, "are:")

#         number = 2

#         while number <= N:
#             is_prime = True
#             divisor = 2

#             while divisor * divisor <= number:
#                 if number % divisor == 0:
#                     is_prime = False
#                     break
#                 divisor += 1

#             if is_prime:
#                 print(number, end=" ")

#             number += 1
# except ValueError:
#     print("Invalid input. Please enter a valid positive integer.")


#Task 13
# try:
#     num_str = input("Enter a number: ")
#     num = int(num_str)
#     reversed_num = int(str(num)[::-1])
#     print("Reversed number:", reversed_num)
# except ValueError:
#     print("Invalid input. Please enter a valid number.")
# except Exception as e:
#     print(f"An error occurred: {e}")


#Task 14
# def is_prime(num):
#     if num <= 1:
#         return False
#     if num <= 3:
#         return True
#     if num % 2 == 0 or num % 3 == 0:
#         return False
#     i = 5
#     while i * i <= num:
#         if num % i == 0 or num % (i + 2) == 0:
#             return False
#         i += 6
#     return True

# def find_next_prime(start):
#     next_num = start + 1
#     while True:
#         if is_prime(next_num):
#             return next_num
#         next_num += 1

# while True:
#     try:
#         user_input = int(input("Enter a number: "))
#         if is_prime(user_input):
#             print(f"{user_input} is a prime number.")
#         else:
#             print(f"{user_input} is not a prime number.")
#             next_prime = find_next_prime(user_input)
#             print(f"The next prime number is {next_prime}")
#     except ValueError:
#         print("Invalid input. Please enter a valid number.")
#     choice = input("Do you want to check another number? (yes/no): ").lower()
#     if choice != 'yes':
#         break