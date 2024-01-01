import reflex as rx
from CS_Interview import style
from CS_Interview.state import State
from reflex import Input


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
        style=style.nav_style,
    )


def search_input():
    return Input(
        type="search",
        autocomplete="off",
        placeholder="검색어를 입력해 주세요",
        role="combobox",
        aria_haspopup="listbox",
        aria_expanded="false",
        aria_autocomplete="list",
        aria_invalid="false",
        data_with_icon="true",
        style=style.main_search_style,
    )


@rx.page()
def index() -> rx.Component:
    return rx.box(
        menu(),
        rx.flex(
            rx.vstack(
                rx.text("이젠 IT 면접 준비는 Reflex로!", style=style.main_text_style),
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
        menu(),
        rx.box(
            rx.hstack(
                rx.box(
                    rx.form(
                        rx.vstack(
                            rx.heading(
                                "이메일로 로그인",
                                style=style.signin_left_pannel_header_style,
                            ),
                            rx.box(
                                rx.text(
                                    "이메일", style=style.signin_left_pannel_text_style
                                ),
                                rx.input(
                                    placeholder="이메일을 입력해주세요.",
                                    as_="b",
                                    name="email",
                                    style=style.signin_left_pannel_input_style,
                                ),
                                style=style.signin_pannel_box_style,
                            ),
                            rx.box(
                                rx.text(
                                    "비밀번호", style=style.signin_left_pannel_text_style
                                ),
                                rx.input(
                                    placeholder="비밀번호를 입력해주세요.",
                                    as_="b",
                                    name="password",
                                    style=style.signin_left_pannel_input_style,
                                ),
                                style=style.signin_pannel_box_style,
                            ),
                            rx.box(
                                rx.button(
                                    "로그인",
                                    type_="submit",
                                    style=style.signin_left_pannel_button_style,
                                ),
                                style=style.signin_pannel_box_style,
                            ),
                        ),
                        on_submit=FormState.handle_submit,
                        reset_on_submit=True,
                        width="100%",
                    ),
                    style=style.signin_left_pannel_style,
                ),
                rx.box(
                    rx.form(
                        rx.vstack(
                            rx.heading(
                                "아직 계정이 없으신가요?",
                                style=style.signin_right_pannel_header_style,
                            ),
                            rx.box(
                                rx.text(
                                    "간단하게 이메일만으로 시작할 수 있습니다.",
                                    style=style.signin_right_pannel_text_style,
                                ),
                                rx.text(
                                    "지금 빠르게 회원가입을 하고 Reflex를 시작해보세요!",
                                    style=style.signin_right_pannel_text_style,
                                ),
                            ),
                            rx.box(
                                rx.link(
                                    rx.button(
                                        "회원가입",
                                        style=style.signin_right_pannel_button_style,
                                    ),
                                    href="/signup",
                                    button=True,
                                ),
                                style=style.signin_pannel_box_style,
                            ),
                            width="100%",
                        ),
                    ),
                    style=style.signin_right_pannel_style,
                ),
                style=style.signin_stack_style,
            ),
            style=style.signin_innerbox_style,
        ),
        style=style.signin_outbox_style,
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
