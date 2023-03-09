import os

print("Welcome to the interactive story of Lizbeth, a talented programmer from Puerto Rico!\n")
name = input("What is your name?\n")

print(f"\nNice to meet you, {name}! Let's begin.")

print("\nLizbeth is a young woman from Puerto Rico who is part of Gen Z.")
print("She studies full-stack development at HolbertonPR and is fluent in both Spanish and English.")
print("Despite her youth, she is a talented programmer with a passion for technology and innovation.")

print("\nOne day, Lizbeth was working on a project when she received an urgent call from her boss, Gabriel.")
print("Gabriel explained that a powerful hacker had breached the company's servers and stolen sensitive information.")
print("He pleaded with Lizbeth to help, as she was their best hope for stopping the hacker and preventing further damage.")

print("\nLizbeth had a choice to make. What should she do?")

print("Option 1: Agree to help Gabriel and dive into the company's servers to stop the hacker.")
print("Option 2: Refuse to help and focus on her own work instead.")

option = input("What should Lizbeth do? Enter 1 or 2.\n")

if option == "1":
    print("\nLizbeth was shocked but immediately sprang into action. She knew this was a serious situation that required her full attention and expertise.")
    print("She quickly gathered her tools and prepared to enter the company's servers.")

    print("\nAs she navigated the maze-like network, Lizbeth could feel the hacker's presence growing stronger.")
    print("She knew she had to act fast before they could do any more damage.")

    print("\nWith her expert coding skills and quick reflexes, Lizbeth managed to track down the hacker and engage in a tense battle of wits.")
    print("The hacker was a formidable opponent, using advanced techniques to try to block Lizbeth's every move.")

    print("\nBut Lizbeth was not deterred. She knew she had to stay calm and keep her wits about her.")
    print("She finally managed to break through the hacker's defenses and gain access to their system.")

    print("\nWith a flurry of keystrokes, Lizbeth quickly set to work neutralizing the hacker's attack and securing the company's data.")
    print("After a few intense minutes, she emerged victorious.")

    print("\nGabriel was overjoyed and thanked Lizbeth for her quick thinking and skillful work.")
    print("He marveled at how she had managed to defeat a hacker that had stumped even their best security experts.")

    print("\nAs Lizbeth went back to her work, she noticed a message on her computer screen from a secret admirer named KP.")
    print("KP had been watching Lizbeth's work and was impressed by her skill and bravery.")
    print("The message read, 'Lizbeth, you are an amazing programmer. I am in awe of your talent and your courage. Would you like to go out with me sometime?'")

    print("\nLizbeth had a choice to make. What should she do?")

    print("Option 1: Set a date and time for the date.")
    print("Option 2: Politely decline KP's invitation and focus on her work instead.")

option2 = input("What should Lizbeth do? Enter 1 or 2.\n")

if option2 == "1":
    date = input("\nEnter a date and time for the date in YYYY-MM-DD HH:MM format.\n")
    
    with open ("date.txt", "w") as f:
        f.write(date)
        
    print("\nLizbeth was flattered by KP's invitation and excited to go on a date with him.")

    print("\nLizbeth and KP went on a wonderful date and had a great time getting to know each other.")

if option2 == "2":

    print("\nInvalid option. Please try again.")