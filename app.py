import chainlit as cl
from src.llm import ask_bot



'''@cl.on_message
async def main(message:cl.Message):
  
    # Send a response back to the user
    await cl.Message(
        content=f"Received: {message.content}",
    ).send()'''