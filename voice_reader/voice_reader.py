"""Welcome to Pynecone! This file outlines the steps to create a basic app."""
from pcconfig import config
import qbreader
import pynecone as pc
import asyncio
import time

docs_url = "https://pynecone.io/docs/getting-started/introduction"
filename = f"{config.app_name}/{config.app_name}.py"

coins = ["tossup"]
p1 = qbreader.set_list()
p1.remove('2016 "stanford housewrite"')
p1.insert(0, "Random Packet")
packets = p1

categories = []

class State(pc.State):
    question_type = "tossup"
    randomizer = ""
    difficulty_str: str = ""
    difficulty: list = []
    packet = ""
    categories = ""
    packet_num = 1
    packet_true = True
    question_num = 0
    question = ""
    packet_questions: dict = {}
    question_word_list: list = []
    on_screen: list = []
    start: bool = False
    x = -2
    packet_tu: list = []
    generated:bool = False
    finished:bool = False
    buzzed:bool = False
    correct_buzz:bool = False
    user_answer:str = ""
    checked_answer:list = []
    answer_status:str = "Buzz"

    def question_logic(self):
        try:
            str_list = self.difficulty_str.split("-")
            self.difficulty = list(range(int(str_list[0]), int(str_list[1]) + 1))
        except:
            pass
        if self.packet.strip() != "Random Packet":
            self.packet_questions = qbreader.packet(
                setName=self.packet, packetNumber=self.packet_num
            )
            self.generated = True

        else:
            question_raw = qbreader.random_question(
                questionType=self.question_type, difficulties=self.difficulty
            )
            self.question = dict(question_raw[0]) 
            print(self.question)
            self.generated = True
            if self.question_type == "tossup":
                self.question_word_list = self.question["question"].split(" ")
            else:
                print(self.question)

    @pc.var
    def reader(self):
        try:
            if self.packet.strip() == "Random Packet":
                    self.x += 1
                    if self.correct_buzz == True:
                        return self.question["question"]
                    self.on_screen.append(self.question_word_list[self.x])
                    return " ".join(self.on_screen)
            else:
                if self.packet_questions != {}:
                    self.packet_tu = self.packet_questions["tossups"]
                    print(self.packet_tu)
                    self.question = self.packet_tu[self.question_num]
                    if self.correct_buzz == True:
                        return self.question["question"]
                    else:
                        print(self.question)
                        self.question_word_list = self.question["question"].split(" ")
                        self.x += 1
                        self.on_screen.append(self.question_word_list[self.x])
                        return " ".join(self.on_screen)
        except:
            if len(self.on_screen) > 1:
                self.finished = True
            return " ".join(self.on_screen)
    
    @pc.var
    def answer_line(self):
        try:
            if self.finished == True or self.correct_buzz == True:
                return (dict(self.question)['answer'])
            else:
                return ""
        except:
            return ""
        
    async def tick(self):
        """Update the clock every second."""
        if self.start:
            await asyncio.sleep(0.15)
            return self.tick

    def flip_switch(self, start):
        """Start or stop the clock."""
        self.start = start
        if self.start:
            return self.tick
    
    def update_question_num(self):
        if self.packet.strip() != "":
            self.question_num +=1
        else:
            pass
    
    def start_timer(self):
        self.start = True
        return self.tick

    def clear(self):
        self.packet_true = True
        self.question_num = 0
        self.question = ""
        self.packet_questions: dict = {}
        self.question_word_list: list = []
        self.on_screen: list = []
        self.start: bool = False
        self.x = -2
        self.packet_tu: list = []
        self.generated:bool = False
        self.finished:bool = False
        self.buzzed:bool = False
        self.correct_buzz:bool = False
        self.user_answer:str = ""
        self.checked_answer:list = []
        self.answer_status:str = "Buzz"
    
    def open_buzz(self):
        self.buzzed = True
        self.start = False

    def buzz_logic(self):
        print(self.question)
        print((dict(self.question)['answer']))
        print(self.user_answer)
        self.checked_answer = qbreader.check_answer(self.question['answer'], self.user_answer)
        print(self.checked_answer)
        if self.checked_answer[0] == "accept":
            self.buzzed = False
            self.correct_buzz = True
            self.start = True
            return self.tick
        elif self.checked_answer[0] == "prompt":
            self.answer_status = "Prompt"+ self.checked_answer[1]
            self.correct_buzz = False
        elif self.checked_answer[0] == "reject":
            self.correct_buzz = False
            self.buzzed = False
            self.start = True
            return self.tick

def index():
    return pc.center(
        pc.vstack(
        
            pc.hstack(
                pc.box(
                    pc.select(
                        packets,
                        on_change=State.set_packet,
                        shadow="md",
                        placeholder="Select a packet.",
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
                    on_click=[State.clear, State.question_logic, State.start_timer],
                ),
                pc.button(
                    "Buzz",
                    width="50%",
                    shadow="md",
                    on_click=State.open_buzz
                ),
                bg="white",
                padding="2em",
                shadow="md",
                border_radius="lg",
                width="100%",
                position="fixed",
            ),
            pc.cond(
                State.buzzed,
                pc.hstack(
                pc.input(
                    placeholder=State.answer_status,
                    width="50%",
                    shadow="md",
                    on_blur=State.set_user_answer,
                ),
                pc.button(
                    "Submit",
                    width="50%",
                    shadow="md",
                    on_click=[State.buzz_logic],
                ),
                ),

            ),
            pc.text(State.reader),
            pc.text(State.answer_line),
            width = "80%"
        ),
        width="100%",
        height="100vh",
        bg="radial-gradient(circle at 22% 11%,rgba(62, 180, 137,.20),hsla(0,0%,100%,0) 19%)",
    )


# Add state and page to the app.
app = pc.App(state=State)
app.add_page(index)
app.compile()
