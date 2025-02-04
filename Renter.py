from datetime import datetime

def main():
   true_false = input("Are you looking Individual rent info or Household Info? ")
   
   
   
   if true_false == "Individual": 
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

   elif true_false == "Household":
    household_size = int(input("Enter the number of people in your household: "))
    
    names = []
    annual_incomes = []
    
    
    for i in range(household_size):
        name = input(f"Enter the name of person {i + 1}: ")
        hourly_wage = float(input(f"Enter {name}'s pay per hour: "))
        annual_income = hourly_wage * 40 * 52
        
        names.append(name)
        annual_incomes.append(annual_income)
    
    total_annual_income = sum(annual_incomes)
    monthly_income = total_annual_income / 12
    affordable_rent = monthly_income * 0.3
    
    
    print("\nHousehold Income Details:")
    for i in range(household_size):
        print(f"{names[i]} has an annual income of ${annual_incomes[i]:.2f}.")
    
    print(f"\nTotal household annual income: ${total_annual_income:.2f}")
    print(f"The household can afford to spend around ${affordable_rent:.2f} on rent per month.");
 
   else:  
     print(" Goodbye")

if __name__ == "__main__":
    main()