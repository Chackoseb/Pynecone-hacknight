import pynecone as pc
import time


class State(pc.State):
    colors: list[str] = [
        "yellow",
        "yellow",
        "yellow",
        "yellow",
        "yellow",
    ]

    questions: list[str] = [
        "Who is father of computers?",
        "Which of the following computer language is written in binary codes only?",
        "Which of the following can access the server?",
        "Which of the following is the first neural network computer?",
        "Which of the following is a technique that marked the beginning of computer communications?",
        "Thankyou For Participating",
    ] 
    qno=0

    optiona : list[str] = [
        "James Gosling",
        "Machine language",
        "User",
        "AN",
        "User Environment",
        ".          Have            .",
    ]
    opa=0

    optionb : list[str] = [
        "Dennis Ritchie",
        "pascal",
        "Web Client",
        "AM",
        "Batch Environment",
        ".           a               .",
    ]
    opb=0

    optionc : list[str] = [
        "Charles Babbage",
        "C",
        "Web Browser",
        "RFD",
        "Time Sharing",
        ".         Nice              ."
    ]
    opc=0

    optiond : list[str] = [
        "Bjarne Stroustrup",
        "C#",
        "Web Server",
        "SNARC",
        "Message passing",
        ".          Day              ."
    ]
    opd=0

    colora : list[str] = [
        "red",
        "green",
        "red",
        "red",
        "red",
        "blue"
    ]
    clra=0

    colorb : list[str] = [
        "red",
        "red",
        "green",
        "red",
        "red",
        "blue"
    ]
    clrb=0

    colorc : list[str] = [
        "green",
        "red",
        "red",
        "red",
        "green",
        "blue"
    ]
    clrc=0

    colord : list[str] = [
        "red",
        "red",
        "red",
        "green",
        "red",
        "blue",
    ]
    clrd=0

    def increment(self):
        self.qno += 1
        self.opa += 1
        self.opb += 1
        self.opc += 1
        self.opd += 1
        self.clra += 1
        self.clrb += 1
        self.clrc += 1
        self.clrd += 1
        if(self.qno==6):
            pc.text("Quiz Over")
            self.qno = 0
            self.opa = 0
            self.opb = 0
            self.opc = 0
            self.opd = 0
            self.clra = 0
            self.clrb = 0
            self.clrc = 0
            self.clrd = 0
        
    def change_color(self, color, index):
        self.colors[index] = color


def index():
    
    return pc.vstack(
        pc.text(State.questions[State.qno]
        ),
        pc.vstack(
            pc.button (
                State.optiona[State.opa],
                default_value="yellow",
                on_click= State.change_color(State.colora[State.clra], 0),
                bg=State.colors[0],
            ),
            pc.button(
                State.optionb[State.opb],
                default_value="yellow",
                on_click= State.change_color(State.colorb[State.clrb], 1),
                bg=State.colors[1],
            ),
            pc.button(
                State.optionc[State.opc],
                default_value=State.colors[2],
                on_click= State.change_color(State.colorc[State.clrc], 2),
                bg=State.colors[2],
            ),
            pc.button(
                State.optiond[State.opd],
                default_value=State.colors[3],
                on_click= State.change_color(State.colord[State.clrd], 3),
                bg=State.colors[3],
            ),

            
        ),
        pc.button(
                "NEXT",
                border_radius="1em",
                box_shadow="rgba(151, 65, 252, 0.8) 0 15px 30px -10px",
                background_image="linear-gradient(144deg,#AF40FF,#5B42F3 50%,#00DDEB)",
                box_sizing="border-box",
                color="white",
                _hover={
                    "opacity": 0.85,
                },
                on_click=[
                    State.increment,
                    State.change_color("yellow",0),
                    State.change_color("yellow",1),
                    State.change_color("yellow",2),
                    State.change_color("yellow",3)
                ]    
            )
        
    )


app = pc.App(state=State)
app.add_page(index)
app.compile()