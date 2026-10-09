print("Hello, create your bot's name: ")
bot_name: str = input()
print(f"""Hello, I'm your personal helper friend, my name is {bot_name}.
I am a simple else-if bot written by Anuar Kanafin.
I can do math by commands like: +; -; *; /;
To turn off the agent type: off """)

while True:
    user_input: str = input("You: ").lower()

    if user_input in ['hi', 'hello']:
        print(f"{bot_name}: Hi there! How can I help you today?")
    elif user_input in ['bye', 'goodbye']:
        print(f"{bot_name}: Goodbye my friend! Hope to see you later!")
        break
    elif user_input == "off":
        break

    elif user_input in ["+", "add","addition","plus"]:
        print(f"{bot_name}:Sure! Let's do some addition, please enter two values: ")
        try:
            num1: float = float(input("write down your first number: "))
            num2: float = float(input("write down your second number: "))
            print(f"{bot_name}: The sum is: {num1 + num2}")
        except ValueError as Error:
            print(f"{bot_name}: Try using a valid number {Error}")

    elif user_input in ["-", "substraction","minus"]:
        print(f"{bot_name}:Sure! Let's do some substraction, please enter two values: ")
        try:
            num1: float = float(input("write down your first number: "))
            num2: float = float(input("write down your second number: "))
            print(f"{bot_name}: The substraction is: {num1 - num2}")
        except ValueError as Error:
            print(f"{bot_name}: Try using a valid number {Error}")

    elif user_input in ["*", "multiplication"]:
        print(f"{bot_name}:Sure! Let's do some multiplication, please enter two values: ")
        try:
            num1: float = float(input("write down your first number: "))
            num2: float = float(input("write down your second number: "))
            print(f"{bot_name}: The multiplication is: {num1 * num2}")
        except ValueError as Error:
            print(f"{bot_name}: Try using a valid number {Error}")

    elif user_input in ["/", "division", "divide"]:
        print(f"{bot_name}:Sure! Let's do some division, please enter two values: ")
        try:
            num1: float = float(input("write down your first number: "))
            num2: float = float(input("write down your second number: "))
            print(f"{bot_name}: The division is: {num1 / num2}")
        except ValueError as Error:
            print(f"{bot_name}: Try using a valid number {Error}")
        except ZeroDivisionError as zero:
            print(f"{bot_name}: Oops, you can't divide by zero {zero}")
    else:
        print(f"{bot_name}: sorry I don't understand your request")