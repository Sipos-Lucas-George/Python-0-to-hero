"""
    Calculator
"""
cmd = input("Type your equation or x to exit:\n")
with_result = "n"
result = ""
while cmd != "x":
    result = str(eval(cmd)) if with_result == "n" else str(eval(result + cmd))
    print(f"The result of the equation is: {result}")
    with_result = input("Do you want the continue with the previous answer (y/n): ")
    cmd = input("Type your equation or x to exit:\n" + result if with_result == "y" else "Type your equation or x to "
                                                                                         "exit:\n")
