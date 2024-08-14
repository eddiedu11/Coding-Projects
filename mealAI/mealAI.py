from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = """
Answer the question below.

Here is the conversation history: {context}
Question: {question} 
Answer:
"""

model = OllamaLLM(model="llama3")
prompt = ChatPromptTemplate.from_template(template) 
chain = prompt | model 

context = ""
def update_context(user_input, ai_response): 
    global context 
    context += f"\nUser: {user_input}\n AI: {ai_response}"
    if len(context) > 1000:
        # context = summarize_context(context)
        return
    
def handle_restrictions():
    context = "" 
    print("Welcome to the mealAI ChatBot! Please let me know if you have any dietary restrictions. \nPlease type 'done' once done with restrictions or type 'exit' to quit the application.")
    restrictions = []
    while True:
        user_input = input ("You: ")
        if user_input.lower() == "exit":
            break
        elif user_input.lower() == "done":
            result = chain.invoke({"context": "", "question": "Suggest a meal without:" + ", ".join(restrictions)})
            print("mealAI:",result)
            update_context(", ".join(restrictions), result)
        else:
            restrictions.append(user_input)
            print("AI: Anything else?")

def get_feedback(): 
    return

if __name__ == "__main__": 
    handle_restrictions() 
