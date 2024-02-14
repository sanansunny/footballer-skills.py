from tabulate import tabulate  # Importing the tabulate library for formatting data into a table

def calculate_salary(overall_rate):
    # List of overall rates and their corresponding salaries
    overList = [80, 60, 45, 30]
    salaries = [1000, 1000, 700, 700, 500, 500, 400]  # Salaries converted to integers
    # Checking overall rate against thresholds and returning corresponding salary
    if overall_rate >= overList[0]:
        return salaries[0]
    elif overList[1] < overall_rate < overList[0]:  # Salary range for overall rate between 60 and 80
        return salaries[1]
    elif overall_rate == overList[0]:  # This condition is redundant as it's covered by the first condition
        return salaries[2]
    elif overList[2] < overall_rate < overList[1]:  # Salary range for overall rate between 45 and 60
        return salaries[3]
    elif overall_rate == overList[2]:  # This condition was missing the corresponding salary
        return salaries[4]  # Salary for overall rate of 45
    elif overList[3] < overall_rate < overList[2]:  # Salary range for overall rate between 30 and 45
        return salaries[5]
    else:
        return salaries[6]  # Default salary if none of the above conditions match

def overall_rate(speed, shooting, passing, defending, dribbling, physicallity):
    # Calculate overall rating based on sum of skills
    skills = speed + shooting + passing + defending + dribbling + physicallity
    overall_rate = (skills * 100) / 30  # Overall rate calculation
    return overall_rate

def valid_input(prompt):
    # Function to validate user input for skill ratings
    while True:
        try:
            rating = int(input(prompt))
            if 0 <= rating <= 5:
                return rating
            else:
                print("Please enter a rating between 0 and 5.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    # Input the number of players
    noPlayers = int(input("Enter num of players"))
    finalList = [["Index", "Overall", "Salary", "ID", "Name"]]  # Initialize final list with headers
    for i in range(0, noPlayers):
        flag = True
        name = input("Enter the name")  # Input player's name
        while flag:
            Id = int(input("Enter the id"))  # Input player's ID
            if 10 <= Id <= 99:  # Validate player ID between 10 and 99
                flag = False
                break
        # Input skills for each player
        speed = valid_input("Please enter the speed skill rate of the player ")
        shooting = valid_input("Please enter the shooting skill rate of player ")
        passing = valid_input("Please enter the passing skill rate of player ")
        dribbling = valid_input("Please enter the dribbling skill rate of player ")
        physicallity = valid_input("Please enter the physicallity skill rate of player ")
        defending = valid_input("Please enter the defending skill rate of player ")
        # Calculate overall rating and salary
        overall = int(overall_rate(speed, shooting, passing, dribbling, defending, physicallity))
        print("Overall rate", overall)
        salary = calculate_salary(overall)
        print("Salary ", salary)
        # Append player information to the final list
        finalList.append([i + 1, overall, salary, Id, name])  # Incremental index starting from 1
        print("------------------>>>>>", finalList)
    # Display the final list as a formatted table
    print(tabulate(finalList, headers="firstrow", tablefmt="fancy_grid", showindex="always"))

# Call the main function to execute the program
main()
