from langchain_google_genai import GoogleGenerativeAIEmbeddings
import google.generativeai as genai
from langchain.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))



def load_faiss_db():
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vector_store = FAISS.load_local("faiss_sports", embeddings)
    return vector_store

def ask_question(question, vector_store):
    # Load conversational chain
    model = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.3)
    prompt_template = """
    Answer the question as detailed as possible from the provided context or related internet context, make sure to provide all the details, if the answer is not in
    provided context then just make an appropriate answers as user need as related to the context as according to you\n\n
    Context:\n {context}?\n
    Question: \n{question}\n

    Answer:
    """
    prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
    chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)

    # Search similar documents in FAISS database
    docs = vector_store.similarity_search(question)

    # Get response from conversational chain
    response = chain({"input_documents": docs, "question": question}, return_only_outputs=True)
    return response


import re
def parse_questions(result):
        # Extract the output text from the result
        output_text = result['output_text']
        
        # Split the output text into individual questions using regex
        questions_data = re.findall(r'\d+\..*?(?=\d+\.|\Z)', output_text, re.DOTALL)
        
        # Initialize a list to store parsed questions
        parsed_questions = []

        # Iterate through each question data
        for question_data in questions_data:
            # Split the question data into question, options, and correct answer
            lines = question_data.strip().split('\n')
            question = lines[0].split('?')[0].strip()
            options = [option.strip() for option in lines[1].split('Options:')[1].split(',')]
            correct_answer = lines[2].split('Correct Answer:')[1].strip()

            # Construct a dictionary for the parsed question
            parsed_question = {
                "question": question,
                "options": options,
                "correct_answer": correct_answer
            }

            # Append the parsed question to the list
            parsed_questions.append(parsed_question)

        return parsed_questions


def mainz():
    while True:
        try:
            # Load FAISS database
            vector_store = load_faiss_db()

            # Ask user for input question
            user_question = """make me 10 mcqs based questions, and their related answers,in the given template:(sample_questions = [     {         "question_number": 1,         "question": "Which country won the FIFA World Cup in 2018?",         "options": ["Germany", "Argentina", "France", "Brazil"],         "correct_answer": "France",         "explanation": "France won the FIFA World Cup in 2018 by defeating Croatia in the final."     },     # Add more questions here ]), the mcqs should be easy that any person can try to solve quiz, note: show me output without using special symbols, by using comma seperate the question,note each question and its options should be unique from whole other options of every question"""

            # Get response for the user question
            response = ask_question(user_question, vector_store)

            # Parse the questions from the response
            parsed_questions = parse_questions(response)

            print(parsed_questions)

            return parsed_questions  # If successful, return parsed questions and exit the loop

        except Exception as e:
            print("An error occurred:", e)
            print("Attempting again...")
            print(response)




 
