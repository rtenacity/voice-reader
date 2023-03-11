"""Welcome to Pynecone! This file outlines the steps to create a basic app."""
from pcconfig import config
import qbreader 
import pynecone as pc
import asyncio

docs_url = "https://pynecone.io/docs/getting-started/introduction"
filename = f"{config.app_name}/{config.app_name}.py"

coins = ["tossup", "bonus"]
p1 = qbreader.set_list()
p1.remove('2016 "stanford housewrite"')
packets = p1

class State(pc.State):

    question_type = "tossup"
    randomizer = ""
    difficulty_str: str = ""
    difficulty: list = []
    packet = ""
    categories = ""
    packet_num = 1
    packet_true = True
    question = ""
    packet_questions = {}
    question_word_list:list = []
    on_screen:list = []
    start: bool = False
    x = -1
    
    def question_logic(self):
        try:
            str_list = self.difficulty_str.split("-")
            self.difficulty = list(range(int(str_list[0]), int(str_list[1])+1))
        except:
            pass
        print(self.difficulty)
        if self.packet.strip() != "":
            self.packet_questions = qbreader.packet(setName=self.packet, packetNumber=self.packet_num)
        else:
            self.question = qbreader.random_question(questionType=self.question_type, difficulties=self.difficulty)
            print(self.question)
            self.question_word_list = self.question[0]['question'].split(" ")

    @pc.var
    def reader(self):
        try:
            self.x+=1
            self.on_screen.append(self.question_word_list[self.x])
            return " ".join(self.on_screen)
        except:
            pass

    
    async def tick(self):
        """Update the clock every second."""
        if self.start:
            await asyncio.sleep(0.3)
            return self.tick

    def flip_switch(self, start):
        """Start or stop the clock."""
        self.start = start
        if self.start:
            return self.tick

def index():
    return pc.center(
        pc.hstack(
            pc.box(
            pc.select(
                packets,
                on_change=State.set_packet,
                shadow="md",
                placeholder="Select a packet."
            ),
            width="50%",
            ),
            pc.input(
                placeholder="Difficulty (1-10)",
                width="50%",
                shadow="md",
                on_blur=State.set_difficulty_str,
            ),
            pc.box(
            pc.select(
                coins,
                on_change=State.set_question_type,
                shadow="md",
                placeholder="Select a question type.",
            ),
            width="50%",
            ),
            pc.button(
                "Submit",
                width="50%",
                shadow="md",
                on_click=State.question_logic,
            ),
            pc.switch(is_checked=State.start, on_change=State.flip_switch),
            
            bg="white",
            padding="2em",
            shadow="md",
            border_radius="lg",
            width="50%",
        ),
        pc.text(State.reader),
        width="100%",
        height="100vh",
        bg="radial-gradient(circle at 22% 11%,rgba(62, 180, 137,.20),hsla(0,0%,100%,0) 19%)",
    )


# Add state and page to the app.
app = pc.App(state=State)
app.add_page(index)
app.compile()
