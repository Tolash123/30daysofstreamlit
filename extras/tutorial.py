def example_1():
    from annotated_text import annotated_text

    annotated_text(
        "This ",
        ("is", "verb", "#8ef"),
        " some ",
        ("annotated", "adj", "#faa"),
        ("text", "noun", "#afa"),
        " for those of ",
        ("you", "pronoun", "#fea"),
        " who ",
        ("like", "verb", "#8ef"),
        " this sort of ",
        ("thing", "noun", "#afa"),
    )
example_1()
def example_2():
    from annotated_text import annotated_text, annotation

    annotated_text(
        "Hello ",
        annotation("world!", "noun", color="#8ef", border="1px dashed red"),
    )
example_2()

import streamlit as st
from streamlit_extras.app_logo import add_logo
def example():
    if st.checkbox("Check the logo", value=True):
        add_logo("p.py", height=300)
    else:
        add_logo("lg.jpeg", height=300)
    st.write("👈 Check out the cat in the nav-bar!")


from streamlit_extras.badges import badge
def example_pypi():
    badge(type="pypi", name="plost")
    badge(type="pypi", name="streamlit")

example_pypi()

def example_streamlit():
    badge(type="streamlit", url="https://plost.streamlitapp.com")
    badge(type="github", name="streamlit/streamlit")
    badge(type="twitter", name="streamlit")
    badge(type="buymeacoffee", name="andfanilo")
example_streamlit()

from streamlit_extras.buy_me_a_coffee import button
def example():
    button(username="fake-username", floating=False, width=221)
example()

from camera_input_live import camera_input_live
def example1():
    st.write("# See a new image every second")
    controls = st.checkbox("Show controls")
    image = camera_input_live(show_controls=controls)
    if image is not None:
        st.image(image)
#example1()
from streamlit_card import card
def example2():
    card(
        title="Hello World!",
        text="Some description",
        image="http://placekitten.com/300/250",
        url="https://www.google.com",
    )
example2()
import pandas as pd
import altair as alt
import streamlit.streamlit_extrasget_data
from streamlit_extras.chart_annotations import get_annotations_chart
def example() -> None:
    data: pd.DataFrame = get_data()
    chart: alt.TopLevelMixin = get_chart(data=data)

    chart += get_annotations_chart(
        annotations=[
            ("Mar 01, 2008", "Pretty good day for GOOG"),
            ("Dec 01, 2007", "Something's going wrong for GOOG & AAPL"),
            ("Nov 01, 2008", "Market starts again thanks to..."),
            ("Dec 01, 2009", "Small crash for GOOG after..."),
        ],
    )

    st.altair_chart(chart, use_container_width=True)  # type: ignore