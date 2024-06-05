import os
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI



load_dotenv()

GOOGLE_API_KEY=os.getenv('GOOGLE_API_KEY')
os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY

def ask_bot(message):
    llm= ChatGoogleGenerativeAI(model="gemini-pro")
    
    response=llm.invoke(message)
    
    return response.content

if __name__ == "__main__":
    print("welcome to the chat bot!")
    
    message=ask_bot("what is the meaning of large language models")
    print(message)
            
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                