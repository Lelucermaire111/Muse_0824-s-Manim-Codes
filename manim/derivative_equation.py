from manimlib.imports import *

class Introduction(MovingCameraScene):
    CONFIG = {
        "stream_lines_config": {
            "delta_x": 1.0 / 8,
            "delta_y": 1.0 / 8,
            "y_min": -8.5,
            "y_max": 8.5,
        },
        "vector_field_config": {},
        "virtual_time": 3,
    }

    def construct(self):
        # Divergence
        def div_func(p):
            return p / 3
        div_vector_field = VectorField(
            div_func, **self.vector_field_config
        )
        stream_lines = StreamLines(
            div_func, **self.stream_lines_config
        )
        stream_lines.shuffle()
        div_title = self.get_title("Divergence")

        self.add(div_vector_field)
        self.play(
            LaggedStartMap(ShowPassingFlash, stream_lines),
            FadeIn(div_title[0]),
            *list(map(GrowFromCenter, div_title[1]))
        )

        # Curl
        def curl_func(p):
            return rotate_vector(p / 3, 90 * DEGREES)

        curl_vector_field = VectorField(
            curl_func, **self.vector_field_config
        )
        stream_lines = StreamLines(
            curl_func, **self.stream_lines_config
        )
        stream_lines.shuffle()
        curl_title = self.get_title("Curl")

        self.play(
            ReplacementTransform(div_vector_field, curl_vector_field),
            ReplacementTransform(
                div_title, curl_title,
                path_arc=90 * DEGREES
            ),
        )
        self.play(ShowPassingFlash(stream_lines, run_time=3))
        self.wait()

    def get_title(self, word):
        title = TextMobject(word)
        title.scale(2)
        title.to_edge(UP)
        title.add_background_rectangle()
        return title


def moveit_(point):
    x,y = point[:2]
    r1 = math.sqrt((x+4)**2+y**2)
    r2 = math.sqrt((x-4)**2+y**2)
    val_x = (x+4)/(r1**3)-(x-4)/(r2**3)
    val_y = y/(r1**3)-y/(r2**3)
    val = np.sqrt(val_x**2 + val_y**2)
    result = val_x/val*RIGHT + val_y/val*UP
    return 2 * result

class Try(Scene):
    CONFIG = {
        "stream_lines_config": {
            "start_points_generator_config": {
                "delta_x": 1.0 / 8,
                "delta_y": 1.0 / 8,
                "y_min": -8.5,
                "y_max": 8.5,
            }
        },
        "vector_field_config": {},
        "virtual_time": 3,
    }
    def construct(self):
        plane = NumberPlane(color = RED)
        plane.add(plane.get_axis_labels())
        #self.add(plane)
        vector_field = VectorField(
            moveit_,
            **self.vector_field_config
        )
        lines = StreamLines(
            moveit_,
            **self.stream_lines_config
        )

        self.add(vector_field)
        self.play(
            LaggedStartMap(ShowPassingFlash, lines)
        )

        ##for fun in func_draw:
        ##    self.play(ShowCreation(fun),run_time = 2)
        self.wait(5)

class BeginAnimation(Scene):
    def construct(self):

        plane = NumberPlane(color = RED)
        plane.add(plane.get_axis_labels())
        self.add(plane)

        points = [
            x * RIGHT + y * UP
            for x in np.arange(-8,8,1)
            for y in np.arange(-5,5,1)
        ]

        vec_field = []
        for point in points:
            de = point[0]+point[1]
            field = 0.8 * (np.sin(math.atan(de)) * UP + np.cos(math.atan(de)) * RIGHT)
            result = Vector(field).shift(point)
            vec_field.append(result)

        draw_field = VGroup(*vec_field).set_color(GREEN)
        self.play(ShowCreation(draw_field), run_time = 4)
        self.wait(2)

        Color = [RED, ORANGE, YELLOW, TEAL, BLUE, PURPLE]
        func = [
            ParametricFunction(
            lambda t:np.array([
                t,
                (-1-t) + x * np.exp(t),
                0
            ])
            ,t_min = -7, t_max  = 7).set_color(Color[(int(x / 2) + 6) % 6])
            for x in np.arange(-12,12,2)
        ]


        # lines = StreamLines(
        #     moveit_,
        #     virtual_time = 1,
        #     min_magnitude = 0,
        #     max_magnitude = 0
        # )
        # self.add_foreground_mobject(AnimatedStreamLines(
        #     lines,
        #     line_anim_class = ShowPassingFlash
        # ))

        func_draw = VGroup(*func)

        ##for fun in func_draw:
        ##    self.play(ShowCreation(fun),run_time = 2)

        self.play(ShowCreation(func_draw), run_time = 3)

        title = TextMobject("微分方程", color = RED).scale(1.2).shift(RIGHT * 4 + UP * 1)
        title_ = TextMobject("Differential Equation", color = RED).scale(1.2).next_to(title,DOWN)
        group = VGroup(title,title_)
        rec = SurroundingRectangle(group).set_color(BLACK)
        rec.set_fill(BLACK,opacity = 1)

        self.play(ShowCreation(rec))
        self.play(Write(title))
        self.play(DrawBorderThenFill(title_))

        self.wait(2)

class Part01(Scene):
    def construct(self):
        sen1 = TextMobject("方程是我们从小学开始就接触的一个概念",color = BLUE).scale(0.8).shift(DOWN * 3.5)
        sen2 = TextMobject("然后我们不断扩充着对方程的认识",color = BLUE).scale(0.8).shift(DOWN * 3.5)
        sen3 = TextMobject("当来到高等数学的范围时，微分方程便走进了我们的视野", color = BLUE).scale(0.8).shift(DOWN * 3.5)

        eq1 = TextMobject("$$2x = x + 1$$", color = RED).shift(UP * 3.5)
        eq2 = TextMobject("$$\\begin{cases} x = y + 1 \\\\ x = 2y - 3 \\end{cases}$$", color = RED).next_to(eq1,DOWN)
        eq3 = TextMobject("$$x^2 - 2x + 1 = 0$$",color = RED).next_to(eq2,DOWN)

        self.play(Write(sen1))
        self.play(Write(eq1))
        self.wait(2)
        self.play(Transform(sen1,sen2))
        self.play(Write(eq2))
        self.wait(2)
        self.play(Write(eq3))
        self.wait(2)

        self.play(Transform(sen1,sen3))

        eq4 = TextMobject("$$y''(x) -py'(x) + qy = f(x)$$",color = YELLOW)

        self.play(Write(eq4))
        self.wait(2)

        sen4 = TextMobject("方程是指含有未知数的等式，而微分方程中则含有导数",color = BLUE).scale(0.8).shift(DOWN * 3.5)
        sen5 = TextMobject("这意味着我们可以描述更复杂的变量关系",color = BLUE).scale(0.8).shift(DOWN * 3.5)
        sen6 = TextMobject("也意味着会有更多困难的、奇怪的方程TAT", color = BLUE).scale(0.8).shift(DOWN * 3.5)

        self.play(Transform(sen1, sen4))
        self.play(ApplyWave(eq4))

        self.wait(3)
        self.play(Transform(sen1, sen5))
        self.wait(2.5)
        self.play(Transform(sen1, sen6))

        eq5 = TextMobject("$$\\displaystyle\\frac{\\partial V}{\\partial t}+(V\\cdot \\nabla)V = f - \\frac{1}{\\rho}\\nabla p + \\frac{\\mu}{\\rho}\\nabla ^2V $$",color = GREEN)
        eq5.next_to(eq4,DOWN)

        self.play(DrawBorderThenFill(eq5),run_time = 2)

        sen7 = TextMobject("这是流体力学中著名的纳斯-斯托克斯方程",color = GREEN).scale(0.8).shift(DOWN * 3.5)
        sen8 = TextMobject("不要害怕，今天我们不会讨论如此复杂的方程",color = GREEN).scale(0.8).shift(DOWN * 3.5)
        sen9 = TextMobject("让我们从最简单的微分方程入手，以便对微分方程有一个轮廓式的认识",color = BLUE).scale(0.8).shift(DOWN * 3.5)

        self.wait(3)
        self.play(Transform(sen1,sen7))
        self.wait(2)
        self.play(Transform(sen1,sen8))
        self.wait(2)
        self.play(FadeOut(eq5))
        self.play(Transform(sen1,sen9))
        self.wait(2)

        eq_group = VGroup(eq1,eq2,eq3,eq4)
        eq6 = TextMobject("$$\\frac{dy}{dx}=2x$$",color= RED).scale(1.5).shift(UP*2)
        tip = TextMobject("$\\displaystyle\\frac{dy}{dx}$与$y'$代表的都是一阶导数",color = GREEN).next_to(eq6,DOWN)

        self.play(Transform(eq_group,eq6))
        self.wait(1)
        self.play(Write(tip))
        self.wait(3)

        self.play(FadeOut(tip))

        sen10 = TextMobject("这是一个简单的微分方程，描述的是$y$关于$x$的一阶导数",color = BLUE).scale(0.8).shift(DOWN*3.5)
        sen11 = TextMobject("我们直接知道每一点$y(x)$的斜率，那么我们能形成大概的数学图像",color = BLUE).scale(0.8).shift(DOWN*3.5)

        eq7 = TextMobject("$$x=1,y'=2;x=2,y'=4;x=3,y'=6\\cdots$$",color = GREEN).next_to(eq6,DOWN)

        self.play(Transform(sen1,sen10))
        self.wait(2)
        self.play(Transform(sen1,sen11))
        self.play(Write(eq7),run_time = 2)
        self.wait(3)

def moveit(point):
    x,y = point[:2]
    result = np.sin(math.atan(2*x)) * UP + np.cos(math.atan(2*x)) * RIGHT
    result = result * 2
    return result

class Part02(Scene):
    def construct(self):
        sen1 = TextMobject("用这样的小向量去代表每一点的斜率，我们可以得到这样一张图",color = BLUE).scale(0.8).shift(DOWN*3.5)

        plane = NumberPlane(color=RED)
        plane.add(plane.get_axis_labels())
        self.add(plane)

        self.play(Write(sen1),run_time = 2)
        self.wait(2)

        points = [
            x * RIGHT + y * UP
            for x in np.arange(-8, 8, 1)
            for y in np.arange(-3, 5, 1)
        ]

        vec_field = []
        for point in points:
            de = point[0] * 2
            field = 0.8 * (np.sin(math.atan(de)) * UP + np.cos(math.atan(de)) * RIGHT)
            result = Vector(field).shift(point)
            vec_field.append(result)

        draw_field = VGroup(*vec_field).set_color(GREEN)
        self.play(ShowCreation(draw_field), run_time=4)
        self.wait(3)

        sen2 = TextMobject("你可以称之为”向量场“，这是一个很有用的概念，我希望你能理解它",color = BLUE).scale(0.8).shift(DOWN * 3.5)
        sen3 = TextMobject("当然也可以画的更密集，这样可以更好地描述这个方程",color = BLUE).scale(0.8).shift(DOWN * 3.5)
        sen4 = TextMobject("WARNING！密恐警告！",color = RED).scale(0.8).shift(DOWN * 3.5)

        points_ = [
            x * RIGHT + y * UP
            for x in np.arange(-8, 8, 0.5)
            for y in np.arange(-3, 5, 0.5)
        ]

        vec_field_ = []
        for point in points_:
            de = point[0] * 2
            field = 0.5 * (np.sin(math.atan(de)) * UP + np.cos(math.atan(de)) * RIGHT)
            result = Vector(field).shift(point)
            vec_field_.append(result)

        draw_field_ = VGroup(*vec_field_).set_color(GREEN)
        self.wait(2)

        self.play(Transform(sen1,sen2))
        self.wait(3)
        self.play(Transform(sen1,sen3))
        self.wait(2)
        self.play(Transform(sen1,sen4))
        self.wait(1)
        self.play(ReplacementTransform(draw_field,draw_field_))
        self.wait(2)

        sen5 = TextMobject("然后我们顺着斜率就可以画出大致的函数图像", color = BLUE).scale(0.8).shift(DOWN * 3.5)
        sen6 = TextMobject("如果说之前的方程都是静态而确定的",color = BLUE).scale(0.8).shift(DOWN * 3.5)
        sen7 = TextMobject("由于导数的关系，微分方程是动态而变化的",color = BLUE).scale(0.8).shift(DOWN * 3.5)
        sen8 = TextMobject("因此我们可以画出很多条函数，需要额外的初始条件去确定是哪一条",color = BLUE).scale(0.8).shift(DOWN*3.5)

        Color = [RED, ORANGE, YELLOW, TEAL, BLUE, PURPLE]

        func = [
            ParametricFunction(
            lambda t:np.array([
                t,
                t**2 + x,
                0
            ])
            ,t_min = -7, t_max  = 7).set_color(Color[(x + 5) % 6])
            for x in np.arange(-5,5,1)
        ]

        func_draw = VGroup(*func)

        self.play(Transform(sen1,sen5))
        self.play(ShowCreation(func_draw[5]))
        self.wait(2)
        self.play(Transform(sen1,sen6))
        self.wait(3)
        self.play(Transform(sen1,sen7))
        self.wait(3)
        lines = StreamLines(
            moveit,
            virtual_time = 1,
            min_magnitude = 0,
            max_magnitude = 0
        )
        self.add_foreground_mobject(AnimatedStreamLines(
            lines,
            line_anim_class = ShowPassingFlash
        ))
        self.wait(3)
        self.play(Transform(sen1,sen8))
        for fun in func_draw:
            self.play(ShowCreation(fun),run_time = 2)
        self.wait(2)

        sen9 = TextMobject("如果你有一些微积分知识，你会很容易地求出这个方程的解",color = BLUE).scale(0.8).shift(DOWN*3.5)
        sen10 = TextMobject("$C$正是我们需要根据初始条件确定的常数",color = BLUE).scale(0.8).shift(DOWN*3.5)

        eq = TextMobject("$$y=x^2 + C$$",color = RED).shift(UP + RIGHT * 4.5).scale(1.5)

        self.play(Transform(sen1,sen9))
        self.wait(2)
        self.play(Write(eq))
        self.play(Transform(sen1,sen10))
        self.wait(3)

        sen11 = TextMobject("接下来让我们看一个更复杂一点的微分方程的可视化",color = BLUE).scale(0.8).shift(DOWN * 3.5)

        self.play(Transform(sen1,sen11))
        self.wait(3)


class Part03(Scene):
    def construct(self):
        eq = TextMobject("$$\\displaystyle\\frac{dy}{dx}=x+y$$", color=RED).shift(UP + RIGHT * 4).scale(1.5)
        plane = NumberPlane(color = RED)
        plane.add(plane.get_axis_labels())
        self.add(plane)

        self.play(Write(eq),run_time = 2)

        points = [
            x * RIGHT + y * UP
            for x in np.arange(-8,8,1)
            for y in np.arange(-3,5,1)
        ]

        vec_field = []
        for point in points:
            de = point[0]+point[1]
            field = 0.8 * (np.sin(math.atan(de)) * UP + np.cos(math.atan(de)) * RIGHT)
            result = Vector(field).shift(point)
            vec_field.append(result)

        draw_field = VGroup(*vec_field).set_color(GREEN)
        self.play(ShowCreation(draw_field), run_time = 4)
        self.wait(2)

        Color = [RED, ORANGE, YELLOW, TEAL, BLUE, PURPLE]
        func = [
            ParametricFunction(
            lambda t:np.array([
                t,
                (-1-t) + x * np.exp(t),
                0
            ])
            ,t_min = -7, t_max  = 7).set_color(Color[(int(x / 2) + 6) % 6])
            for x in np.arange(-12,12,2)
        ]


        lines = StreamLines(
            moveit_,
            virtual_time = 1,
            min_magnitude = 0,
            max_magnitude = 0
        )
        self.add_foreground_mobject(AnimatedStreamLines(
            lines,
            line_anim_class = ShowPassingFlash
        ))

        func_draw = VGroup(*func)

        self.play(ShowCreation(func_draw), run_time = 5)

        sen1 = TextMobject("这个方程的解稍微复杂一些", color = BLUE).scale(0.8).shift(DOWN*3.5)
        sen2 = TextMobject("而且需要用到","常数变易法，但这并不是今天的重点",color = BLUE).scale(0.8).shift(DOWN*3.5)

        eq1 = TextMobject("$$y=-1-x+Ce^{x}$$", color=RED).shift(UP + RIGHT * 4).scale(1.5)

        self.play(Write(sen1))
        self.wait(2)
        self.play(Transform(eq,eq1))
        self.play(Transform(sen1,sen2))
        self.wait(3)

        sen3 = TextMobject("希望你能通过这种方式初步理解微分方程",color = BLUE).scale(0.8).shift(DOWN*3.5)
        self.play(Transform(sen1,sen3))
        self.wait(3)

class Part04(Scene):
    CONFIG = {
        'phase':'phase.png'
    }
    def construct(self):
        phase = ImageMobject(self.phase).set_height(5)
        sen1 = TextMobject("很遗憾，并不是所有微分方程都可以顺利地这样描述",color = BLUE).scale(0.8).shift(DOWN*3.5)
        sen2 = TextMobject("比如更重要的二阶常微分方程，不过不要担心",color = BLUE).scale(0.8).shift(DOWN*3.5)
        eq = TextMobject("$$y''(x) -py'(x) + qy = f(x)$$", color=YELLOW).shift(UP*3.5)
        sen3 = TextMobject("同样有描述二阶常微分方程的方式，比如自动控制关注系统的相平面",color = BLUE).scale(0.8).shift(DOWN*3.5)
        sen4 = TextMobject("这就留到以后再讲啦！希望你看得开心！感谢观看！",color = BLUE).scale(0.8).shift(DOWN*3.5)

        self.play(Write(sen1))
        self.wait(2)
        self.play(Transform(sen1,sen2))
        self.play(Write(eq))
        self.wait(2)
        self.play(Transform(sen1,sen3))
        self.play(FadeIn(phase))
        self.wait(3)
        self.play(Transform(sen1,sen4))
        self.wait(3)