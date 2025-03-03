import openai

def generate_quiz_questions(topic, num_questions=5):
    prompt = f"Generate {num_questions} multiple-choice questions on {topic}."
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

# Example usage
if __name__ == '__main__':
    questions = generate_quiz_questions("Machine Learning Basics")
    print(questions)