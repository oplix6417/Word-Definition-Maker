from manim import *

class WordDefinitionScene(Scene):
    def create_definition(self, word: str, phonetic: str, definition: str):
        # Create background rectangle with a black background
        background = Rectangle(
            width=14,
            height=8,
            fill_color=BLACK,
            fill_opacity=1,
            stroke_color=WHITE,
            stroke_width=2
        )
        self.add(background)

        # Create the word text and position it at the upper-left corner
        title = Text(word, color=WHITE)
        title.scale(2)
        title.to_corner(UL, buff=0.5)

        # Create the phonetic pronunciation and align it to the left of the title
        phonetic_text = Text(phonetic, color=WHITE, slant=ITALIC)
        phonetic_text.next_to(title, DOWN, buff=0.5)
        phonetic_text.align_to(title, LEFT)

        # Create a horizontal line below the phonetic text
        line = Line(
            start=LEFT * 4,
            end=RIGHT * 4,
            color=WHITE
        )
        line.next_to(phonetic_text, DOWN, buff=0.5)
        line.align_to(title, LEFT)

        # Create the definition text and align it to the left
        definition_text = Text(definition, color=WHITE)
        definition_text.scale(0.8)
        definition_text.next_to(line, DOWN, buff=0.5)
        definition_text.align_to(title, LEFT)

        # Animation sequence
        self.play(Write(title), run_time=1)
        self.play(Write(phonetic_text), run_time=1)
        self.play(Create(line), run_time=0.5)
        self.play(Write(definition_text), run_time=2)
        self.wait(2)

    def construct(self):
        # Example usage of create_definition method
        self.create_definition(
            word="time",
            phonetic="[time] noun",
            definition="a finite resource that we all wish we had more of"
        )

if __name__ == "__main__":
    with tempconfig({"quality": "medium_quality", "preview": True}):
        scene = WordDefinitionScene()
        scene.render()
