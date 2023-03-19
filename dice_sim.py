import random
import tkinter


def dice_choice():
    """Prompts user to select dice to be rolled."""
    options = {1: "1 dice", 2: "2 dice", 3: "30sec"}

    choice = ''
    while choice not in options.keys():
        message = "\nSelect Number Specifying Dice to be Rolled.\n"
        message += "1 - 1 dice.\n2 - 2 Dice.\n3 - 30 SECONDS Dice.\n"
        message += "choice: "

        choice = input(message).strip()
        
        if choice.isdigit() and int(choice) in options.keys():
            choice = int(choice)
            print("\nDice to be Rolled - " + options[choice])
            
            confirm_msg = "Enter ANY Key to Confirm Choice"
            confirm_msg += " / N to Choose Again: "
            confirm = input(confirm_msg).strip().upper()

            if confirm == 'N': choice = ''
        
    return options[choice]


def one_dice():
    """
    Simulates rolling of singular dice.
    returns rolls in range 1-6.
    """
    return random.randint(1, 6)


def secs_dice():
    """
    Simulates rolling of 30 SECONDS dice.
    returns roll in range 0-2."""
    return random.randint(0, 2)


def window_setup():
    """Sets up Tkinter window which shall display dice rolls.
    And sets up Label widget that will display rolled number/dots."""
    global window, label

    # Setting Up and Displaying window.
    window = tkinter.Tk()
    window.geometry("600x400")
    window.title("Dice Simulator")
    window.configure(bg="black")

    # Setting up label
    label = tkinter.Label(window, font=("times", 250), bg="black", 
        fg="yellow")


def button_setup(choice):
    """Sets up button which shall execute rolling of dice."""
    if choice == "1 dice": 
       roll_button = tkinter.Button(window, text="Roll!", width=10, 
        height=2, font=15, bg="white", bd=2, command=display_one_dice)

    elif choice == "2 dice": 
        roll_button = tkinter.Button(window, text="Roll!", width=10, 
        height=2, font=15, bg="white", bd=2, command=display_two_dice)
    
    elif choice == "30sec": 
        roll_button = tkinter.Button(window, text="Roll!", width=10, 
        height=2, font=15, bg="white", bd=2, command=display_secs_dice)
    
    # Positioning Button.
    roll_button.pack(expand=True, padx=10, pady=15)


def display_one_dice():
    """
    Displays rolling of one dice using Tkinter.
    """
    # unicode representation of dice dots (1-6)
    dice_dots = ["\u2680", "\u2681", "\u2682", "\u2683", "\u2684", "\u2685"]

    display = f"{dice_dots[one_dice()-1]}"
    label.configure(text=display)
    label.pack(expand=True)  
    

def display_two_dice():
    """
    Displays rolling of two dice using Tkinter.
    """
    # unicode representation of dice dots (1-6)
    dice_dots = ["\u2680", "\u2681", "\u2682", "\u2683", "\u2684", "\u2685"]

    display = f"{dice_dots[one_dice()-1]} {dice_dots[one_dice()-1]}"
    label.configure(text=display)
    label.pack(expand=True) 


def display_secs_dice():
    """
    Displays rolling of 30 SECONDS dice using Tkinter.
    """
    # strings are unicode by default.
    label.configure(text=str(secs_dice()))
    label.pack(expand=True) 
    

def roll_again():
    """
    Determines whether user would like to continue simulating dice rolls.
    """
    message = "Would You Like to Simulate Rolling Again, "  
    message += "Specifying Which Dice to Roll?"
    message += "Choice (Any Key to Stop / Y to Continue): "

    if input(message).strip().upper() == 'Y': return True
    else: return False


def dice_simulator():
    """Simulates rolling of dice until user closes Tkinter window."""
    cont_roll = True
    
    while cont_roll:
        choice = dice_choice()
        
        print("Repeateadly Click Roll Button That Will Appear " + 
            "on Screen to Roll Dice.")
        
        window_setup()
        button_setup(choice)
        window.mainloop()

        # Allows user to change Dice / Exit Simulation.
        cont_roll = roll_again()
    

if __name__ == "__main__":
    dice_simulator()