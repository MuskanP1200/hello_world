"""
FastAPI entry point
"""

from fastapi import FastAPI
from hello_world.hello import get_message

app = FastAPI(title="Hello World API")

@app.get("/")
def read_root(name: str = "World is one"):
    """
    Root endpoint that returns a hello message.
    """
    return {"message": get_message(name)}






# ======================================


# """
# Streamlit app entry point
# """

# import streamlit as st
# from hello_world.hello import get_message

# def run():
#     st.title("🚀 Hello World App")
#     st.write("This is a simple Streamlit app with proper structure.")

#     # Input box
#     name = st.text_input("Enter your name", "World")

#     # Display hello message
#     message = get_message(name)
#     st.success(message)

# if __name__ == "__main__":
#     run()
