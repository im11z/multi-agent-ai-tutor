from agents.tutor_agent import explain_topic
from agents.quiz_agent import generate_quiz
from agents.evaluator_agent import evaluate_answer
from agents.feedback_agent import give_feedback
from memory.progress_memory import ProgressMemory

memory = ProgressMemory()

print("AI Multi-Agent Tutor")

topic = input("Enter topic: ")

print("\n--- Explanation ---\n")
print(explain_topic(topic))

print("\n--- Quiz ---\n")

quiz = generate_quiz(topic)

# Hide correct answer
question_only = quiz.split("Correct Answer")[0]

print(question_only)

answer = input("\nYour answer (A/B/C/D): ").strip().upper()

print("\n--- Evaluation ---\n")

evaluation = evaluate_answer(question_only, answer)

print(evaluation)

correct = "Correct" in evaluation
memory.update(correct)

print("\n--- Feedback ---\n")

feedback = give_feedback(topic, evaluation)
print(feedback)

print("\n--- Progress ---\n")
print(memory.stats())