import pynecone as pc


class State(pc.State):
    colors: list[str] = [
        "yellow",
        "yellow",
        "yellow",
        "yellow",
    ]

    questions: list[str] = [
        "Question 1",
        "Question 2",
        "Question 3",
        "Question 4",
        "Question 5",
    ] 
    qno=0

    optiona : list[str] = [
        "answer1a",
        "answer2a",
        "answer3a",
        "answer4a",
        "answer5a",
    ]
    opa=0

    optionb : list[str] = [
        "answer1b",
        "answer2b",
        "answer3b",
        "answer4b",
        "answer5b",
    ]
    opb=0

    optionc : list[str] = [
        "answer1c",
        "answer2c",
        "answer3c",
        "answer4c",
        "answer5c",
    ]
    opc=0

    optiond : list[str] = [
        "answer1d",
        "answer2d",
        "answer3d",
        "answer4d",
        "answer5d",
    ]
    opd=0

    colora : list[str] = [
        "red",
        "green",
        "red",
        "red",
        "red",
    ]
    clra=0

    colorb : list[str] = [
        "red",
        "red",
        "green",
        "red",
        "red",
    ]
    clrb=0

    colorc : list[str] = [
        "green",
        "red",
        "red",
        "red",
        "green",
    ]
    clrc=0

    colord : list[str] = [
        "red",
        "red",
        "red",
        "green",
        "red",
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
            on_click=State.increment,
        )
    )


app = pc.App(state=State)
app.add_page(index)
app.compile()