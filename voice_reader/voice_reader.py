"""Welcome to Pynecone! This file outlines the steps to create a basic app."""
from pcconfig import config
import qbreader 
import pynecone as pc
import asyncio

docs_url = "https://pynecone.io/docs/getting-started/introduction"
filename = f"{config.app_name}/{config.app_name}.py"

coins = ["tossup", "bonus"]

packets = ['', '2023 Black History Month Packet', '2023 ACF Regionals', '2022 Winter Closed', '2022 WORKSHOP', '2022 UGGHH', '2022 The Last 1022 Years Were Boring Anyway', '2022 STANIEL', '2022 SCOP MS 11', '2022 Reinstein', '2022 Random Music Packet', '2022 QUARTET', '2022 Penn Bowl', '2022 PACE NSC', '2022 NIPPON', '2022 NASAT', '2022 Medieval Literature Packet', '2022 MUSES III', '2022 MSQB Madness II', '2022 MRNA VACCINE', '2022 Logomachy', '2022 Eminent Victorians', '2022 DECAF', '2022 Chicago Open', '2022 COHORT', '2022 COAST', '2022 Boilermaker Spring Novice', "2022 Alex's Science Packet", '2022 ARCADIA', '2022 ACF Winter', '2022 ACF Regionals', '2022 ACF Nationals', '2022 ACF Fall', '2022 20th-21st Century Literature Packet', '2021 WORKSHOP', "2021 Vedul's Short Poetry Packet", '2021 The World As It Is', '2021 The Geography Front', '2021 TSALT', '2021 TELEOLOGY', '2021 Spring Novice', "2021 Shiva's Tiny Science Tossups", '2021 Semi-Serious Charity Tournament', '2021 Scattergories', '2021 SOS', '2021 SMH', '2021 SKUFFED', '2021 SCOP B', '2021 Remember the Women', '2021 Penn Bowl', '2021 PACE NSC', '2021 NEWT', '2021 NASAT', '2021 MUSES II', '2021 MSQB Madness', '2021 LHASA', '2021 KEYSET', '2021 JORDU', '2021 Illinois Open', '2021 Halloween Contemporary Poetry Packet', '2021 HARI', '2021 Glasgow Scottie', "2021 Geoffrey Wu's NFL Packet", '2021 GORKY III', '2021 GORKY II', '2021 FINE AARTS', "2021 Dan and Coby and Tiffany's Math Set", '2021 DUOS', '2021 DART II', '2021 DART I', '2021 Chicago Open', '2021 COOT', '2021 CERES', '2021 CALISTO 2', '2021 Bentley Contemporary Literature Packet', '2021 BHSAT', '2021 ARCADIA', '2021 AQBL February Set', '2021 ACF Winter', '2021 ACF Regionals', '2021 ACF Nationals Qualifier', '2021 ACF Nationals', '2021 ACF Fall', '2020-2021 Matt Cvijanovich Memorial Tournament', '2020 WORKSHOP', '2020 Vanity John Milton Packet', '2020 Terrapin', '2020 TAPIR', '2020 TAILS', '2020 Spring Undergraduate Novice', '2020 Scattergories', '2020 Saturnalia', '2020 STASH', '2020 SCOP MS 10', '2020 SCOP A', '2020 SCALE', '2020 RAFT II', '2020 Prison Bowl', '2020 Oxford Open', '2020 Michigan Winter Tournament', '2020 MOQBA Novice', '2020 Longhorn Invitational Tournament', '2020 LONE STAR', '2020 IKEA', '2020 Hit or Myth', '2020 HC History', '2020 Glasgow Scottie', '2020 GORKY', '2020 FRENCH II', '2020 FLopen', '2020 ERIS', '2020 Delta Burke', '2020 DITCH', '2020 DECAMERON', '2020 CALISTO', '2020 BHSAT', '2020 ART NOUVEAU', '2020 AQBL October Set', '2020 ACF Winter', '2020 ACF Regionals', '2020 ACF Fall', '2019 WAIT', '2019 The Unanswered Question', '2019 Terrapin', '2019 Spartan Housewrite', '2019 ScotBowl', '2019 Scattergories', '2019 SCOP Novice 10', '2019 Reel Knowledge', '2019 RULFO', '2019 RMBAT', '2019 RAFT', '2019 Prison Bowl', '2019 Penn Bowl', '2019 PIANO', '2019 PACE NSC', '2019 Oxford Open', '2019 NASAT', '2019 MUSES', '2019 MKVLTRA', '2019 META', '2019 Lederberg', '2019 LOGIC', '2019 ILLIAC', '2019 HFT', '2019 Guerrilla History', '2019 Glasgow Scottie', '2019 Florida Spring Tournament (FST)', '2019 Fall Open', '2019 FONS', '2019 Early Fall Tournament (EFT)', '2019 Delta Burke', '2019 Chicago Open', '2019 Canadian Hybrid', '2019 CAST', '2019 BLAST', '2019 BHSAT', '2019 Age of Empires', '2019 ATHENA II', '2019 ACF Regionals', '2019 ACF Nationals', '2019 ACF Fall', '2018 Words and Objects', '2018 WORLDSTAR', '2018 WHAQ', '2018 Sun God Invitational', '2018 Stevenson Memorial Tournament (SMT)', '2018 Scattergories', '2018 SCOP Novice 9', '2018 RAPTURE', '2018 Prison Bowl', '2018 Penn Bowl', '2018 PACE NSC', '2018 Oxford Open', '2018 OCTAVIAN', '2018 NASAT', '2018 MVS RAMS', '2018 MKULTR4', '2018 MBAT', '2018 MALA', '2018 IMSAnity', '2018 Human Use of Human Beings', '2018 Historature', '2018 HFT', '2018 Glasgow Scottie', '2018 Geography Monstrosity', '2018 GLRAC', '2018 GHOTI', '2018 Florida Spring Tournament (FST)', '2018 FONS', '2018 FACTS', '2018 Early Fall Tournament (EFT)', '2018 Delta Burke', '2018 Chicago Open', '2018 Cambridge Open', '2018 CMST', '2018 BHSAT', '2018 ACF Regionals', '2018 ACF Nationals', '2018 ACF Fall', '2017 XENOPHON', '2017 WHAQ', '2017 WAO', '2017 Thought Monstrosity', '2017 Scattergories', '2017 SUN', '2017 SCOP Novice 8', '2017 SCOP MS 7', '2017 RMBCT', '2017 Prison Bowl', '2017 Penn Bowl', '2017 PSACA', '2017 POMMSS', '2017 PACE NSC', '2017 NASAT', '2017 Maryland Fall', '2017 MKULTRA 3', '2017 MASSOLIT', '2017 Letras', '2017 LIST VI', '2017 Jakob', "2017 It's Lit", '2017 HIGS', '2017 HFT', '2017 Geography Monstrosity', '2017 GSAC', '2017 GEODUCK', '2017 FRENCH', '2017 FONS', '2017 Eisenhower Memorial Tournament (EMT)', '2017 Early Fall Tournament (EFT)', '2017 Delta Burke', '2017 Darien DEFT', '2017 Chicago Open', '2017 BHSAT', '2017 ACF Regionals', '2017 ACF Nationals', '2017 ACF Fall', '2017 (This) Tournament is a Crime', '2016 WHAQ', '2016 Terrapin', '2016 SAGES II', '2016 Prison Bowl', '2016 Pennsylvania Novice', '2016 Penn Bowl', '2016 PLATO', '2016 PACE NSC', '2016 Oxford Open', '2016 NASAT', '2016 Minnesota Undergraduate Tournament (MUT)', '2016 MYSTERIUM', '2016 MLK', '2016 Listory', '2016 HFT', '2016 Geography Monstrosity', '2016 FONS', '2016 Early Fall Tournament (EFT)', '2016 Delta Burke', '2016 Chicago Open', '2016 CLEAR II', '2016 BHSAT', '2016 ARTSEE', '2016 ACF Regionals', '2016 ACF Nationals', '2016 ACF Fall', '2015 VTACO', '2015 VICO', '2015 VCU Open', '2015 STIMPY', '2015 SHEIKH', '2015 SAGES', '2015 Prison Bowl', '2015 Penn Bowl', '2015 PACE NSC', '2015 Oxford Open', '2015 NASAT', '2015 Missouri Open', '2015 Minnesota Undergraduate Tournament (MUT)', '2015 Maryland Fall', '2015 MKULTRA', '2015 HFT', '2015 HERMES', '2015 George Oppen', '2015 GSAC', '2015 Delta Burke', '2015 Chicago Open', '2015 BISB', '2015 BHSAT', '2015 BASK', '2015 ACF Regionals', '2015 ACF Nationals', '2015 ACF Fall', '2014 VCU Open', '2014 SUBMIT', '2014 Prison Bowl', '2014 Penn Bowl', '2014 PADAWAN', '2014 PACE NSC', '2014 Oxford Open', '2014 NASAT', '2014 Minnesota Undergraduate Tournament (MUT)', '2014 Maryland Spring', '2014 MGMT', '2014 Lederberg', '2014 LIST IV', '2014 Introductory Collaborative Collegiate Set', '2014 HFT', '2014 GSAC', '2014 Delta Burke', '2014 DEES', '2014 Chicago Open', '2014 Cane Ridge Revival', '2014 CLEAR', '2014 BISB', '2014 BHSAT', '2014 BELLOCO', '2014 ACF Regionals', '2014 ACF Nationals', '2014 ACF Fall', '2013 Western Invitational Tournament', '2013 VCU Open', '2013 VCU Closed', '2013 Terrapin', '2013 SASS', '2013 Prison Bowl', '2013 Penn Bowl', '2013 PACE NSC', '2013 NASAT', '2013 Minnesota Undergraduate Tournament (MUT)', '2013 Michigan Fall Tournament', '2013 LIST', '2013 JAMES', '2013 GSAC', '2013 Fall Kickoff Tournament (FKT)', '2013 Delta Burke', '2013 DRAGOON', '2013 Collegiate Novice', '2013 Collaborative Middle School Tournament #4', '2013 Chicago Open', '2013 BISB', '2013 BHSAT', '2013 ACF Regionals', '2013 ACF Nationals', '2013 ACF Fall', '2012 YMIR', '2012 WELD', '2012 RAVE', '2012 QUARK', '2012 Prison Bowl', '2012 Penn-ance', '2012 Penn Bowl', '2012 PACE NSC', '2012 Oxford Open', '2012 NASAT', '2012 Minnesota Undergraduate Tournament (MUT)', '2012 Minnesota Open', '2012 Michigan KABO', '2012 LIST', '2012 Illinois Fall Tournament', '2012 GSAC', '2012 Fall Kickoff Tournament (FKT)', '2012 Delta Burke', '2012 Collegiate Novice', '2012 Collaborative Middle School Tournament #3', '2012 Chicago Open', '2012 BHSAT', '2012 BDAT', '2012 BARGE', '2012 ACF Regionals', '2012 ACF Nationals', '2012 ACF Fall', '2011 SACK', '2011 Prison Bowl', '2011 Penn Bowl', '2011 PACE NSC', '2011 OLEFIN', '2011 NASAT', '2011 Minnesota Undergraduate Tournament (MUT)', '2011 Minnesota Open', '2011 MAGNI', '2011 LIST', '2011 Illinois Open', '2011 GSAC', '2011 Fall Kickoff Tournament (FKT)', '2011 Delta Burke', '2011 Collegiate Novice', '2011 Collaborative Middle School Tournament #2', '2011 Chicago Open', '2011 BDAT', '2011 ACF Regionals', '2011 ACF Nationals', '2011 ACF Fall', '2010 Prison Bowl', '2010 Penn Bowl', '2010 PACE NSC', '2010 NASAT', '2010 NAREN', '2010 Minnesota Undergraduate Tournament (MUT)', '2010 Minnesota Open', '2010 MELD', '2010 Fall Novice Tournament', '2010 Fall Kickoff Tournament (FKT)', '2010 Early Fall Tournament (EFT)', '2010 Delta Burke', '2010 Collegiate Novice', '2010 Collaborative Middle School Tournament', '2010 Chicago Open', '2010 Ben Cooper', '2010 BATE', '2010 ANGST', '2010 ACF Winter', '2010 ACF Regionals', '2010 ACF Nationals', '2010 ACF Fall', '2009 Prison Bowl', '2009 PACE NSC', '2009 Minnesota Undergraduate Tournament (MUT)', '2009 Minnesota Open', '2009 Lederberg', '2009 Fall Novice Tournament', '2009 Fall Kickoff Tournament (FKT)', '2009 Early Fall Tournament (EFT)', '2009 ACF Winter', '2009 ACF Nationals', '2009 ACF Fall', '2008 Prison Bowl', '2008 PACE NSC', '2008 Minnesota Undergraduate Tournament (MUT)', '2008 Minnesota Open', '2008 FEUERBACH', '2008 Early Fall Tournament (EFT)', '2008 ACF Nationals', '2008 ACF Fall', '2007 PACE NSC', '2007 Early Fall Tournament (EFT)', '2007 ACF Nationals', '2007 ACF Fall', '2006 PACE NSC', '2006 Early Fall Tournament (EFT)', '2006 ACF Nationals', '2006 ACF Fall', '2005 PACE NSC', '2005 ACF Nationals', '2005 ACF Fall', '2004 PACE NSC', '2004 ACF Fall', '2003 PACE NSC', '2003 ACF Fall', '2002 PACE NSC', '2000 PACE NSC']
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

    async def question_reader(self):
        pass

    def question_logic(self):
        str_list = self.difficulty_str.split("-")
        self.difficulty = list(range(int(str_list[0]), int(str_list[1])+1))
        print(self.difficulty)
        if self.packet.strip() != "":
                self.packet_questions = qbreader.packet(setName=self.packet, packetNumber=self.packet_num)
        else:
            self.question = qbreader.random_question(questionType=self.question_type, difficulties=self.difficulty)


    



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
            bg="white",
            padding="2em",
            shadow="md",
            border_radius="lg",
            width="50%",
        ),
        width="100%",
        height="100vh",
        bg="radial-gradient(circle at 22% 11%,rgba(62, 180, 137,.20),hsla(0,0%,100%,0) 19%)",
    )


# Add state and page to the app.
app = pc.App(state=State)
app.add_page(index)
app.compile()
