import time
import random

def multiplication_practice():
    print("=" * 50)
    print("   FOURTH GRADE MULTIPLICATION PRACTICE")
    print("=" * 50)
    print()

    # Get the multiplication table to practice
    while True:
        try:
            table_num = int(input("Which multiplication table do you want to practice? (1-12): "))
            if 1 <= table_num <= 12:
                break
            else:
                print("Please enter a number between 1 and 12.")
        except ValueError:
            print("Please enter a valid number.")

    # Get timer setting (default is 105 seconds)
    print(f"\nDefault timer is 105 seconds.")
    timer_input = input("Press Enter for default, or enter custom time in seconds: ")

    if timer_input.strip() == "":
        timer_seconds = 105
    else:
        try:
            timer_seconds = int(timer_input)
            if timer_seconds <= 0:
                print("Using default timer of 105 seconds.")
                timer_seconds = 105
        except ValueError:
            print("Invalid input. Using default timer of 105 seconds.")
            timer_seconds = 105

    print(f"\nGreat! You'll practice the {table_num} times table for {timer_seconds} seconds.")
    print("Type your answers and press Enter. Good luck!")
    print("\nPress Enter when you're ready to start...")
    input()

    # Initialize game variables
    correct_answers = 0
    total_questions = 0
    start_time = time.time()
    end_time = start_time + timer_seconds

    print(f"\n🚀 GO! You have {timer_seconds} seconds!")
    print("-" * 30)

    # Main game loop
    while time.time() < end_time:
        # Generate random problem (table_num × 1-12)
        multiplier = random.randint(1, 12)
        correct_answer = table_num * multiplier

        # Calculate remaining time
        remaining_time = int(end_time - time.time())

        if remaining_time <= 0:
            break

        print(f"\nTime left: {remaining_time}s")

        try:
            user_answer = int(input(f"{table_num} × {multiplier} = "))
            total_questions += 1

            if user_answer == correct_answer:
                print("✓ Correct! Great job!")
                correct_answers += 1
            else:
                print(f"✗ Sorry, the answer is {correct_answer}")

        except ValueError:
            print("Please enter a number only.")
            continue
        except KeyboardInterrupt:
            print("\n\nGame stopped by user.")
            break

    # Game over - show results
    print("\n" + "=" * 40)
    print("⏰ TIME'S UP!")
    print("=" * 40)

    if total_questions > 0:
        percentage = (correct_answers / total_questions) * 100
        print(f"📊 RESULTS:")
        print(f"   Correct answers: {correct_answers}")
        print(f"   Total questions: {total_questions}")
        print(f"   Accuracy: {percentage:.1f}%")

        # Encouraging messages based on performance
        if percentage >= 90:
            print("🌟 EXCELLENT! You're a multiplication star!")
        elif percentage >= 75:
            print("👍 GREAT JOB! Keep practicing!")
        elif percentage >= 50:
            print("👌 GOOD WORK! You're getting better!")
        else:
            print("💪 KEEP PRACTICING! You'll improve with time!")
    else:
        print("No questions were answered. Try again!")

    print(f"\nYou practiced the {table_num} times table.")
    print("Thanks for practicing multiplication! 🎉")

def main():
    while True:
        multiplication_practice()

        play_again = input("\nWould you like to practice again? (y/n): ").lower().strip()
        if play_again not in ['y', 'yes']:
            print("Goodbye! Keep practicing your multiplication! 📚")
            break
        print("\n")

if __name__ == "__main__":
    main()
