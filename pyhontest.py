print("This is the first project on git ")
print ("let's go and make the first project which is simple calculator")

#make the code for calculator
#let's define the item that we need first
#result which eqaul result of summation
#/ for division
# * for multible
# - for substract
#+ for summation
# % for reminder
print ("Welcom, Can you choose your operation from the down menu:/ for dividsion ,* for mltible,+ for summation, - for substraction, % for remainder")
# 🌟 Welcome to Your First Git Project: Simple Calculator 🌟
print("==============================================")
print("       🚀 Welcome to the Simple Calculator!      ")
print("==============================================")
print("Let's create something amazing together. 🎉")
print()

# 🛠️ Display the available operations
print("💡 Available Operations:")
print("   ➕  Addition (+)")
print("   ➖  Subtraction (-)")
print("   ✖️  Multiplication (*)")
print("   ➗  Division (/)")
print("   🟰  Remainder (%)")
print()
print("👉 Please choose an operation from the menu above.")
operation = input("Your choice (e.g., +, -, *, /, %): ")

# 🚪 Prompt the user to enter two numbers
print("\nGreat choice! Now, let's calculate:")
num1 = float(input("🔢 Enter the first number: "))
num2 = float(input("🔢 Enter the second number: "))

# 🎯 Perform the calculation
print("\n🔄 Calculating...")
if operation == "+":
    result = num1 + num2
    print(f"✅ The result of {num1} + {num2} is: {result}")
elif operation == "-":
    result = num1 - num2
    print(f"✅ The result of {num1} - {num2} is: {result}")
elif operation == "*":
    result = num1 * num2
    print(f"✅ The result of {num1} × {num2} is: {result}")
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"✅ The result of {num1} ÷ {num2} is: {result}")
    else:
        print("❌ Error: Division by zero is not allowed.")
elif operation == "%":
    if num2 != 0:
        result = num1 % num2
        print(f"✅ The remainder when {num1} is divided by {num2} is: {result}")
    else:
        print("❌ Error: Modulus by zero is not allowed.")
else:
    print("❌ Invalid operation. Please choose a valid operation from the menu.")

# 👋 Thank the user
print("\n==============================================")
print("       🙌 Thank you for using the calculator!       ")
print("==============================================")
