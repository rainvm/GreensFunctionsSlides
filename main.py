# manim
from manim import *
from manim_editor import PresentationSectionType
# math
from sympy import *
import numpy as np

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
<<<<<<< Updated upstream
            axis_config={'font_size': 18, "stroke_color": BLACK}
        )
        axes.set_y(-1)
=======
            axis_config={'font_size': 18, 'color': BLACK, },
        )
        axes.set_y(-1)
        axes.color = BLACK
>>>>>>> Stashed changes
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
<<<<<<< Updated upstream
        hole = Circle(0.0001, fill_opacity=1, fill_color=WHITE,)
=======
        vert = axes.plot_implicit_curve(lambda x, y: x - 1, color=BLACK)
        vert.y_range = {0, 2}
        hole = Circle(0.0001, fill_opacity=1, fill_color=WHITE, )
>>>>>>> Stashed changes
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
<<<<<<< Updated upstream
        self.next_section(type=PresentationSectionType.NORMAL)
        self.play(Create(limfRight), Create(limfLeft), Create(rightLimitDot), Create(leftLimitDot))
        self.wait()
        self.play(MoveAlongPath(rightLimitDot, limfRight), rate_func=linear)
=======


class Derivative(Scene):
    def construct(self):
        self.next_section(type=PresentationSectionType.NORMAL)
        # defs
        h = Symbol('a')
        tracker = ValueTracker(0)
        x = Symbol('x')
        y = x ** 3 - 9 * x ** 2 + 25 * x - 19
        Dy = y.diff(x)
        f = lambdify(x, y, 'numpy')
        Df = lambdify(x, Dy, 'numpy')
        tanLine = lambdify([x, h], Df(h) * (x - h) + f(h), 'numpy')
        inv_f = lambdify([x, h], (x - f(h)) / Df(h) + h, 'numpy')

        # axes = Axes(
        #     tips=False,
        #     x_range=[0, 5, 1],
        #     y_range=[-2, 4, 1],
        #     x_length=4,
        #     y_length=4,
        #     axis_config={'font_size': 18, 'color': BLACK},
        # )

        axes = NumberPlane(x_range=[0, 6, 1], x_length=5, y_range=[-2, 4, 1], y_length=5).add_coordinates().shift(
            LEFT * 3.5)
        function = axes.plot(
            lambda t: f(t),
            color=PURPLE_C,
            x_range=[1, 4.8]
        )
        axes.x_axis.set_color(BLACK)
        axes.y_axis.set_color(BLACK)

        # tanPlot = axes.plot(
        #     lambda x: tanLine(x, tracker.get_value()),
        #     color=RED_E,
        #     x_range=[x_min, x_max]
        # )

        tanPlot = always_redraw(
            lambda: axes.plot(lambda x: tanLine(x, tracker.get_value()),
                              color=GREEN_E,
                              x_range=[0 if inv_f(-2, tracker.get_value()) < 0 else inv_f(-2, tracker.get_value()),
                                       6 if inv_f(4, tracker.get_value()) > 6 else inv_f(4, tracker.get_value())])
        )

        maxLabel = always_redraw(lambda: Text("%f" % (0 if inv_f(-2, tracker.get_value()) < 0 else inv_f(-2, tracker.get_value())), color=BLACK))

        self.add(axes, tracker, maxLabel)
        self.play(Create(function), Create(tanPlot))
        tracker.add_updater(lambda mobject, dt: mobject.increment_value(dt))
        self.wait(4)
>>>>>>> Stashed changes
