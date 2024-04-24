import reflex as rx
from CS_Interview import style

def menu() -> rx.Component:
    return rx.box(
        rx.link(
            rx.button(
                "HOME",
                variant="ghost",
            ),
            href="/",
            style=style.nav_link_style,
            button=True,
        ),
        rx.link(
            rx.button(
                "SIGNIN",
                variant="ghost",
            ),
            href="/signin",
            style=style.nav_link_style,
            button=True,
        ),
        rx.link(
            rx.button(
                "SIGNUP",
                variant="ghost",
            ),
            href="/signup",
            style=style.nav_link_style,
            button=True,
        ),
        rx.link(
            rx.button(
                "LABS",
                variant="ghost",
            ),
            href="/labs",
            style=style.nav_link_style,
            button=True,
        ),
        style=style.nav_style,
    )

@rx.page()
def index() -> rx.Component:
    return rx.box(
        menu(),
        rx.flex(
            rx.vstack(
                rx.text("이젠 IT 면접 준비는 RehearserAI로!", style=style.main_text_style),
                rx.link(
                    rx.button(
                        "로그인 페이지로 이동",
                        style=style.main_button_style,
                    ),
                    href="/signin",
                    button=True,
                ),
            ),
            style=style.main_flex_style,
        ),
    )


app = rx.App()
app.add_page(index, route="/")
# app.add_page(signin, route="/signin")
# app.add_page(signup, route="/signup")