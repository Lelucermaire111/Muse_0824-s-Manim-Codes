from manimlib.imports import *

def moveit(point):
    x,y = point[:2]
    result = RIGHT*np.cos(y)+UP*np.cos(x)
    result = result * 2
    return result

def moveit_(point):
    x,y = point[:2]
    result = RIGHT*x+UP*(x+y)
    return result

class BeginAnimation(Scene):
    def construct(self):
        plane = NumberPlane(color = RED)
        plane.add(plane.get_axis_labels())
        self.add(plane)
        points_ = [
            x * RIGHT + y * UP
            for x in np.arange(-8, 8, 0.5)
            for y in np.arange(-3, 5, 0.5)
        ]
        vec_field_ = []
        for point in points_:
            # theta = np.arctan((point[0]+point[1])/point[0])
            # field = 0.5 * (- np.cos(theta) * RIGHT - np.sin(theta) * UP)
            field = 0.4 * ( - point[0] * RIGHT - (point[0] + point[1]) * UP)
            result = Vector(field).shift(point)
            vec_field_.append(result)

        draw_field_ = VGroup(*vec_field_).set_color(BLUE)
        self.wait(1)
        self.play(ShowCreation(draw_field_),run_time = 3)
        self.wait(2)
        # lines = StreamLines(
        #     moveit_
        # )
        # self.add_foreground_mobject(AnimatedStreamLines(
        #     lines,
        #     line_anim_class=ShowPassingFlash
        # ))
        title = TextMobject("混   沌",color = RED).scale(3).shift(UP)
        title_eng = TextMobject("Chaos", color = RED).scale(3).shift(DOWN)
        self.wait(2)
        # self.play(Write(title))
        # self.play(Write(title_eng))
        # self.wait(5)

class Part01(Scene):
    def construct(self):
        sen1 = TextMobject("确定的系统一定会有确定的结果吗？",color = BLUE).shift(UP)
        sen2 = TextMobject("为什么我们的天气预报只在短期内是有效的？", color = BLUE)
        sen3 = TextMobject("蝴蝶效应又是怎么一回事儿？", color = BLUE).shift(DOWN)
        sen4 = TextMobject("我相信在看完这期视频后会对你有一些启发！")
        group = VGroup(sen1,sen2,sen3)
        self.play(Write(sen1))
        self.wait(2)
        self.play(Write(sen2))
        self.wait(2)
        self.play(Write(sen3))
        self.wait(2)
        self.play(Transform(group,sen4))
        self.wait(3)

class Part02(Scene):
    def construct(self):
        sen1 = TextMobject("首先让我们来看一个这样的系统").scale(0.8).shift(DOWN*3.5)
        eq1 = TextMobject("$x_n = $","$\\mu x_{n-1}$","$- \\mu x ^2 _{n-1}$", color = BLUE).shift(UP*3)
        eq2 = TextMobject("$$x_n \\in [0,1] \\quad \\mu \\in [0,4]$$",color = RED).next_to(eq1,DOWN)

        sen2 = TextMobject("你可以将它理解为一个种群的数量变化模型").scale(0.8).shift(DOWN*3.5)
        sen3 = TextMobject("同时有限制条件").scale(0.8).shift(DOWN*3.5)
        sen4 = TextMobject("你可以将$x_n$理解为被归一化了").scale(0.8).shift(DOWN*3.5)
        sen5 = TextMobject("比如最大种群数量是1000，也就是1；那么0.5代表的也就是500").scale(0.8).shift(DOWN*3.5)
        sen6 = TextMobject("$\\mu$代表的是环境的影响，适于繁殖或者生存危机").scale(0.8).shift(DOWN*3.5)

        sen7 = TextMobject("所以第一项驱动着种群增长，","第二项由于竞争使得种群数量减少").scale(0.8).shift(DOWN*3.5)

        sen8 = TextMobject("只要我们给出$\\mu$以及初值$x_0$系统就可以演化下去").scale(0.8).shift(DOWN*3.5)
        sen9 = TextMobject("由于这是一个迭代模型，我们无法一眼看出其变化规律").scale(0.8).shift(DOWN*3.5)
        sen10 = TextMobject("所以不妨让我们给出几组初值去模拟系统").scale(0.8).shift(DOWN*3.5)

        eq3 = TextMobject("$x_1 = \\mu (x_0 -x_0^2) \\quad x_2 = \\mu (x_1 -x_1^2) \\quad ...$", color = BLUE).scale(0.8).next_to(eq2,DOWN)

        self.play(Write(sen1))
        self.wait(2)
        self.play(Write(eq1))
        self.wait(2)
        self.play(Transform(sen1,sen2))
        self.wait(3)
        self.play(Transform(sen1,sen3))
        self.wait(1)
        self.play(Write(eq2))
        self.wait(2)
        self.play(Transform(sen1,sen4))
        self.wait(3)
        self.play(Transform(sen1,sen5))
        self.wait(3)
        self.play(Transform(sen1,sen6))
        self.wait(2.5)
        self.play(FadeOut(sen1))
        self.play(Write(sen7[0]),ApplyWave(eq1[1]))
        self.wait(2)
        self.play(Write(sen7[1]),ApplyWave(eq1[2]))
        self.wait(2)
        self.play(Transform(sen7,sen8))
        self.play(Write(eq3))
        self.wait(3)
        self.play(Transform(sen7,sen9))
        self.wait(3)
        self.play(Transform(sen7,sen10))
        self.wait(3)

class Part03_1(GraphScene):
    CONFIG = {
        "x_min": 0,
        "x_max": 100,
        "x_tick_frequency": 10,
        "x_axis_label": "$n$",
        "y_axis_label": "$x_n$",
        "y_min": 0,
        "y_max": 1,
        "exclude_zero_label": False,
        "y_axis_height": 5,
        "x_axis_width": 12,
        "graph_origin": DOWN * 2.5 + LEFT * 6
    }
    def construct(self):
        self.setup_axes()
        mu = 0.5
        func = []
        title = TextMobject("$$x_0=0.9 \\qquad \\mu = 0.5$$",color = RED).shift(DOWN*3.5)
        self.play(Write(title))
        func.append(0.9)
        for i in range(1,100):
            val_y = mu*(func[i-1]-func[i-1]**2)
            func.append(val_y)
        for i,dat in enumerate(func):
            dot = Dot(radius = 0.05).move_to(self.coords_to_point(i,dat)).set_color(BLUE)
            self.play(ShowCreation(dot),run_time = 0.05)
        sen1 = TextMobject("可以看到在这样的条件下，$x_n$趋于0",color = BLUE).scale(0.8).shift(UP*3)
        sen2 = TextMobject("那么当我们更改$\\mu$值后是否也是这样的规律呢？",color = RED).scale(0.8).shift(UP*2.2)
        self.play(Write(sen1))
        self.wait(2)
        self.play(Write(sen2))
        self.wait(3)

class Part03_2(GraphScene):
    CONFIG = {
        "x_min": 0,
        "x_max": 100,
        "x_tick_frequency": 10,
        "x_axis_label": "$n$",
        "y_axis_label": "$x_n$",
        "y_min": 0,
        "y_max": 1,
        "exclude_zero_label": False,
        "y_axis_height": 5,
        "x_axis_width": 12,
        "graph_origin": DOWN * 2.5 + LEFT * 6
    }
    def construct(self):
        self.setup_axes()
        mu = 2
        func = []
        title = TextMobject("$$x_0=0.9 \\qquad \\mu = 2$$",color = RED).shift(DOWN*3.5)
        self.play(Write(title))
        func.append(0.9)
        for i in range(1,100):
            val_y = mu*(func[i-1]-func[i-1]**2)
            func.append(val_y)
        for i,dat in enumerate(func):
            dot = Dot(radius = 0.05).move_to(self.coords_to_point(i,dat)).set_color(BLUE)
            self.play(ShowCreation(dot),run_time = 0.05)
        self.wait(26)

class Part03_3(GraphScene):
    CONFIG = {
        "x_min": 0,
        "x_max": 100,
        "x_tick_frequency": 10,
        "x_axis_label": "$n$",
        "y_axis_label": "$x_n$",
        "y_min": 0,
        "y_max": 1,
        "exclude_zero_label": False,
        "y_axis_height": 5,
        "x_axis_width": 12,
        "graph_origin": DOWN * 2.5 + LEFT * 6
    }
    def construct(self):
        self.setup_axes()
        mu = 3.2
        func = []
        title = TextMobject("$$x_0=0.9 \\qquad \\mu = 3.2$$",color = RED).shift(DOWN*3.5)
        self.play(Write(title))
        func.append(0.9)
        for i in range(1,100):
            val_y = mu*(func[i-1]-func[i-1]**2)
            func.append(val_y)
        for i,dat in enumerate(func):
            dot = Dot(radius = 0.05).move_to(self.coords_to_point(i,dat)).set_color(BLUE)
            self.play(ShowCreation(dot),run_time = 0.05)
        self.wait(18)

class Part03_4(GraphScene):
    CONFIG = {
        "x_min": 0,
        "x_max": 100,
        "x_tick_frequency": 10,
        "x_axis_label": "$n$",
        "y_axis_label": "$x_n$",
        "y_min": 0,
        "y_max": 1,
        "exclude_zero_label": False,
        "y_axis_height": 5,
        "x_axis_width": 12,
        "graph_origin": DOWN * 2.5 + LEFT * 6
    }
    def construct(self):
        self.setup_axes()
        mu = 3.54
        func = []
        title = TextMobject("$$x_0=0.9 \\qquad \\mu = 3.54$$",color = RED).shift(DOWN*3.5)
        self.play(Write(title))
        func.append(0.9)
        for i in range(1,100):
            val_y = mu*(func[i-1]-func[i-1]**2)
            func.append(val_y)
        for i,dat in enumerate(func):
            dot = Dot(radius = 0.05).move_to(self.coords_to_point(i,dat)).set_color(BLUE)
            self.play(ShowCreation(dot),run_time = 0.05)
        self.wait(10)

class Part03_5(GraphScene):
    CONFIG = {
        "x_min": 0,
        "x_max": 100,
        "x_tick_frequency": 10,
        "x_axis_label": "$n$",
        "y_axis_label": "$x_n$",
        "y_min": 0,
        "y_max": 1,
        "exclude_zero_label": False,
        "y_axis_height": 6,
        "x_axis_width": 15,
        "graph_origin": DOWN * 2.5 + LEFT * 6
    }
    def construct(self):
        self.setup_axes()
        mu = 4
        func = []
        title = TextMobject("$$x_0=0.9 \\qquad \\mu = 4$$",color = RED).shift(DOWN*3.5)
        self.play(Write(title))
        func.append(0.9)
        for i in range(1,100):
            val_y = mu*(func[i-1]-func[i-1]**2)
            func.append(val_y)
        for i,dat in enumerate(func):
            dot = Dot(radius = 0.05).move_to(self.coords_to_point(i,dat)).set_color(BLUE)
            self.play(ShowCreation(dot),run_time = 0.05)
        self.wait(3)

class Part04(Scene):
    def construct(self):
        sen1 = TextMobject("你可以看到在$\\mu=4$时便不再收敛到某几个固定的值").scale(0.8).shift(DOWN*3.5)
        sen2 = TextMobject("而是呈现出一种杂乱无章的状态").scale(0.8).shift(DOWN*3.5)
        sen3 = TextMobject("更有趣的是此时系统对初值是极为敏感的").scale(0.8).shift(DOWN*3.5)
        sen4 = TextMobject("为了更好地向你展示这种现象，我会将点与点连起来").scale(0.8).shift(DOWN*3.5)
        sen5 = TextMobject("你可以看到微小的初值差别随着时间推移带来了巨大的演化差别！").scale(0.8).shift(DOWN*3.5)
        sen6 = TextMobject("这正是一种","混沌","的体现").scale(0.8).shift(DOWN*3.5)
        sen6[1].set_color(RED)

        self.play(Write(sen1))
        self.wait(3)
        self.play(Transform(sen1,sen2))
        self.wait(3)
        self.play(Transform(sen1,sen3))
        self.wait(3)
        self.play(Transform(sen1,sen4))
        self.wait(4)
        self.play(Transform(sen1,sen5))
        self.wait(3)
        self.play(FadeOut(sen1))
        self.play(Write(sen6[0]))
        self.play(DrawBorderThenFill(sen6[1]))
        self.play(Write(sen6[2]))
        self.wait(3)

class Part04_01(GraphScene):
    CONFIG = {
        "x_min": 0,
        "x_max": 30,
        "x_tick_frequency": 10,
        "x_axis_label": "$n$",
        "y_axis_label": "$x_n$",
        "y_min": 0,
        "y_max": 1,
        "exclude_zero_label": False,
        "y_axis_height": 6,
        "x_axis_width": 12,
        "graph_origin": DOWN * 3.5 + LEFT * 6
    }
    def construct(self):
        self.setup_axes()
        mu = 4
        func = []
        func1 = []
        title = TextMobject("$$\\mu = 4$$", color=RED).shift(UP * 3.5)
        self.play(Write(title))
        name1 = TextMobject("$blue:x_0=0.9$",color = BLUE).shift(UP*3.5+RIGHT*3.7)
        name2 = TextMobject("$yellow:x_0=0.90001$",color = YELLOW).next_to(name1,DOWN).align_to(name1,LEFT)
        self.play(Write(name1),Write(name2))
        func.append(0.9)
        func1.append(0.90001)
        for i in range(1, 30):
            val_y = mu * (func[i - 1] - func[i - 1] ** 2)
            val_y1 = mu * (func1[i - 1] - func1[i - 1] ** 2)
            func.append(val_y)
            func1.append(val_y1)
        for i, dat in enumerate(func):
            dot = Dot(radius=0.05).move_to(self.coords_to_point(i, dat)).set_color(BLUE)
            if i != 0:
                line = Line(self.coords_to_point(i,dat),self.coords_to_point(i-1,func[i-1]),color = BLUE)
                self.play(ShowCreation(dot),ShowCreation(line), run_time=0.05)
            else:
                self.play(ShowCreation(dot), run_time=0.05)
        for i, dat in enumerate(func1):
            dot = Dot(radius=0.05).move_to(self.coords_to_point(i, dat)).set_color(YELLOW)
            if i != 0:
                line = Line(self.coords_to_point(i,dat),self.coords_to_point(i-1,func1[i-1]),color = YELLOW)
                self.play(ShowCreation(dot),ShowCreation(line), run_time=0.05)
            else:
                self.play(ShowCreation(dot), run_time=0.05)
        self.wait(10)

class Part05(Scene):
    def construct(self):
        sen1 = TextMobject("1963年混沌理论之父Lorentz说出了那句著名的").scale(0.8).shift(DOWN*3.5)
        sen2 = TextMobject("一个蝴蝶在巴西轻拍翅膀,","可以导致一个月后德克萨斯州的一场龙卷风.",color = BLUE).scale(0.8).shift(UP*3+RIGHT)
        sen2[1].next_to(sen2[0],DOWN).align_to(sen2,LEFT)
        eq = TextMobject("$$\\begin{cases}\\displaystyle \\frac{dx}{dt}=-\\sigma x+\\sigma y \\\\ \\displaystyle\\frac{dy}{dt} = rx-y-xz \\\\ \\displaystyle\\frac{dz}{dt}=-bz+xy\\end{cases}$$",color = RED).next_to(sen2,1.5*DOWN)
        sen3 = TextMobject("洛伦兹方程组是大气流动模型中一个简化的常微分模型").scale(0.8).shift(DOWN*3.5)
        sen4 = TextMobject("我不会去深究数学原理，但很愿意展示不同初值下其美丽的三维演化").scale(0.8).shift(DOWN*3.5)

        self.play(Write(sen1))
        self.wait(2)
        self.play(Write(sen2),run_time = 2)
        self.wait(2)
        self.play(Write(eq),run_time = 3)
        self.wait(2)
        self.play(Transform(sen1,sen3))
        self.wait(3)
        self.play(Transform(sen1,sen4))
        self.wait(15)

class Part06(Scene):
    def construct(self):
        sen1 = TextMobject("以上内容向你直观展示了混沌现象",color = BLUE).scale(0.8).shift(UP*3.5)
        sen2 = TextMobject("混沌使得我们的世界变得不那么确定，微小的初值偏差将导致系统最终巨大的差异",color = BLUE).scale(0.8).next_to(sen1,DOWN)
        sen3 = TextMobject("所以混沌告诉我们能做得只有把握现在喔！",color = RED).scale(0.8).next_to(sen2,DOWN)
        sen4 = TextMobject("混沌与非线性有着紧密的关系",color = BLUE).scale(0.8).next_to(sen3,DOWN)
        sen5 = TextMobject("回忆一下本期视频前面的例子，如果没有$\\mu x^2$项，那么种群将无限制增长下去", color = BLUE).scale(0.8).next_to(sen4,DOWN)
        sen6 = TextMobject("最后让我们再来看一个大鱼小鱼的例子!感谢你能看到这里:)",color = BLUE).scale(0.8).next_to(sen5,DOWN)

        self.play(Write(sen1))
        self.wait(2)
        self.play(Write(sen2),run_time = 2)
        self.wait(2)
        self.play(DrawBorderThenFill(sen3))
        self.wait(2)
        self.play(Write(sen4))
        self.wait(2)
        self.play(Write(sen5))
        self.wait(2)
        self.play(Write(sen6))
        self.wait(3)

class Part07(Scene):
    def construct(self):
        sen1 = TextMobject("在一个只有大鱼和小鱼的生态系统中，大鱼小鱼数量分别为$x,y$",color = BLUE).scale(0.8).shift(UP*3.5)
        sen2 = TextMobject("大鱼的出生率和小鱼的死亡率与它们的数量均有关",color = BLUE).scale(0.8).next_to(sen1,0.8*DOWN)
        sen3 = TextMobject("大鱼的出生率$=axy \\quad$ 小鱼的死亡率$=-bxy$",color = RED).scale(0.8).next_to(sen2,0.8*DOWN)
        sen4 = TextMobject("而大鱼的死亡率与小鱼的出生率则只与其自身数量有关",color = BLUE).scale(0.8).next_to(sen3,0.8*DOWN)
        sen5 = TextMobject("大鱼的死亡率$=-cx \\quad$ 小鱼的出生率$=dy$",color = RED).scale(0.8).next_to(sen4,0.8*DOWN)
        sen6 = TextMobject("$\\displaystyle\\frac{dx}{dt}=axy-cx \\quad \\frac{dy}{dt}=dy-bxy$",color = RED).scale(0.8).next_to(sen5,DOWN*0.8)
        sen7 = TextMobject("$\\displaystyle\\frac{dx}{dt}$代表变化率，也就是数量对时间的导数",color = BLUE).scale(0.8).next_to(sen6,DOWN*0.8)

        self.play(Write(sen1))
        self.wait(2)
        self.play(Write(sen2))
        self.wait(2)
        self.play(Write(sen3))
        self.wait(2)
        self.play(Write(sen4))
        self.wait(2)
        self.play(Write(sen5))
        self.wait(2)
        self.play(Write(sen6))
        self.wait(2)
        self.play(Write(sen7))
        self.wait(4)

def moveit_(point):
    x,y = point[:2]
    valx = 0.5*x*y-0.3*x
    valy = 0.8*y - 0.6*x*y
    val = np.sqrt(valx**2+valy**2)
    result = RIGHT*valx/val+UP*valy/val
    result = result * 2
    return result

class Part08(Scene):
    def construct(self):
        sen1 = TextMobject("让我们以横轴为大鱼，纵轴为小鱼，像向量场那样画出变化趋势").scale(0.8).shift(DOWN*3.5)
        sen2 = TextMobject("你可以看到$(x,y)$的初值稍有偏差便会落到不同的漩涡中！").scale(0.8).shift(DOWN*3.5)
        self.play(Write(sen1))
        self.wait(3)
        self.play(Transform(sen1,sen2))
        self.wait(10)

class Part09(GraphScene):
    CONFIG = {
        "x_tick_frequency": 10,
        "x_axis_label": "大鱼数量",
        "y_axis_label": "小鱼数量",
        "exclude_zero_label": False,
        "y_axis_height": 8,
        "x_axis_width": 15,
        "graph_origin": DOWN * 3.5 + LEFT * 6.5
    }
    def construct(self):
        self.setup_axes()
        plane = NumberPlane()
        plane.add(plane.get_axis_labels())
        #self.add(plane)
        points_ = [
            x * RIGHT + y * UP
            for x in np.arange(0, 16, 0.8)
            for y in np.arange(0, 8, 0.8)
        ]
        vec_field_ = []
        for point in points_:
            x, y = point[:2]
            valx = 0.5 * x * y - 0.3 * x
            valy = 0.8 * y - 0.6 * x * y
            val = np.sqrt(valx ** 2 + valy ** 2)
            field = 0.6 * (valy/val * UP + valx/val * RIGHT)
            result = Vector(field).shift(point)
            vec_field_.append(result)

        draw_field_ = VGroup(*vec_field_).shift(DOWN*3.5+LEFT*6.5).set_color(RED)
        self.wait(1)
        self.play(ShowCreation(draw_field_), run_time=3)
        self.wait(2)
        lines = StreamLines(
            moveit_,
            x_min = 0,
            y_min = 0,
            x_max = 16,
            y_max = 8
        ).shift(LEFT*6.5+DOWN*3.5)
        self.add_foreground_mobject(AnimatedStreamLines(
            lines,
            line_anim_class=ShowPassingFlash
        ))
        self.wait(10)