import reflex as rx
from CS_Interview import style
from CS_Interview.state import State
from reflex import Input


def menu() -> rx.Component:
    return rx.box(
        rx.link(
            "Home",
            href="/",
            style=style.nav_link_style,
        ),
        rx.link(
            "signin",
            href="/signin",
            style=style.nav_link_style,
        ),
        rx.link(
            "signup",
            href="/signup",
            style=style.nav_link_style,
        ),
        style=style.nav_style,
    )


def search_input():
    return Input(
        type="search",
        autocomplete="off",
        id="mantine-aikol13wn",
        placeholder="검색어를 입력해 주세요",
        role="combobox",
        aria_haspopup="listbox",
        aria_expanded="false",
        aria_autocomplete="list",
        aria_invalid="false",
        data_with_icon="true",
        value="",
        style=style.main_search_style,
    )


@rx.page()
def index() -> rx.Component:
    return rx.box(
        menu(),
        rx.flex(
            rx.vstack(
                rx.text(
                    "이젠 IT 면접 준비는 Reflex로!",
                    style=style.main_text_style,
                ),
                search_input(),
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


class FormState(rx.State):
    form_data: dict = {}

    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        self.form_data = form_data


@rx.page("/signin")
def signin():
    return rx.box(
        rx.box(
            rx.hstack(
                rx.box(
                    rx.form(
                        rx.vstack(
                            rx.heading("Sign In"),
                            rx.box(
                                rx.input(
                                    placeholder="First Name",
                                    name="first_name",
                                )
                            ),
                            rx.input(
                                placeholder="Last Name",
                                name="last_name",
                            ),
                            rx.button(
                                "Sign in",
                                type_="submit",
                            ),
                        ),
                        on_submit=FormState.handle_submit,
                        reset_on_submit=True,
                    ),
                    width="50%",
                    height="100%",
                    text_align="center",
                    display="flex",
                    justify_content="center",
                    align_items="center",
                ),
                rx.box(
                    rx.form(
                        rx.vstack(
                            rx.heading(
                                "Please Join Us Page!",
                            ),
                            rx.text(
                                "Enter your personal details and start journey with us",
                                font_size="1em",
                            ),
                            rx.link(
                                rx.button(
                                    "Sign Up",
                                    border="1px solid #FFFFFF",
                                    color="#FFFFFF",
                                    background_color="transparent",
                                    font_weight="bold",
                                    padding="12px 45px",
                                    letter_spacing="1px",
                                    text_transform="uppercase",
                                    border_radius="1em",
                                    # box_shadow="rgba(151, 65, 252, 0.8) 0 15px 30px -10px",
                                    box_sizing="border-box",
                                    # opacity="0.6",
                                    _hover={
                                        "opacity": 1,
                                    },
                                ),
                                href="/signup",
                                button=True,
                            ),
                        ),
                    ),
                    width="50%",
                    height="100%",
                    background_image="linear-gradient(#FF4B2B, #FF416C)",
                    text_align="center",
                    display="flex",
                    justify_content="center",
                    align_items="center",
                ),
                width="100%",
                height="480px",
            ),
            border_radius="10px",
            box_shadow="0 14px 28px rgba(0,0,0,0.25), 0 10px 10px rgba(0,0,0,0.22)",
            position="relative",
            overflow="hidden",
            width="768px",
            max_width="100%",
            min_height="480px",
            display="flex",
            justify_content="center",
            align_items="center",
        ),
        display="flex",
        justify_content="center",
        align_items="center",
        height="100vh",
    )


@rx.page("/signup")
def signup():
    return rx.box(
        rx.box(
            border_radius="10px",
            box_shadow="0 14px 28px rgba(0,0,0,0.25), 0 10px 10px rgba(0,0,0,0.22)",
            position="relative",
            overflow="hidden",
            width="480px",
            max_width="100%",
            min_height="768px",
            display="flex",
            justify_content="center",
            align_items="center",
        ),
        display="flex",
        justify_content="center",
        align_items="center",
        height="100vh",
    )


app = rx.App()
app.compile()
