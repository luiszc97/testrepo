import traceback

def calculator():
    
    # Get dog age
    age = input("Input dog years: ")

    try:
        # Cast to float
        d_age = float(age)

        # If user enters negative number, print message
        # Otherwise, calculate dog's age in human years


        # your code here
        
        if d_age < 0:
            print('negative')
            return
        
        if d_age <= 1:
            h_age = d_age * 15
        elif d_age <= 2:
            h_age = d_age * 12
        elif d_age <= 3:
            h_age = float(d_age * 9.3)
        elif d_age <= 4:
            h_age = d_age * 8
        elif d_age <= 5:
            h_age = d_age * 7.2
        else:
            h_age = 36 + (d_age - 5) * 7

        # formatear salida con dos decimales forzados
        print(f"The given dog age {d_age:.1f} is {h_age:.1f} in human years.")
            
    except ValueError:
        print(age, "is an invalid age.")
        print(traceback.format_exc())
    
calculator() # This line calls the calculator function