shadow = "rgba(0, 0, 0, 0.15) 0px 2px 8px"
background = "linear-gradient(10deg,#52b8f1,#d889fd)"

# nav bar
nav_style = dict(
    position="fixed",
    top=0,
    left=0,
    width="100%",
    height="4em",
    display="flex",
    align_items="center",
    justify_content="flex-start",
    padding="0 2em",
    box_shadow=shadow,
    z_index=1,
)

nav_link_style = dict(
    margin="0 1em",
    color="black",
    _hover={
        "text-decoration": None,
    },
)


# main page
main_flex_style = dict(
    display="flex",
    justify_content="center",
    align_items="center",
    height="100vh",
)

main_text_style = dict(
    font_size="48px",
    font_weight="700",
    background=background,
    letter_spacing="1.6px",
    color="transparent",
    background_clip="text",
    margin="10px 0",
    font_family="'Montserrat', sans-serif",
)

main_search_style = dict(
    padding="2em 2em",
    box_shadow=shadow,
    width="100%",
    border_radius="3em",
)

main_button_style = dict(
    border_radius="1em",
    box_shadow="rgba(151, 65, 252, 0.8) 0 15px 30px -10px",
    background_image=background,
    box_sizing="border-box",
    color="white",
    opacity="0.7",
    _hover={
        "opacity": 1,
    },
    margin="20px 0",
)


# signin page
signin_outbox_style = dict(
    display="flex",
    justify_content="center",
    align_items="center",
    height="100vh",
)

signin_inbox_style = dict(
    border_radius="1em",
    box_shadow=shadow,
    position="relative",
    overflow="hidden",
    width="768px",
    max_width="100%",
    min_height="480px",
    display="flex",
    justify_content="center",
    align_items="center",
)

signin_stack_style = dict(
    width="100%",
    height="480px",
)

signin_left_pannel_style = dict(
    width="50%",
    height="100%",
    text_align="center",
    display="flex",
    justify_content="center",
    align_items="center",
)

signin_right_pannel_style = dict(
    width="50%",
    height="100%",
    background_image=background,
    text_align="center",
    display="flex",
    justify_content="center",
    align_items="center",
)

signin_pannel_box_style = dict(
    width="80%",
)

signin_left_pannel_header_style = dict(
    font_size="1.5em",
    margin="0 0 30px 0",
    width="80%",
)

signin_left_pannel_text_style = dict(
    text_align="left",
    color="gray",
    margin="0 0 5px 5px",
    font_size="14px",
    font_weight="bold",
)

signin_left_pannel_input_style = dict(
    background_color="transparent",
    margin="0 0 20px 0",
    width="100%",
    height="42px",
    border_radius="10px",
)

signin_left_pannel_button_style = dict(
    background_color="white",
    border="1px solid #dcdcdc",
    width="50%",
    margin="10px 0",
    border_radius="30px",
    _hover={
        "background_color": "#52b8f1",
        "color": "white",
        "box_shadow": "rgba(0, 0, 0, 0.15) 0px 2px 8px",
        "border": "None",
    },
)

signin_right_pannel_header_style = dict(
    font_size="1.5em",
    margin="0 0 10px 0",
    width="80%",
    color="white",
)

signin_right_pannel_text_style = dict(
    text_align="center",
    color="white",
    font_size="14px",
)

signin_right_pannel_button_style = dict(
    background_color="transparent",
    border="1px solid white",
    color="white",
    width="60%",
    margin="20px 0",
    border_radius="30px",
    _hover={
        "background_color": "white",
        "color": "black",
        "box_shadow": "rgba(0, 0, 0, 0.15) 0px 2px 8px",
        "border": "None",
    },
)