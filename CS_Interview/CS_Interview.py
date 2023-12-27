"""Welcome to Reflex! This file outlines the steps to create a basic app."""
from rxconfig import config

import reflex as rx

from CS_Interview import style

from CS_Interview.state import State

docs_url = "https://reflex.dev/docs/getting-started/introduction"
filename = f"{config.app_name}/{config.app_name}.py"


def qa(question: str, answer: str) -> rx.Component:
    """A simple question and answer component."""
    return rx.box(
        rx.box(
            rx.text(question, style=style.question_style),
            text_align="right"),
        rx.box(
            rx.text(answer, style=style.answer_style),
            text_align="left")
    )  

def chat() -> rx.Component:
    """A simple chat component."""
    return rx.box(
        rx.foreach(
            State.chat_history,
            lambda messages: qa(messages[0], messages[1])
        )
    )

def action_bar() -> rx.Component:
    return rx.hstack(
        rx.input(
            value=State.question,
            placeholder="Enter your question",
            on_change=State.set_question,
            style=style.input_style,),
        rx.button(
            "Submit", 
            on_click=State.answer,
            style=style.button_style)
    )

def index() -> rx.Component:
    return rx.container(
        chat(),
        action_bar()
    )

# Add state and page to the app.
app = rx.App()
app.add_page(index)
app.compile()
