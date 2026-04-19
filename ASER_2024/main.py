import random

# Sample questions for reading and arithmetic
reading_questions = [
    {"question": "What is the main idea of the story?", "answer": "The tiger is hungry."},
    {"question": "Who is the main character?", "answer": "The rabbit."},
]

arithmetic_questions = [
    {"question": "What is 7 + 5?", "answer": 12},
    {"question": "What is 10 - 3?", "answer": 7},
]

# Function to get student's answer
def ask_question(question_set):
    question = random.choice(question_set)
    print(f"Question: {question['question']}")
    answer = input("Your answer: ")
    return answer.strip().lower() == str(question['answer']).lower()

# Adaptive learning function based on correct/incorrect answers
def adaptive_learning(level):
    if level == "beginner":
        # Easier questions
        reading_level = reading_questions[:1]
        arithmetic_level = arithmetic_questions[:1]
    else:
        # Slightly harder questions
        reading_level = reading_questions[1:]
        arithmetic_level = arithmetic_questions[1:]
    
    correct_reading = ask_question(reading_level)
    correct_arithmetic = ask_question(arithmetic_level)
    
    if correct_reading and correct_arithmetic:
        print("Great job! You're progressing well!")
    else:
        print("Keep practicing! Don't worry, you'll improve.")

# Main app simulation
def main():
    print("Welcome to SkillSync! Let's start with an assessment.")
    
    # Start with beginner level
    level = "beginner"
    
    # Simulate daily task
    while True:
        print("\nNext Daily Challenge:")
        adaptive_learning(level)
        
        # Check if they want to continue
        continue_playing = input("\nDo you want to continue? (yes/no): ")
        if continue_playing.lower() != "yes":
            print("Thanks for using SkillSync! Keep practicing!")
            break
        else:
            # Move to the next level
            level = "advanced"

if __name__ == "__main__":
    main()