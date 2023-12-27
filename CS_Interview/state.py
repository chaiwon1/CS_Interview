import reflex as rx
import asyncio


class State(rx.State):
    # The current question being asked.
    question: str

    # Keep track of the chat history as a list of (question, answer) tuples.
    chat_history: list[tuple[str, str]]

    async def answer(self):
        # Our chatbot is not very smart right now...
        answer = "I don't know!"
        self.chat_history.append((self.question, answer))
        self.question = ""

        yield

        for i in range(len(answer)):
            await asyncio.sleep(0.1)    # Sleep for 0.1 seconds.
            self.chat_history[-1] = (
                self.chat_history[-1][0],   # question
                answer[:i+1])            # answer
            yield