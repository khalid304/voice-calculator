

import pyttsx3

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 120)
engine.setProperty('volume', 1.0)

while True:
    try:
        a = float(input("Enter first number: "))
        op = input("Enter operator (+, -, *, /): ")
        b = float(input("Enter second number: "))

        if op == "+":
            result = a + b
        elif op == "-":
            result = a - b
        elif op == "*":
            result = a * b
        elif op == "/":
            if b != 0:
                result = a / b
            else:
                result = "Error: Division by zero"
        else:
            result = "Invalid operator"

        print(f"Result: {result}")
        engine.say(f"The result is {result}")
        engine.runAndWait()

    except ValueError:
        print("Invalid input, please enter numbers.")
        engine.say("Invalid input, please enter numbers.")
        engine.runAndWait()

    except KeyboardInterrupt:
        print("\nGoodbye!")
        engine.say("Goodbye!")
        engine.runAndWait()
        break
    except ZeroDivisionError:
        print("you cant div by zero !")
        engine.say('you cant div by zero')
        engine.runAndWait()
    except Exception as e:
        print(f"An error occurred: {e}")
        engine.say(f"An error occurred: {e}")
        engine.runAndWait()


    again = input("Do you want to calculate again? (yes/no): ").lower()
    if again != "yes":
        print("Exiting calculator. Thank you!")
        engine.say("Exiting calculator. Thank you!")
        engine.runAndWait()
        break