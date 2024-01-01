shadow = "rgba(0, 0, 0, 0.15) 0px 2px 8px"

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

main_flex_style = dict(
    display="flex",
    justify_content="center",
    align_items="center",
    height="100vh",
)

main_text_style = dict(
    font_size="48px",
    font_weight="700",
    background="linear-gradient(10deg,#52b8f1,#d889fd)",
    letter_spacing="1.6px",
    color="transparent",
    background_clip="text",
    margin="10px 0",
)

main_search_style= dict(
    padding="2em 2em",
    box_shadow=shadow,
    width="100%",
    border_radius="3em",
)

main_button_style = dict(
    border_radius="1em",
    box_shadow="rgba(151, 65, 252, 0.8) 0 15px 30px -10px",
    background_image="linear-gradient(144deg,#AF40FF,#5B42F3 50%,#00DDEB)",
    box_sizing="border-box",
    color="white",
    opacity="0.6",
    _hover={
        "opacity": 1,
    },
    margin="20px 0"
)
