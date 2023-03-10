"""Welcome to Pynecone! This file outlines the steps to create a basic app."""
from pcconfig import config
import qbreader 
import pynecone as pc

docs_url = "https://pynecone.io/docs/getting-started/introduction"
filename = f"{config.app_name}/{config.app_name}.py"


class State(pc.State):

    question_type = "all"
    setName = ""
    randomizer = ""
    difficulty: list = []
    packet = "2023 ACF Regionals"
    def question_logic(self):
        pass
    def random_question(self):
        return qbreader.query(questionType = self.question_type, randomize=self.randomizer, difficulties = self.difficulty)
    
    def query_packet(self):
        return print(qbreader.packet(self.packet, 65))


def index():
    return pc.center(
        pc.vstack(
            pc.heading("Welcome to Pynecone!", font_size="2em"),
            pc.button(
                "Get Started",
                on_click = [State.question_logic]
            ),
            spacing="1.5em",
            font_size="2em",
        ),
        padding_top="10%",
    )


# Add state and page to the app.
app = pc.App(state=State)
app.add_page(index)
app.compile()
