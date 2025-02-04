from datetime import datetime

def main():
  
    name = input("Enter your name: ")
    birth_year = int(input("Enter your birth year: "))
    hourly_wage = float(input("Enter your hourly wage: "))
    

    current_year = datetime.now().year
    age = current_year - birth_year
    
   
    annual_income = hourly_wage * 40 * 52
    monthly_income = hourly_wage * (40 * 4) 
    affordable_rent = monthly_income * 0.3

    print(f"\nHello {name}, you are {age} years old and your annual income is approximately ${annual_income:.2f}. ")

    print(f"\nBased on your annual income, you can afford approximately ${affordable_rent:.2f} per month in rent.")




if __name__ == "__main__":
    main()