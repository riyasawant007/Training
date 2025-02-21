from chainlit import AskUserMessage, Message, on_chat_start


@on_chat_start
async def main():
    res = await AskUserMessage(content="What is your name?", timeout=30).send()
    if res:
        await Message(
            content=f"Your name is: {res['content']}.\nChainlit installation is working!\nYou can now start building your own chainlit apps!",
        ).send()

'''import chainlit as cl


@cl.on_message
async def main(message: cl.Message):
    # Send a response back to the user
    await cl.Message(
        content=f"Received: {message.content}",
    ).send()'''


'''@cl.on_chat_start
def on_chat_start():
    print("A new chat session has started!")

@cl.on_message
def on_message(msg: cl.Message):
    print("The user sent: ", msg.content)

@cl.on_stop
def on_stop():
    print("The user wants to stop the task!")

@cl.on_chat_end
def on_chat_end():
    print("The user disconnected!")

from chainlit.types import ThreadDict

@cl.on_chat_resume
async def on_chat_resume(thread: ThreadDict):
    print("The user resumed a previous chat session!")'''