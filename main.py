from manim import *

from manim_editor import  PresentationSectionType

config["background_color"] = WHITE

class Title(Scene):
    def construct(self):
        self.next_section(type=PresentationSectionType.NORMAL)
        pos = 2
        dist = 1
        dot = Dot(color=WHITE)
        self.play(Create(dot))
        title = Text("The Method of Green's Functions", font_size=36, should_center=True, color='#38248a',
                     font="Tenorite")
        title.set_y(pos)
        byline = Text("Ryan Coyne", font_size=20, should_center=False, color=BLACK, font="Tenorite")
        byline.set_y(pos - dist)
        byline.set_x(0)
        inst = Text("NHTI - Concord's Community College", font_size=20, should_center=False, color=BLACK,
                    font="Tenorite")
        inst.set_y(pos - 2 * dist)
        inst.set_x(0)
        date = Text("5/5/2023", font_size=20, should_center=False, color=BLACK, font="Tenorite")
        date.set_x(0)
        date.set_y(pos - 3 * dist)
        self.add(byline, title, inst, date)
        self.wait()


class Limit(Scene):
    def construct(self):
        self.next_section(type=PresentationSectionType.NORMAL)
        title = Text("Limits", color = BLACK)
        title.set_y(3.5)
        title.set_x(-4)
        axes = Axes(
            tips=False,
            x_range=[0, 2, 0.5],
            y_range=[0, 3, 0.5],
            x_length=4,
            y_length=4,
            axis_config={'font_size': 18, "stroke_color": BLACK}
        )
        axes.set_y(-1)
        axes.add_coordinates({0, 0.5, 1, 1.5, 2}, {0, 0.5, 1, 1.5, 2, 2.5, 3})
        axes.x_axis.numbers.color = BLACK
        axes.y_axis.numbers.color = BLACK
        limf = axes.plot(
            lambda t: t + 1,
            color=BLACK,
            x_range=[0, 2]
        )
        limfRight = axes.plot(
            lambda t: t + 1,
            color=BLACK,
            x_range=[1,0],
        )
        limfLeft = axes.plot(
            lambda t: t + 1,
            color=BLACK,
            x_range=[0, 1]
        )
        limitFunctionText = MathTex(r"f(x)=\frac{x^2-1}{x-1}", color=BLACK, font_size=24)
        limitFunctionText.set_x(-3.5)
        limitFunctionText.set_y(2.5)
        hole = Circle(0.0001, fill_opacity=1, fill_color=WHITE,)
        holePos = axes.coords_to_point(1, 2)
        hole.set_x(holePos[0])
        hole.set_y(holePos[1])
        rightLimitDot = Dot().set_color(RED_E)
        leftLimitDot = Dot().set_color(RED_E)
        self.add(limitFunctionText, title)
        self.play(Create(axes))
        self.play(Create(limf))
        self.next_section(type=PresentationSectionType.NORMAL)
        self.add(hole)
        self.play(hole.animate.scale(500))
        self.next_section(type=PresentationSectionType.NORMAL)
        self.play(Create(limfRight), Create(limfLeft), Create(rightLimitDot), Create(leftLimitDot))
        self.wait()
        self.play(MoveAlongPath(rightLimitDot, limfRight), rate_func=linear)
