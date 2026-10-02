import os
import random
import sys
import time
if os.name == "nt":
    os.system("")
RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"

GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
WHITE = "\033[97m"


QUESTIONS = [

    {
        "difficulty": "Easy",
        "question": "What is the capital city of France?",
        "options": ["Berlin", "Madrid", "Paris", "Rome"],
        "answer": "C",
        "explanation": "Paris is the capital and most populous city of France."
    },
    {
        "difficulty": "Easy",
        "question": "Which planet is known as the 'Red Planet'?",
        "options": ["Venus", "Mars", "Jupiter", "Saturn"],
        "answer": "B",
        "explanation": "Mars appears reddish because of iron oxide (rust) on its surface."
    },
    {
        "difficulty": "Easy",
        "question": "What is the largest mammal currently living on Earth?",
        "options": ["African Bush Elephant", "Blue Whale", "Giraffe", "Colossal Squid"],
        "answer": "B",
        "explanation": "The blue whale can grow up to 100 feet long and weigh nearly 200 tons."
    },
    {
        "difficulty": "Easy",
        "question": "Who painted the world-famous portrait 'Mona Lisa'?",
        "options": ["Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Michelangelo"],
        "answer": "C",
        "explanation": "Leonardo da Vinci began painting the Mona Lisa in Florence around 1503."
    },
    {
        "difficulty": "Easy",
        "question": "What is the name of the magical school Harry Potter attends?",
        "options": ["Durmstrang", "Beauxbatons", "Ilvermorny", "Hogwarts"],
        "answer": "D",
        "explanation": "Harry attends Hogwarts School of Witchcraft and Wizardry in Scotland."
    },
    {
        "difficulty": "Easy",
        "question": "What is the chemical formula for water?",
        "options": ["CO2", "H2O", "NaCl", "O2"],
        "answer": "B",
        "explanation": "Water is formed by two hydrogen atoms bonded to one oxygen atom (H2O)."
    },
    {
        "difficulty": "Easy",
        "question": "In computer technology, what does 'CPU' stand for?",
        "options": [
            "Central Processing Unit",
            "Computer Personal Unit",
            "Central Performance Utility",
            "Core Processor Unit"
        ],
        "answer": "A",
        "explanation": "The Central Processing Unit is often called the 'brain' of the computer."
    },
    {
        "difficulty": "Medium",
        "question": "What is the chemical symbol for the element Gold?",
        "options": ["Ag", "Fe", "Au", "Gd"],
        "answer": "C",
        "explanation": "The symbol 'Au' originates from the Latin word for gold, 'aurum'."
    },
    {
        "difficulty": "Medium",
        "question": "Which is traditionally recognized as the longest river in the world?",
        "options": ["Amazon River", "Nile River", "Yangtze River", "Mississippi River"],
        "answer": "B",
        "explanation": "The Nile River stretches approximately 6,650 kilometers (4,132 miles)."
    },
    {
        "difficulty": "Medium",
        "question": "In which year did the luxury passenger liner RMS Titanic sink?",
        "options": ["1905", "1912", "1918", "1923"],
        "answer": "B",
        "explanation": "The Titanic struck an iceberg and sank in the North Atlantic on April 15, 1912."
    },
    {
        "difficulty": "Medium",
        "question": "How many bones are in the adult human skeleton?",
        "options": ["186", "206", "226", "256"],
        "answer": "B",
        "explanation": "Babies are born with ~270 bones, but many fuse together to form 206 bones in adulthood."
    },
    {
        "difficulty": "Medium",
        "question": "Approximately how long does it take for light from the Sun to reach Earth?",
        "options": ["About 2 minutes", "About 8 minutes", "About 15 minutes", "About 24 minutes"],
        "answer": "B",
        "explanation": "Traveling at ~300,000 km/s, sunlight takes about 8 minutes and 20 seconds to reach Earth."
    },
    {
        "difficulty": "Medium",
        "question": "Who created the Python programming language in 1991?",
        "options": ["James Gosling", "Guido van Rossum", "Dennis Ritchie", "Bjarne Stroustrup"],
        "answer": "B",
        "explanation": "Dutch programmer Guido van Rossum designed Python, naming it after Monty Python's Flying Circus."
    },
    {
        "difficulty": "Medium",
        "question": "What is the smallest sovereign country in the world by land area?",
        "options": ["Monaco", "Nauru", "Vatican City", "San Marino"],
        "answer": "C",
        "explanation": "Vatican City covers an area of just 0.49 square kilometers (121 acres)."
    },

    # ---------- HARD QUESTIONS (6) ----------
    {
        "difficulty": "Hard",
        "question": "What is the rarest naturally occurring element in the Earth's crust?",
        "options": ["Francium", "Astatine", "Californium", "Promethium"],
        "answer": "B",
        "explanation": "Less than 1 gram of astatine is estimated to exist in Earth's crust at any moment due to rapid decay."
    },
    {
        "difficulty": "Hard",
        "question": "Which pre-Columbian civilization built the mountain citadel of Machu Picchu?",
        "options": ["Aztec", "Maya", "Inca", "Olmec"],
        "answer": "C",
        "explanation": "Machu Picchu was built in the 15th century by the Inca Empire high in the Peruvian Andes."
    },
    {
        "difficulty": "Hard",
        "question": "What is the shortest play ever written by William Shakespeare?",
        "options": ["The Comedy of Errors", "Macbeth", "The Tempest", "A Midsummer Night's Dream"],
        "answer": "A",
        "explanation": "At just 1,787 lines and roughly 14,369 words, 'The Comedy of Errors' is his shortest play."
    },
    {
        "difficulty": "Hard",
        "question": "Which planet in our solar system holds the record for the most confirmed moons?",
        "options": ["Jupiter", "Saturn", "Uranus", "Neptune"],
        "answer": "B",
        "explanation": "Saturn leads our solar system with 146 confirmed moons, outnumbering Jupiter's 95."
    },
    {
        "difficulty": "Hard",
        "question": "What is the hardest mineral substance found in the human body?",
        "options": ["Femur Bone", "Tooth Enamel", "Skull Cranium", "Fingernail Keratin"],
        "answer": "B",
        "explanation": "Tooth enamel is composed of 96% minerals (mainly hydroxyapatite), making it harder than bone."
    },
    {
        "difficulty": "Hard",
        "question": "What is the deepest surveyed point in Earth's oceans?",
        "options": ["Puerto Rico Trench", "Challenger Deep", "Java Trench", "Molloy Deep"],
        "answer": "B",
        "explanation": "Challenger Deep, located in the Mariana Trench, plunges approximately 10,928 meters (~35,853 ft) deep."
    }
]
def print_divider(char="=", length=65, color=CYAN):
    print(f"{color}{char * length}{RESET}")


def display_welcome_banner():
    print_divider("=", 65, CYAN)
    print(f"{BOLD}{MAGENTA}")
    print(r"   ____  _    _ _____ ______   _____          __  __ ______ ")
    print(r"  / __ \| |  | |_   _|___  /  / ____|   /\   |  \/  |  ____|")
    print(r" | |  | | |  | | | |    / /  | |  __   /  \  | \  / | |__   ")
    print(r" | |  | | |  | | | |   / /   | | |_ | / /\ \ | |\/| |  __|  ")
    print(r" | |__| | |__| |_| |_ / /__  | |__| |/ ____ \| |  | | |____ ")
    print(r"  \___\_\\____/|_____/_____|  \_____/_/    \_\_|  |_|______|")
    print(f"{RESET}")
    print_divider("=", 65, CYAN)
    print(f"{BOLD}{WHITE} Welcome to the Ultimate Python Trivia Quiz Challenge!{RESET}")
    print(f"{DIM} Test your knowledge across Science, History, Tech, Pop Culture & more.{RESET}")
    print_divider("-", 65, CYAN)


def choose_difficulty():
    print(f"\n{BOLD}{YELLOW}SELECT YOUR DIFFICULTY LEVEL:{RESET}")
    print(f"  {CYAN}[1]{RESET} {GREEN}Easy{RESET}      (7 fun, beginner-friendly questions)")
    print(f"  {CYAN}[2]{RESET} {YELLOW}Medium{RESET}    (7 thought-provoking trivia questions)")
    print(f"  {CYAN}[3]{RESET} {RED}Hard{RESET}      (6 challenging master-level questions)")
    print(f"  {CYAN}[4]{RESET} {MAGENTA}Mixed{RESET}     (All 20 questions in random order!)")
    print(f"  {CYAN}[Q]{RESET} {DIM}Quit game{RESET}")

    choices = {
        "1": ("Easy", [q for q in QUESTIONS if q["difficulty"] == "Easy"]),
        "2": ("Medium", [q for q in QUESTIONS if q["difficulty"] == "Medium"]),
        "3": ("Hard", [q for q in QUESTIONS if q["difficulty"] == "Hard"]),
        "4": ("Mixed (All 20 Questions)", QUESTIONS.copy()),
    }

    while True:
        choice = input(f"\n{BOLD}Enter your choice (1-4 or Q): {RESET}").strip().upper()
        if choice in choices:
            mode_name, selected_questions = choices[choice]
            return mode_name, selected_questions
        elif choice == "Q":
            print(f"\n{YELLOW}Thanks for checking out the Quiz Game! See you next time! 👋{RESET}\n")
            sys.exit(0)
        else:
            print(f"{RED}Invalid selection. Please type 1, 2, 3, 4, or Q.{RESET}")


def get_difficulty_badge(difficulty):
    if difficulty == "Easy":
        return f"{GREEN}[EASY]{RESET}"
    elif difficulty == "Medium":
        return f"{YELLOW}[MEDIUM]{RESET}"
    elif difficulty == "Hard":
        return f"{RED}[HARD]{RESET}"
    return f"{WHITE}[{difficulty}]{RESET}"


def display_question(q_data, index, total):

    badge = get_difficulty_badge(q_data["difficulty"])
    print_divider("-", 65, BLUE)
    print(f"{BOLD}Question {index} of {total}{RESET}  {badge}")
    print_divider("-", 65, BLUE)
    print(f"\n{BOLD}{WHITE}{q_data['question']}{RESET}\n")

    option_labels = ["A", "B", "C", "D"]
    for label, option_text in zip(option_labels, q_data["options"]):
        print(f"   {CYAN}{BOLD}{label}){RESET} {option_text}")
    print()


def get_user_answer():

    valid_options = {"A", "B", "C", "D", "Q"}
    while True:
        user_input = input(f"{BOLD}Your Answer (A, B, C, D or Q to quit): {RESET}").strip().upper()
        if user_input in valid_options:
            return user_input
        print(f"{RED}Invalid input! Please enter A, B, C, or D (or Q to quit).{RESET}")


def calculate_grade(score, total):
    if total == 0:
        return 0.0, "N/A", "No questions were played."

    percentage = (score / total) * 100

    if percentage == 100:
        return percentage, "🏆 Grandmaster Quiz Champion", "Flawless victory! You got every single question right!"
    elif percentage >= 80:
        return percentage, "🌟 Trivia Expert", "Impressive knowledge! You clearly know your stuff!"
    elif percentage >= 60:
        return percentage, "🎓 Solid Achiever", "Well done! A very respectable performance."
    elif percentage >= 40:
        return percentage, "📚 Aspiring Scholar", "Good try! A bit more practice and you'll be at the top."
    else:
        return percentage, "🌱 Curious Explorer", "Every master was once a beginner. Keep learning and try again!"


def display_final_results(score, total, round_history, mode_name):
    percentage, rank_title, feedback_msg = calculate_grade(score, total)

    print("\n" + "=" * 65)
    print(f"{BOLD}{MAGENTA}                 🎉 QUIZ COMPLETE! 🎉{RESET}")
    print("=" * 65)
    print(f"  {BOLD}Mode Played:{RESET}      {CYAN}{mode_name}{RESET}")
    print(f"  {BOLD}Final Score:{RESET}      {YELLOW}{score} / {total}{RESET}")
    print(f"  {BOLD}Accuracy:{RESET}         {GREEN if percentage >= 60 else RED}{percentage:.1f}%{RESET}")
    print(f"  {BOLD}Rank Awarded:{RESET}     {BOLD}{WHITE}{rank_title}{RESET}")
    print(f"  {BOLD}Verdict:{RESET}          {feedback_msg}")
    print_divider("-", 65, CYAN)

    print(f"\n{BOLD}{YELLOW}📝 ROUND SUMMARY & REVIEW:{RESET}")
    for item in round_history:
        status_icon = f"{GREEN}✓ CORRECT{RESET}" if item["is_correct"] else f"{RED}✗ WRONG  {RESET}"
        print(f"\n {status_icon} | {BOLD}Q{item['num']}: {item['question']}{RESET}")
        print(f"   Your Answer:    {CYAN}[{item['user_answer']}]{RESET} {item['user_text']}")
        if not item["is_correct"]:
            print(f"   Correct Answer: {GREEN}[{item['correct_answer']}]{RESET} {item['correct_text']}")
        print(f"   {DIM}💡 {item['explanation']}{RESET}")

    print_divider("=", 65, CYAN)


def play_quiz():
    """
    Runs a single full round of the quiz game:
    1. Selects difficulty
    2. Shuffles the questions
    3. Iterates through each question, showing one at a time
    4. Validates user input and provides instant feedback
    5. Tracks score and summary history
    6. Displays final results
    """
    mode_name, selected_questions = choose_difficulty()
    active_questions = selected_questions.copy()
    random.shuffle(active_questions)

    total_questions = len(active_questions)
    score = 0
    round_history = []

    print(f"\n{BOLD}{GREEN}Starting round:{RESET} {mode_name} ({total_questions} questions)")
    print(f"{DIM}Tip: You can type 'Q' at any prompt to exit early.{RESET}\n")
    time.sleep(1)

    labels = ["A", "B", "C", "D"]

    for index, q_data in enumerate(active_questions, start=1):

        display_question(q_data, index, total_questions)

        user_choice = get_user_answer()

        if user_choice == "Q":
            print(f"\n{YELLOW}You chose to quit the round early.{RESET}")
            break

        correct_letter = q_data["answer"]
        user_option_index = labels.index(user_choice)
        correct_option_index = labels.index(correct_letter)

        user_text = q_data["options"][user_option_index]
        correct_text = q_data["options"][correct_option_index]

        is_correct = (user_choice == correct_letter)

        if is_correct:
            score += 1
            print(f"\n{GREEN}{BOLD}✓ Correct!{RESET} Great job! 🎉")
        else:
            print(f"\n{RED}{BOLD}✗ Incorrect.{RESET} The correct answer is {GREEN}[{correct_letter}] {correct_text}{RESET}.")

        print(f"{DIM}💡 {q_data['explanation']}{RESET}")
        print(f"{DIM}Current Score: {score}/{index}{RESET}\n")

        round_history.append({
            "num": index,
            "question": q_data["question"],
            "user_answer": user_choice,
            "user_text": user_text,
            "correct_answer": correct_letter,
            "correct_text": correct_text,
            "is_correct": is_correct,
            "explanation": q_data["explanation"]
        })

        time.sleep(0.5)

    questions_played = len(round_history)
    display_final_results(score, questions_played, round_history, mode_name)


def main():
    display_welcome_banner()

    while True:
        play_quiz()
        while True:
            replay_input = input(f"\n{BOLD}Would you like to play another round? (Y/N): {RESET}").strip().upper()
            if replay_input in ("Y", "YES"):
                print("\n" * 2)
                display_welcome_banner()
                break
            elif replay_input in ("N", "NO", "Q"):
                print(f"\n{GREEN}Thank you for playing the Python Quiz Game! Keep learning and have a great day! 👋{RESET}\n")
                return
            else:
                print(f"{RED}Please enter 'Y' for Yes or 'N' for No.{RESET}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{YELLOW}Game interrupted. Goodbye! 👋{RESET}\n")
        sys.exit(0)
