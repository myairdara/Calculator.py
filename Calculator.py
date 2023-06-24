def calculator()
    while True
        
        operation = input(Enter an operation (+, -, , ) or 'q' to quit )

        
        if operation == 'q'
            print(Exiting calculator...)
            break

        
        num1 = float(input(Enter the first number ))

        
        num2 = float(input(Enter the second number ))

        
        if operation == '+'
            print(fResult {num1 + num2})
        elif operation == '-'
            print(fResult {num1 - num2})
        elif operation == ''
            print(fResult {num1  num2})
        elif operation == ''
            if num2 != 0
                print(fResult {num1  num2})
            else
                print(Error Division by zero!)
        else
            print(Invalid operation!)



calculator()
