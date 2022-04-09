from manimlib.imports import *

class BeginAnimation(Scene):
    def construct(self):
        sen1 = TextMobject("我相信观看视频的很多人已经对导数很熟悉了",color = BLUE).scale(0.7).to_edge(UP)
        sen2 = TextMobject("但是我仍然打算花点时间来介绍一下它",color = BLUE).scale(0.7).next_to(sen1,DOWN*0.8)
        sen3 = TextMobject("因为它超级重要，后续的视频内容也会涉及到相关知识",color = BLUE).scale(0.7).next_to(sen2,DOWN*0.8)
        sen4 = TextMobject("让我们进入正文吧~",color = GREEN).scale(0.7).next_to(sen3,DOWN*0.8)
        sen  = TextMobject("What is Derivative?",color = BLUE).scale(1.5).shift(UP)
        self.play(Write(sen1),run_time = 1)
        self.wait(1.5)
        self.play(Write(sen2),run_time = 1)
        self.wait(1)
        self.play(Write(sen3),run_time = 1.5)
        self.wait(1)
        self.play(Write(sen4),run_time = 1)
        self.wait(1)
        group = VGroup(sen1,sen2,sen3,sen4)
        self.play(ReplacementTransform(group,sen),run_time = 1)
        self.wait(2)
        self.play(FadeOut(sen))

class Part01(GraphScene):
    CONFIG = {
        "x_min": 0,
        "x_max": 10,
        "x_tick_frequency": 1,
        "x_labeled_nums": range(0, 11, 1),
        "x_axis_label": "$x$",
        "y_min": 0,
        "y_max": 25,
        "y_tick_frequency": 5,
        "y_labeled_nums": range(0, 25, 5),
        "exclude_zero_label": False,

        "y_axis_height": 6,
        "x_axis_width": 12,
        "graph_origin": LEFT_SIDE / 7 * 6 + BOTTOM / 4 * 3,
        "func": lambda x: (x**2-4*x+5)/2,
        "steam":'steam.png'
    }
    def construct(self):
        sen1 = TextMobject("我们时常会去关注数据如何变化",color = BLUE).scale(0.7).to_edge(UP)
        self.play(Write(sen1),run_time = 1)
        self.wait(1)
        pic1 = ImageMobject(self.steam).set_height(4)
        self.play(ShowCreation(pic1),run_time = 1)
        self.wait(1.5)
        self.play(FadeOut(sen1),FadeOut(pic1),run_time = 1)

        sen2 = TextMobject("导数正是帮助我们去定量描述函数变化的工具",color = BLUE).scale(0.7).to_edge(UP)
        sen3 = TextMobject("有时我们也叫它微商",color = BLUE).scale(0.7).next_to(sen2,DOWN*0.9)
        sen4 = TextMobject("那如何去描述数据的变化呢？","我们也许会说：",color = BLUE).scale(0.7).to_edge(UP)
        sen5 = TextMobject("当两个相邻的数据之间的差越大，其变化也就越剧烈",color = BLUE).scale(0.7).next_to(sen4,DOWN*0.9)
        sen6 = TextMobject("但是这样的说法显然不够严格，而且相邻的概念太过粗略",color = BLUE).scale(0.7).next_to(sen5,DOWN*0.9)
        equation = TextMobject("$$\\displaystyle\\frac{dy}{dx}=\\lim\\limits_{\\Delta x\\rightarrow 0}\\frac{\\Delta y}{\\Delta x}$$",color = RED)
        self.play(Write(sen2),run_time = 1.5)
        self.wait(1.5)
        self.play(Write(sen3),run_time = 1.5)
        self.play(DrawBorderThenFill(equation),run_time = 1)
        self.wait(2)
        group1 = VGroup(sen2,sen3,equation)
        self.play(FadeOut(group1))
        self.play(Write(sen4[0]),run_time = 1)
        self.wait(1)
        self.play(Write(sen4[1]),run_time = 1)
        self.wait(0.5)
        self.setup_axes(animate=True)
        graph = self.get_graph(self.func, color=RED)
        self.play(ShowCreation(graph))
        self.wait(0.5)
        self.play(Write(sen5),run_time = 1.5)
        point = [
            self.input_to_graph_point(i, graph)
            for i in range(0,10) if i % 3 == 0
        ]
        dot = [
          Dot(p, color = YELLOW)
          for p in point
        ]
        self.play(FadeIn(dot[0]),FadeIn(dot[1]))
        self.play(Indicate(dot[0]),Indicate(dot[1]))
        self.wait(1)
        self.play(FadeIn(dot[2]), FadeIn(dot[3]))
        self.play(Indicate(dot[2]), Indicate(dot[3]))
        self.wait(1)
        self.play(Write(sen6),run_time = 1.5)
        self.wait(2)
        group2 = VGroup(sen4,sen5,sen6)
        self.play(FadeOut(group2),run_time = 1)
        self.play(FadeOut(dot[0]),FadeOut(dot[1]))

        sen7 = TextMobject("我们知道变化描述的是一个过程",color = BLUE).scale(0.7).to_edge(UP)
        sen8 = TextMobject("如果我们将这个过程缩到足够短,","那么对某点的变化趋势描述得也就更精确",color = BLUE).scale(0.7).next_to(sen7,DOWN*0.9)
        sen9 = TextMobject("这也正是一个无限逼近的极限思想",color = BLUE).scale(0.7).next_to(sen8,DOWN*0.9)
        equation1 = TextMobject("$$\\displaystyle\\frac{dy}{dx}=\\lim\\limits_{\\Delta x\\rightarrow 0}\\frac{\\Delta y}{\\Delta x}$$",color = BLUE).scale(0.7).to_edge(UP)
        slop1 = self.get_secant_slope_group(6, graph, dx=1)
        slop2 = self.get_secant_slope_group(6, graph, dx=0.5)
        slop3 = self.get_secant_slope_group(6, graph, dx=0.05)
        graph2 = self.get_graph(lambda x:4*x-15.5, color=GREEN)
        self.play(Write(sen7),run_time = 1)
        self.wait(1)
        self.play(Write(sen8),run_time = 2)
        self.wait(1.5)
        self.play(ShowCreation(slop1),run_time = 1)
        self.wait(1)
        self.play(ReplacementTransform(slop1,slop2))
        self.wait(1)
        self.play(ReplacementTransform(slop2,slop3))
        self.wait(1)
        self.play(Write(sen9),run_time = 1)
        self.play(ReplacementTransform(slop3,graph2),run_time = 1)
        self.wait(2)
        group3 = VGroup(sen7,sen8,sen9)
        self.play(ReplacementTransform(group3,equation1))
        self.wait(2)
        group3 = VGroup(equation1,self.axes,graph2,dot[2],dot[3],graph)
        self.play(FadeOut(group3),run_time = 1)

class Part02(ZoomedScene):
    CONFIG = {
        "zoomed_camera_frame_starting_position": np.array([2,-2, 0]),
        "zoomed_display_center": DOWN+LEFT*5,
        "zoom_factor":0.1,
        "zoomed_camera_config": {
            "default_frame_stroke_width": 2,
            "background_opacity": 0,
        },
    }

    def construct(self):
        sen1 = TextMobject("刚才我们也看到割线一步步逼近切线的过程",color = BLUE).scale(0.7).to_edge(UP)
        sen2 = TextMobject("我们也经常说某点的导数就是过该点切线的斜率",color = BLUE).scale(0.7).next_to(sen1,DOWN*0.9)
        sen3 = TextMobject("这确实符合我们的直观感受，但我想更深刻地展示一下切线为何如此特殊",color = BLUE).scale(0.7).next_to(sen2,DOWN*0.9)
        group = VGroup(sen1,sen2,sen3)
        self.play(Write(sen1),run_time = 1)
        self.wait(1)
        self.play(Write(sen2),run_time = 1)
        self.wait(1)
        self.play(Write(sen3),run_time = 2)
        self.wait(2)
        self.play(FadeOut(group))
        self.wait(0.5)

        line = FunctionGraph(lambda x:x-4,x_min = -6,x_max = 6,color = GREEN)
        line1 = FunctionGraph(lambda x:0.9*x-3.8,x_min=-6,x_max=6,color = RED)
        sen4 = TextMobject("局部放大十倍后",color = BLUE).scale(0.8).shift(DOWN*3+LEFT*5)
        sen5 = TextMobject("当我们将切线稍稍旋转",color = BLUE).scale(0.7).to_edge(UP)
        graph = FunctionGraph(lambda x:0.25*x**2-3, x_min=-6,x_max=6)

        self.play(ShowCreation(graph))
        self.play(ShowCreation(line))
        self.activate_zooming(animate=True)
        self.wait(1)
        self.play(Write(sen4),run_time = 1)
        self.wait(1)
        self.play(Write(sen5),run_time = 1)
        self.play(TransformFromCopy(line,line1))
        self.wait(1)
        self.play(FadeOut(sen5))

        sen6 = TextMobject("我们直观地看到在切点附近切线与原函数几乎重合！",color = BLUE).scale(0.7).to_edge(UP)
        sen7 = TextMobject("这也正是为什么导数的几何意义是切线的斜率",color = BLUE).scale(0.7).next_to(sen6,DOWN*0.9)
        sen8 = TextMobject("然后你自然可以理解函数的增减性与导数正负的关系啦",color = BLUE).scale(0.7).next_to(sen7,DOWN*0.9)
        self.play(Write(sen6),run_time = 1)
        self.wait(1.5)
        self.play(Write(sen7),run_time = 1)
        self.wait(1.5)
        self.play(Write(sen8),run_time = 1)
        self.wait(3)

class Part03(Scene):
    CONFIG = {
        'de':'Derivative.png'
    }
    def construct(self):
        de = ImageMobject(self.de).set_height(4).shift(DOWN)
        sen1 = TextMobject("比起导数的叫法，导函数或许更为准确",color = BLUE).scale(0.7).to_edge(UP)
        sen2 = TextMobject("它与自变量有关，描述每一点的变化",color = BLUE).scale(0.7).next_to(sen1,DOWN*0.9)
        sen3 = TextMobject("是一种映射关系，是一种描述函数变化的规则",color = BLUE).scale(0.7).next_to(sen2,DOWN*0.9)
        sen4 = TextMobject("对于一些常用函数，你需要将这些规则记下来",color = BLUE).scale(0.7).next_to(sen3,DOWN*0.9)
        self.play(Write(sen1,run_time = 1))
        self.wait(1)
        self.play(Write(sen2,run_time = 1))
        self.wait(1)
        self.play(Write(sen3,run_time = 1))
        self.wait(1)
        self.play(Write(sen4,run_time = 1))
        self.wait(2)
        self.play(FadeIn(de),run_time = 2)
        self.wait(5)
        group = VGroup(sen1,sen2,sen3,sen4)
        self.play(FadeOut(group),FadeOut(de),run_time = 1)

class Part04(Scene):
    def construct(self):
        sen1 = TextMobject("接下来，我们将用数轴上的映射来重新看待导函数",color = BLUE).scale(0.7).to_edge(UP)
        self.play(Write(sen1,run_time = 1.5))
        self.wait(1)
        self.play(FadeOut(sen1))

        sen2 = TextMobject("$$y=x$$",color = RED).to_edge(UP)
        sen22 = TextMobject("一次函数是线性变化的，因此映射也是均匀的",color = RED).scale(0.7).next_to(sen2,DOWN*0.9)
        self.play(DrawBorderThenFill(sen2),run_time = 1)
        nl1 = NumberLine(x_max = 28).shift(UP*1.5+LEFT*7)
        nl2 = NumberLine(x_max = 28).shift(DOWN*1.5+LEFT*7)
        label1 = TextMobject("$0$").scale(0.7).next_to(nl1,UP).move_to(np.array([-7,1.8,0]))
        label2 = TextMobject("$0$").scale(0.7).next_to(nl2,DOWN).move_to(np.array([-7,-1.8,0]))

        self.play(ShowCreation(nl1),FadeIn(label1),run_time = 1)
        self.play(ShowCreation(nl2),FadeIn(label2),run_time = 1)
        self.wait(2)

        arr = [
            Line(start=np.array([i/4-7,1.5,0]),end=np.array([i/4-7,-1.5,0]),color = RED)
            for i in range(0,14*4)
        ]

        group1=VGroup(sen2)
        for i in arr:
            self.play(ShowCreation(i),run_time = 0.1)
            group1.add(i)

        self.play(Write(sen22),run_time = 1)
        self.wait(2)
        self.play(FadeOut(group1),FadeOut(sen22))

        sen3 = TextMobject("$$y=x^2$$",color = BLUE).to_edge(UP)
        sen33 = TextMobject("它增长得越来越快，因此映射也呈现变化的分布",color = BLUE).scale(0.7).next_to(sen3,DOWN*0.9)
        self.play(DrawBorderThenFill(sen3),run_time = 1)

        arr1 = [
            Line(start=np.array([i/4-7, 1.5, 0]), end=np.array([(i/4)*2-7, -1.5, 0]), color=BLUE)
            for i in range(0,14*4)
        ]

        group2 = VGroup(sen3)
        for i in arr1:
            self.play(ShowCreation(i),run_time=0.1)
            group2.add(i)

        self.play(Write(sen33),run_time = 1)
        self.wait(2)
        self.play(FadeOut(group2),FadeOut(sen33))

        sen4 = TextMobject("$$y=\\sin x$$",color = GREEN).to_edge(UP)
        sen44 = TextMobject("三角函数呈现周期性变化，因此映射也有一种周期性分布",color = GREEN).scale(0.7).next_to(sen4,DOWN*0.9)
        self.play(DrawBorderThenFill(sen4),run_time = 1)

        arr2 = [
            Line(start=np.array([i/4-7, 1.5, 0]), end=np.array([np.cos(i/4)-7, -1.5, 0]), color=GREEN)
            for i in range(0, 14*4)
        ]

        group3 = VGroup(sen4)
        for i in arr2:
            self.play(ShowCreation(i),run_time = 0.1)
            group3.add(i)

        self.play(Write(sen44),run_time = 1)
        self.wait(2)
        self.play(FadeOut(group3),FadeOut(nl1),FadeOut(nl2),FadeOut(sen44),FadeOut(label1),FadeOut(label2))

class Part05(ZoomedScene):
    CONFIG = {
        "zoomed_display_center": DOWN*2 + RIGHT*2,
        "zoomed_camera_config": {
            "default_frame_stroke_width": 2,
            "background_opacity": 0,
        },
    }
    def construct(self):
        sen1 = TextMobject("Now,你大概可以理解导数的用处了",color = BLUE).scale(0.7).to_edge(UP)
        sen2 = TextMobject("它可以帮助我们通过求解导数等于$0$来找到函数的极值",color = BLUE).scale(0.7).next_to(sen1,DOWN*0.9)
        sen3 = TextMobject("但是这并不绝对,观察$x^3$的图象,你就会发现反例",color = BLUE).scale(0.7).next_to(sen2,DOWN*0.9)
        sen4 = TextMobject("极值通常会要求在这一点导函数是变号的",color = RED).scale(0.7).next_to(sen3,DOWN*0.9)
        graph = FunctionGraph(lambda x:x**3,x_min = -4,x_max = 4,color = YELLOW)
        line = FunctionGraph(lambda x:0, x_min = -4, x_max = 4,color = GREEN)
        self.play(Write(sen1),run_time = 1)
        self.wait(1)
        self.play(Write(sen2),run_time = 1.5)
        self.wait(1)
        self.play(Write(sen3),run_time = 1)
        self.wait(1)
        self.play(ShowCreation(graph),run_time = 1)
        self.play(ShowCreation(line),run_time = 1)
        self.wait(1)

        self.activate_zooming(animate=True)
        self.wait(2)

        self.play(Write(sen4),run_time = 1)
        self.wait(3)

class Part06(Scene):
    CONFIG = {
        'de_di':'di_de.png',
        'gd':'gd.png',
        'gw':'gw.png'
    }
    def construct(self):
        sen1 = TextMobject("我们刚才讨论的情况只是一元函数",color = BLUE).scale(0.7).to_edge(UP)
        sen2 = TextMobject("当涉及到多元函数时,我们需要引入方向导数的概念",color = BLUE).scale(0.7).next_to(sen1,DOWN*0.9)
        sen3 = TextMobject("你可以将它理解为沿着某一方向函数的变化率",color = BLUE).scale(0.7).next_to(sen2,DOWN*0.9)
        self.play(Write(sen1),run_time = 1)
        self.wait(1)
        self.play(Write(sen2),run_time = 1)
        self.wait(1.5)
        de_di = ImageMobject(self.de_di).set_height(4).shift(DOWN)
        self.play(FadeIn(de_di),run_time = 1)
        self.wait(2)
        self.play(Write(sen3),run_time = 1)
        self.wait(2)
        sen4 = TextMobject("而方向导数取最大值也就是变化最快的方向称之为梯度",color = BLUE).scale(0.7).next_to(sen3,DOWN*0.9)
        sen5 = TextMobject("因此梯度是一个向量,而方向导数仍然是标量",color = RED).scale(0.7).next_to(sen4,DOWN*0.9)
        self.play(Write(sen4),run_time = 1.5)
        self.wait(1.5)
        self.play(Write(sen5),run_time = 1)
        self.wait(1.5)
        group = VGroup(sen1,sen2,sen3,sen4,sen5)
        self.play(FadeOut(group),FadeOut(de_di))

        sen6 = TextMobject("方向导数与梯度的概念也许并不那么好理解",color = BLUE).scale(0.7).to_edge(UP)
        sen7 = TextMobject("这并不是这期的重点,你只需要有一个轮廓的印象",color = BLUE).scale(0.7).next_to(sen6,DOWN*0.9)
        sen8 = TextMobject("但它们在机器学习中扮演着非常重要的角色，大名鼎鼎的梯度下降法帮助我们优化神经网络",color = BLUE).scale(0.7).next_to(sen7,DOWN*0.9)
        gd = ImageMobject(self.gd).set_height(4).shift(DOWN)
        self.play(Write(sen6),run_time = 1)
        self.wait(1)
        self.play(Write(sen7),run_time = 1)
        self.wait(1)
        self.play(Write(sen8),run_time = 1.5)
        self.wait(1)
        self.play(FadeIn(gd))
        self.wait(2)
        group1 = VGroup(sen6,sen7,sen8)
        self.play(FadeOut(group1),FadeOut(gd))

        sen9 = TextMobject("但是导数并不是万能的,有时我们的目标函数可能是离散的,或非连续等等",color = BLUE).scale(0.7).to_edge(UP)
        sen10 = TextMobject("这时就需要借助例如无梯度算法来优化",color = BLUE).scale(0.7).next_to(sen9,DOWN*0.9)
        gw = ImageMobject(self.gw).set_height(4).shift(DOWN)
        self.play(Write(sen9),run_time = 2)
        self.wait(2)
        self.play(FadeIn(gw))
        self.wait(2)
        self.play(Write(sen10),run_time = 1)
        self.wait(2)
        group3 = VGroup(sen9,sen10)

        sen11 = TextMobject("当在较大的区域中绘制时,Griewank函数看似平滑(左),但是当放大时,你可以看到解空间具有多个局部最小值(中),尽管该函数仍然是平滑的(右)",color = BLUE).scale(0.7).to_edge(UP)
        self.play(ReplacementTransform(group3,sen11),run_time = 1)
        self.wait(5)