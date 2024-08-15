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

def update_context(user_profile, user_input, ai_response): 
     
    user_profile["context"] += f"\nUser: {user_input}\n AI: {ai_response}"
    if len(user_profile["context"]) > 1000:
        # context = summarize_context(context)
        return
    
def handle_restrictions(user_profile):

    print(f"Welcome to the mealAI ChatBot, {user_profile['name']}! Please let me know if you have any dietary restrictions. \nPlease type 'done' once done with restrictions or type 'exit' to quit the application.")
    restrictions = user_profile['restrictions'] if user_profile['restrictions'] else []
    
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

# Get user feedback 
def get_feedback():
    print("AI: Were the suggestions helpful? (yes/no)")
    feedback = input("You: ")
    if feedback.lower() == "no": 
        reason = input("Please let us know what went wrong!\nYou: ")
        return reason
    return None

def create_or_load_profile(user_id, users_profiles):
    if user_id in users_profiles:
        print(f"Welcome back, {users_profiles[user_id]['name']}!")
        return users_profiles[user_id]
    else:
        name = input("It looks like you're new here! Please enter your name: ")
        user_profile = {
            'name': name,
            'restrictions': [],
            'context': ""
        }
        users_profiles[user_id] = user_profile
        return user_profile

if __name__ == "__main__": 
    users_profiles = {} 
    
    user_id = input("Please enter your user ID or name: ").strip().lower()
    user_profile = create_or_load_profile(user_id, users_profiles)

    handle_restrictions(user_profile)

    feedback = get_feedback()
    if feedback:
        print("Thank you for your feedback!") 

    users_profiles[user_id] = user_profile

