import json

class Chatbot:
    def __init__(self, filename='knowledge.json'):
        self.filename = filename
        self.load_knowledge()

    def load_knowledge(self):
        try:
            with open(self.filename, 'r') as f:
                self.knowledge = json.load(f)
        except FileNotFoundError:
            self.knowledge = {}

    def save_knowledge(self):
        with open(self.filename, 'w') as f:
            json.dump(self.knowledge, f)

    def learn(self, question, answer):
        self.knowledge[question.lower()] = answer
        self.save_knowledge()

    def get_response(self, question):
        return self.knowledge.get(question.lower(), None)

    def handle_input(self, user_input):
        responses = []
        questions = user_input.split('.')
        if len(questions) == 1:
            questions = user_input.split(',')
        
        for question in questions:
            question = question.strip()
            if question:
                response = self.get_response(question)
                if response:
                    responses.append(response)
                else:
                    answer = input(f"I don't know the answer to '{question}'. What should I respond? ")
                    self.learn(question, answer)
                    responses.append(answer)
        return ' '.join(responses)

def main():
    bot = Chatbot()
    print("Enter your questions for the chatbot. Use '.' or ',' to separate multiple questions.")
    print("Type 'exit' or 'quit' to end the chat.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            print("Goodbye!")
            break
        response = bot.handle_input(user_input)
        print("Bot:", response)

if __name__ == "__main__":
    main()
