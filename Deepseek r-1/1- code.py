# from langchain_core.prompts import ChatPromptTemplate

# from langchain_ollama import OllamaLLM
# from langchain_ollama import OllamaLLM

# model = OllamaLLM(model="llama3")

# # Define the prompt template
# template = """Question: {question}

# Answer: Let's think step by step."""

# # Create the prompt template using the given template
# prompt = ChatPromptTemplate.from_template(template)

# # Initialize the model (use your desired model)
# # model = OllamaLLM(model="deepseek-r1")

# # Create a chain with the prompt and the model
# chain = prompt | model

# # Capture user input
# question = input("Enter your question here: ")

# # If the user has entered a question, format the prompt and invoke the chain
# if question:
#     try:
#         # Format the input question with the template
#         formatted_prompt = prompt.format(question=question)
        
#         # Pass the formatted prompt directly to the model (invoke chain)
#         response = chain.invoke({"question": question})  # Pass it as a dictionary
        
#         # Display the response from the model
#         print("Response:", response)
#     except Exception as e:
#         print(f"Error: {e}")






from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import OllamaLLM

# Prompt template
template = """Question: {question}

Answer: Let's think step by step.
"""

prompt = ChatPromptTemplate.from_template(template)

# NEW correct model class
model = OllamaLLM(model="deepseek-r1")

# Create chain
chain = prompt | model

# Input from user
question = input("Enter your question here: ")

if question:
    try:
        response = chain.invoke({"question": question})
        print("\nResponse:\n", response)
    except Exception as e:
        print("Error:", e)