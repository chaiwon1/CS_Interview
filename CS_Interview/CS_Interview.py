import reflex as rx
from CS_Interview import style
from CS_Interview.state import State
from reflex import Input
from typing import List


career_options: List[str] = ["신입", "1-3년", "4-6년", "7년 이상"]
language_options: List[str] = ["Python", "Java", "C", "C#", "C++", "Go", "Rust", "기타"]


class FormState(rx.State):
    form_data: dict = {}

    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        self.form_data = form_data


class SelectState(rx.State):
    option: str = "No selection yet."


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
                rx.text("이젠 IT 면접 준비는 RehearserAI로!", style=style.main_text_style),
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
                                rx.password(
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
                                "지금 빠르게 회원가입을 하고 RehearserAI를 시작해보세요!",
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
                    style=style.signin_right_pannel_style,
                ),
                style=style.signin_stack_style,
            ),
            style=style.signin_inbox_style,
        ),
        style=style.signin_outbox_style,
    )


@rx.page("/signup")
def signup():
    return rx.box(
        menu(),
        rx.box(
            rx.hstack(
                rx.box(
                    rx.vstack(
                        rx.heading(
                            "가입 정보가 기억나셨나요?",
                            style=style.signin_right_pannel_header_style,
                        ),
                        rx.box(
                            rx.text(
                                "RehearserAI를 계속 이용하기 위해",
                                style=style.signin_right_pannel_text_style,
                            ),
                            rx.text(
                                "로그인 페이지로 돌아가 가입 정보로 로그인 해주세요!",
                                style=style.signin_right_pannel_text_style,
                            ),
                        ),
                        rx.box(
                            rx.link(
                                rx.button(
                                    "로그인",
                                    style=style.signin_right_pannel_button_style,
                                ),
                                href="/signin",
                                button=True,
                            ),
                            style=style.signin_pannel_box_style,
                        ),
                        width="100%",
                    ),
                    style=style.signin_right_pannel_style,
                ),
                rx.box(
                    rx.form(
                        rx.vstack(
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
                                rx.password(
                                    placeholder="비밀번호를 입력해주세요.",
                                    as_="b",
                                    name="password1",
                                    style=style.signin_left_pannel_input_style,
                                ),
                                style=style.signin_pannel_box_style,
                            ),
                            rx.box(
                                rx.text(
                                    "비밀번호 확인", style=style.signin_left_pannel_text_style
                                ),
                                rx.password(
                                    placeholder="비밀번호를 다시 입력해주세요.",
                                    as_="b",
                                    name="password2",
                                    style=style.signin_left_pannel_input_style,
                                ),
                                style=style.signin_pannel_box_style,
                            ),
                            rx.box(
                                rx.text(
                                    "이름", style=style.signin_left_pannel_text_style
                                ),
                                rx.password(
                                    placeholder="이름을 입력해주세요.",
                                    as_="b",
                                    name="username",
                                    style=style.signin_left_pannel_input_style,
                                ),
                                style=style.signin_pannel_box_style,
                            ),
                            rx.box(
                                rx.text(
                                    "연차", style=style.signin_left_pannel_text_style
                                ),
                                rx.select(
                                    career_options,
                                    placeholder="Select an example.",
                                    on_change=SelectState.set_option,
                                    color_schemes="twitter",
                                ),
                                style=style.signin_pannel_box_style,
                            ),
                            rx.box(
                                rx.text(
                                    "사용 언어", style=style.signin_left_pannel_text_style
                                ),
                                rx.select(
                                    language_options,
                                    placeholder="Select an example.",
                                    on_change=SelectState.set_option,
                                    color_schemes="twitter",
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
                style=style.signin_stack_style,
            ),
            style=style.signup_inbox_style,
        ),
        style=style.signin_outbox_style,
    )


@rx.page("/labs")
def labs():
    return rx.box(
        menu(),
        rx.box(
            rx.vstack(
                search_input(),
                rx.grid(
                    rx.grid_item(
                        rx.card(
                            rx.text(
                                "Body of the Card Component",
                            ),
                            header=rx.heading("Header", size="lg"),
                            footer=rx.heading("Footer", size="sm"),
                        ),
                        row_span=1,
                        col_span=1,
                    ),
                    rx.grid_item(
                        rx.card(
                            rx.text("Body of the Card Component"),
                            header=rx.heading("Header", size="lg"),
                            footer=rx.heading("Footer", size="sm"),
                        ),
                        row_span=1,
                        col_span=1,
                    ),
                    rx.grid_item(
                        rx.card(
                            rx.text("Body of the Card Component"),
                            header=rx.heading("Header", size="lg"),
                            footer=rx.heading("Footer", size="sm"),
                        ),
                        row_span=1,
                        col_span=1,
                    ),
                    rx.grid_item(
                        rx.card(
                            rx.text("Body of the Card Component"),
                            header=rx.heading("Header", size="lg"),
                            footer=rx.heading("Footer", size="sm"),
                        ),
                        row_span=1,
                        col_span=1,
                    ),
                    rx.grid_item(
                        rx.card(
                            rx.text("Body of the Card Component"),
                            header=rx.heading("Header", size="lg"),
                            footer=rx.heading("Footer", size="sm"),
                        ),
                        row_span=1,
                        col_span=1,
                    ),
                    rx.grid_item(
                        rx.card(
                            rx.text("Body of the Card Component"),
                            header=rx.heading("Header", size="lg"),
                            footer=rx.heading("Footer", size="sm"),
                        ),
                        row_span=1,
                        col_span=1,
                    ),
                    template_columns="repeat(3, 1fr)",
                    gap=4,
                ),
                style=style.labs_grid_style,
            )
        ),
    )


app = rx.App()
app.compile()
