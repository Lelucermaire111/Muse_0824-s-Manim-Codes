from manimlib.imports import *

class BeginAnimation(GraphScene):
    def construct(self):
        grid = NumberPlane(
            axis_config={"stroke_color": WHITE
                        }
        )
        self.play(ShowCreation(grid), run_time = 2)
        self.wait(1)
        func_graph_1 = FunctionGraph(lambda x:(np.exp(x)-np.exp(-x))/2, color = GREEN)
        func_graph_2 = FunctionGraph(lambda x:(np.exp(x)+np.exp(-x))/2, color = RED)
        sinh = TextMobject("$$sinh(x)=\\displaystyle\\frac{e^x-e^{-x}}{2}$$", color = GREEN).shift(DOWN*2+LEFT*4)
        cosh = TextMobject("$$cosh(x)=\\displaystyle\\frac{e^x+e^{-x}}{2}$$", color = RED).shift(UP*2+LEFT*4)
        self.play(ShowCreation(func_graph_1), run_time = 2)
        self.play(Write(sinh), run_time = 1)
        self.wait(1)
        self.play(ShowCreation(func_graph_2), run_time = 2)
        self.play(Write(cosh), run_time = 1)
        self.wait(2)
        group = VGroup(grid, func_graph_1, func_graph_2, sinh, cosh)
        title = TextMobject("双曲正弦与双曲余弦", color = BLUE).scale(1.5)
        self.play(ReplacementTransform(group, title), run_time = 1)
        self.wait(2)
        self.play(FadeOut(title))
        self.wait()

class Part01(Scene):
    def construct(self):
        sen1 = TextMobject("在大学第一堂高数课上，基本都会提到双曲正弦与双曲余弦函数", color = BLUE).scale(0.8).to_edge(UP)
        formula = TextMobject("$sinh(x)=\\displaystyle\\frac{e^x-e^{-x}}{2},cosh(x)=\\displaystyle\\frac{e^x+e^{-x}}{2}$",color = RED).scale(0.8).next_to(sen1, DOWN)
        sen2 = TextMobject("但是，我们为什么需要定义这两个函数呢？", color = BLUE).scale(0.8).next_to(formula, DOWN)
        sen3 = TextMobject("本期视频让我们一起深入地认识它们!", color = BLUE).scale(0.8).next_to(sen2, DOWN)
        sen4 = TextMobject("别担心，和往常一样，并没有数学基础的特殊要求:)", color = GREEN).scale(0.8).next_to(sen3, DOWN)
        self.play(Write(sen1), run_time = 2)
        self.wait(1)
        self.play(Write(formula), run_time = 2)
        self.wait(1)
        self.play(Write(sen2), run_time = 1.5)
        self.wait(1)
        self.play(Write(sen3), run_time = 1.5)
        self.wait(1)
        self.play(Write(sen4), run_time = 2)
        self.wait(2)
        group = VGroup(sen1, formula, sen2, sen3 , sen4)
        self.play(FadeOut(group))

class Part02(GraphScene):
    CONFIG = {
        "x_min": -6,
        "x_max": 6,
        "y_min": -2,
        "y_max": 2,
        "x_axis_width": 6,
        "y_axis_height": 4,
        "graph_origin": ORIGIN+DOWN*1.8,
        "function_color": RED,
        "axes_color": WHITE,
    }
    def construct(self):
        sen1 = TextMobject("当我们去关注一个函数的时候，很重要的一个性质就是奇偶性", color = BLUE).scale(0.8).to_edge(UP)
        sen2 = TextMobject("$奇函数是指f(x)=-f(-x)$，","$而偶函数是指f(x)=f(-x)$",color = BLUE).scale(0.8).next_to(sen1, DOWN)
        f1 = lambda x:np.sin(x)
        f2 = lambda x:np.cos(x)
        f3 = lambda x:np.cosh(x)
        f4 = lambda x:np.sinh(x)
        self.play(Write(sen1), run_time = 2)
        self.wait(1)
        self.play(Write(sen2[0]), run_time = 1)
        self.setup_axes(animate=True)
        g1 = self.get_graph(f1,color = GREEN)
        g2 = self.get_graph(f2, color = RED)
        g3 = self.get_graph(f3, color = GREEN)
        g4 = self.get_graph(f4, color = RED)
        self.play(ShowCreation(g1))
        self.wait(1)
        self.play(Write(sen2[1]))
        self.play(ReplacementTransform(g1,g2))
        self.wait(2)
        self.play(FadeOut(g2),FadeOut(self.axes))
        sen3 = TextMobject("一个关于奇偶性很有趣的性质是：", color = BLUE).scale(0.8).next_to(sen2, DOWN)
        sen4 = TextMobject("任何函数可以被分解成一个奇函数与一个偶函数之和", color = RED).scale(0.8).next_to(sen3, DOWN)
        tip = TextMobject("当然，这里要求定义域是关于原点对称的，你可以先暂停下来自己想一想", color = GREEN).scale(0.8).next_to(sen4,DOWN)
        sen5 = TextMobject("$f(x)=$","$\\displaystyle\\frac{f(x)+f(-x)}{2}$","$+$","$\\displaystyle\\frac{f(x)-f(-x)}{2}$", color = BLUE).scale(0.8).next_to(sen4,DOWN)
        sen5[1].set_color(RED)
        sen5[3].set_color(GREEN)
        sen6 = TextMobject("很容易验证红色部分是偶函数，而绿色部分是奇函数", color = BLUE).scale(0.8).next_to(sen5,DOWN)
        self.play(Write(sen3),run_time = 1)
        self.wait(1)
        self.play(Write(sen4), run_time = 2)
        self.wait(1)
        self.play(Write(tip, run_time = 2))
        self.wait(2)
        self.play(FadeOut(tip))
        self.play(Write(sen5, run_time = 2))
        self.wait(1.5)
        self.play(Write(sen6),Indicate(sen5[1], color = RED),Indicate(sen5[3], color = GREEN), run_time = 1.5)
        self.wait(2)
        group1 = VGroup(sen1,sen2,sen3,sen4,sen5,sen6)
        self.play(FadeOut(group1),run_time = 1)
        self.wait(1)


class Part03(Scene):
    def construct(self):
        sen1 = TextMobject("从开头的动画我们看到，双曲正弦是奇函数，而双曲余弦是偶函数", color = BLUE).scale(0.8).to_edge(UP)
        sen2 = TextMobject("而它们的和正是","$y=e^x$", color = BLUE).scale(0.8).next_to(sen1, DOWN)
        sen2[1].set_color(RED)
        sen3 = TextMobject("也就是说它们所包含的信息是和指数函数相同的，但是因为它们有一些很好的性质，我们在与指数函数相关的问题中可以用它们来表达", color = BLUE).scale(0.8).next_to(sen2,DOWN)
        sen4 = TextMobject("这就类似于对于向量问题，我们第一步需要做的就是选取一组合适的基底", color = BLUE).scale(0.8).next_to(sen3,DOWN)
        sen5 = TextMobject("良好的基底能极大地简化问题", color = BLUE).scale(0.8).next_to(sen4, DOWN)
        vec = Vector(np.array([4,4,0]), color = BLUE).shift(DOWN*3.8)
        vec1 = Vector(np.array([2,2*(3**0.5),0]), color = RED).shift(DOWN*3.8)
        vec2 = Vector(np.array([2*(3**0.5),2,0]), color = GREEN).shift(DOWN*3.8)
        sen6 = TextMobject("在立体几何问题中建立合适的坐标系也是同样的道理", color = BLUE).scale(0.8).next_to(sen5, DOWN)
        sen7 = TextMobject("也就是说基底从$e^x,e^{-x}$变成了$sinh,cosh$，通常能帮助我们简化问题", color = BLUE).scale(0.8).next_to(sen6,DOWN)
        self.play(Write(sen1), run_time = 2)
        self.wait(1)
        self.play(Write(sen2[0]), run_time = 1)
        self.play(DrawBorderThenFill(sen2[1]))
        self.wait(1)
        self.play(Write(sen3),run_time = 2.5)
        self.wait(2)
        self.play(Write(sen4),run_time = 2)
        self.wait(1)

        self.play(ShowCreation(vec),run_time = 1)
        self.wait(1)
        self.play(ShowCreation(vec1),run_time = 1)
        self.play(ShowCreation(vec2),run_time = 1)
        self.wait(1)
        formula1 = TextMobject("$\\vec a=$","$0.732\\vec x_1$","$+$","$0.732\\vec x_2$").scale(1.2).shift(DOWN*1.5+LEFT*4)
        formula1[1].set_color(GREEN)
        formula1[3].set_color(RED)
        formula2 = TextMobject("$\\vec a =$","$\\vec x_1$","$+$","$\\vec x_2$").scale(1.2).shift(DOWN*1.5+LEFT*4)
        formula2[1].set_color(GREEN)
        formula2[3].set_color(RED)
        self.play(Write(formula1),run_time = 1)
        self.wait(1)
        self.play(Write(sen5),run_time = 1)
        self.play(Rotating(vec1,about_point = np.array([0,-3.8,0]),radians = PI/6),Rotating(vec2,about_point = np.array([0,-3.8,0]),radians = -PI/6),run_time = 1)
        self.wait(1)
        self.play(ReplacementTransform(formula1,formula2),run_time = 1)
        self.wait(2)
        self.play(FadeOut(vec1),FadeOut(vec2),FadeOut(vec),FadeOut(formula2))

        self.play(Write(sen6),run_time = 1)
        self.wait(1.5)
        self.play(Write(sen7),run_time = 1.5)
        self.wait(1.5)
        group = VGroup(sen1,sen2,sen3,sen4,sen5,sen6,sen7)
        self.play(FadeOut(group),run_time = 1)
        self.wait(1)

class Part04(Scene):
    def construct(self):
        begin = TextMobject("让我们再来看一个很简单的例子", color = GREEN).scale(0.8).to_edge(UP)
        sen1 = TextMobject("当我们求解一个轨迹问题时，根据条件推断出解是对于$x=0$偶对称的", color = BLUE).scale(0.8).to_edge(UP)
        sen2 = TextMobject("假设通过计算得到解的形式为","$y=Ae^x+Be^{-x}$",color = BLUE).scale(0.8).next_to(sen1,DOWN)
        sen2[1].set_color(RED)
        sen_2 = TextMobject("假设通过计算得到解的形式为","$y=A\\sinh x+B\\cosh x$").scale(0.8).next_to(sen1,DOWN)
        sen_2[1].set_color(RED)
        sen_2[1].shift(RIGHT)
        sen3 = TextMobject("根据我们以上的讨论，我们也可以将解写成这样的形式",color = GREEN).scale(0.7).next_to(sen2,DOWN)
        sen4 = TextMobject("而由对称性我们可以立即得到$A=0$，因为sinh是奇对称的",color = BLUE).scale(0.8).next_to(sen2,DOWN)
        sen5 = TextMobject("这并不是说原来的形式不能解决问题，而是双曲正余弦的形式能给我们一些更加直观的物理感受~", color = RED).scale(0.8).next_to(sen4,DOWN)
        sen6 = TextMobject("But wait...为什么它们就和三角函数建立起关系了呢？接下来我们就一起去讨论这一点", color = BLUE).scale(0.8).next_to(sen5, DOWN)
        graph1 = FunctionGraph(lambda x:x**2,x_min = -2,x_max = 2).set_color(GREEN).shift(DOWN*3)
        graph2 = FunctionGraph(lambda x:np.cos(x),x_min = -2*PI,x_max = 2*PI).set_color(GREEN).shift(DOWN*2)
        graph3 = FunctionGraph(lambda x:np.cosh(x),x_min = -2, x_max = 2).set_color(GREEN).shift(DOWN*3)
        graph4 = FunctionGraph(lambda x:np.sinh(x),x_min = -2,x_max = 2).set_color(RED).shift(DOWN*1)
        self.play(Write(begin),run_time = 1)
        self.wait(1)
        self.play(FadeOut(begin))
        self.play(Write(sen1),run_time = 1.5)
        self.wait(1)
        self.play(ShowCreation(graph1),run_time = 1)
        self.wait(1)
        self.play(ReplacementTransform(graph1,graph2),run_time = 1)
        self.wait(1)
        self.play(ReplacementTransform(graph2,graph3),run_time = 1)
        self.wait(1)
        self.play(Write(sen2),run_time = 1.5)
        self.wait(1.5)
        self.play(Write(sen3),run_time = 1.5)
        self.play(ClockwiseTransform(sen2[1],sen_2[1]))
        self.wait(1)
        self.play(FadeOut(sen3))
        self.play(Write(sen4),run_time = 1.5)
        self.play(ShowCreationThenFadeOut(graph4,run_time = 2))
        self.wait(1)
        self.play(FadeOut(graph3))
        self.play(Write(sen5),run_time = 1.5)
        self.wait(1)
        self.play(Write(sen6),run_time = 1.5)
        self.wait(2)
        group=VGroup(sen1,sen2,sen4,sen5,sen6)
        self.play(FadeOut(group))
        self.wait(2)

class Part05(Scene):
    def construct(self):
        sen1 = TextMobject("首先我在这里写出一些双曲正余弦的性质", color = BLUE).scale(0.8).to_edge(UP)
        sen2 = TextMobject("这些性质都很容易验证，你可以试试看",color = BLUE).scale(0.8).next_to(sen1,DOWN)
        prop1 = TextMobject("$\\cosh^2 x-\\sinh^2 x=1$",color = RED).scale(0.8).next_to(sen2,DOWN)
        prop2 = TextMobject("$\\sinh (x+y)=\\sinh x\\cosh y+\\cosh x\\sinh y$", color = RED).scale(0.8).next_to(prop1,DOWN)
        prop3 = TextMobject("$\\cosh (x+y)=\\cosh x\\cosh y+\\sinh x\\sinh y$", color = RED).scale(0.8).next_to(prop2,DOWN)
        prop4 = TextMobject("$\\sinh 'x=\\cosh x,\\cosh 'x=\\sinh x$",color = RED).scale(0.8).next_to(prop3,DOWN)
        sen3 = TextMobject("和三角函数的性质十分相似，Right?",color = BLUE).scale(0.8).next_to(prop4,DOWN)
        sen4 = TextMobject("但我想让你更直观地感受，理解这样的定义是有意义的", color = BLUE).scale(0.8).next_to(sen3,DOWN)
        sen5 = TextMobject("让我们先从老朋友——圆说起", color = BLUE).scale(0.8).next_to(sen4,DOWN)
        self.play(Write(sen1),run_time = 1)
        self.wait(1.5)
        self.play(Write(sen2),run_time = 1)
        self.wait(1.5)
        self.play(Write(prop1),run_time = 1)
        self.wait(1)
        self.play(Write(prop2),run_time = 1)
        self.wait(1)
        self.play(Write(prop3),run_time = 1)
        self.play(Write(prop4),run_time = 1)
        self.wait(3)
        self.play(Write(sen3),run_time = 1)
        self.wait(1.5)
        self.play(Write(sen4),run_time = 1.5)
        self.wait(1.5)
        self.play(DrawBorderThenFill(sen5),run_time = 2)
        self.wait(2)
        group = VGroup(sen1,sen2,prop1,prop2,prop3,prop4,sen3,sen4,sen5)
        self.play(FadeOut(group))
        self.wait()

class Part06(Scene):
    def construct(self):
        sen1 = TextMobject("圆是怎样与三角函数建立起联系的呢？").scale(0.65).to_edge(UP).to_edge(LEFT)
        sen2 = TextMobject("$\\cos ^2\\theta+\\sin ^2\\theta=1$对应圆的方程$x^2+y^2=1$").scale(0.65).next_to(sen1,0.8*DOWN)
        grid = ComplexPlane(
            axis_config={"stroke_color": WHITE}
        )
        self.play(ShowCreation(grid), run_time=2)
        cir = Circle(radius = 3).set_color(BLUE)
        line = Line(np.array([0,0,0]), np.array([3*np.cos(1), 3*np.sin(1), 0]), color = BLUE)
        line1 = Line(np.array([0,0,0]),np.array([3*np.cos(1),0,0]), color = GREEN)
        line2 = Line(np.array([3*np.cos(1),0,0]),np.array([3*np.cos(1),3*np.sin(1),0]), color = RED)
        arc = Arc(radius=0.8, angle=1).set_color(BLUE)
        label = TextMobject("$\\theta$", color = BLUE).scale(0.8).next_to(arc, RIGHT*0.8)
        label2 = TextMobject("$\\sin \\theta$",color = RED).scale(0.8).next_to(line2,RIGHT)
        label1 = TextMobject("$\\cos \\theta$",color = GREEN).scale(0.8).next_to(line1,DOWN)
        self.play(ShowCreation(cir))
        self.play(Write(sen1),run_time = 1.5)
        self.wait(1)
        self.play(Write(sen2),run_time = 1.5)
        self.wait(1)
        self.play(ShowCreation(arc), ShowCreation(line))
        self.play(Write(label))
        self.play(ShowCreation(line1),Write(label1),run_time = 1.5)
        self.play(ShowCreation(line2),Write(label2),run_time = 1.5)
        self.wait(2)
        sen3 = TextMobject("Up之前也介绍过可以通过复数来理解$e^{i\\theta}=\\cos \\theta+i\\sin \\theta$",color = RED).scale(0.65).to_edge(UP).to_edge(LEFT)
        sen4 = TextMobject("在复数域中，旋转等操作也有着更加直观的物理图像").scale(0.65).next_to(sen3,DOWN*0.8)
        sen5 = TextMobject("Now，你能试着建立一套双曲余弦的几何图像吗？", color = RED).scale(0.65).next_to(sen4,DOWN*0.8)
        group1 = VGroup(sen1,sen2)
        self.play(FadeOut(group1))
        self.play(Write(sen3),run_time = 1)
        self.wait(1.5)
        self.play(Write(sen4),run_time = 1)
        self.wait(1.5)
        self.play(Write(sen5),run_time = 1)
        self.wait(2)
        group2 = VGroup(sen3,sen4,sen5)
        self.play(FadeOut(group2))
        self.wait(2)
        sen = TextMobject("$\\cosh ^2x-\\sinh ^2x=1$")
        group3 = VGroup(cir,line,line1,line2,label,label1,label2,arc,line2,grid)
        self.play(ReplacementTransform(group3,sen),run_time = 2)
        self.wait(2)
        self.play(FadeOut(sen),run_time = 1)
        self.wait()

class Part07(GraphScene):
    CONFIG = {
        "x_min": 0,
        "x_max": 10,
        "x_axis_label": "$x$",
        "y_min": 0,
        "y_max": 25,
        "y_tick_frequency": 5,
        "exclude_zero_label": False,

        "y_axis_height": 3,
        "x_axis_width": 6,
        "graph_origin": LEFT_SIDE/10 * 9 + BOTTOM / 4 * 3,
        "func": lambda x: (x**2-4*x+5)/2
    }
    def construct(self):
        grid = ComplexPlane(
            axis_config={"stroke_color": WHITE}
        )
        self.play(ShowCreation(grid), run_time=2)
        graph1 = FunctionGraph(lambda x:(x**2-1)**0.5,x_min=1).set_color(BLUE)
        graph2 = FunctionGraph(lambda x:-(x**2-1)**0.5,x_min=1).set_color(BLUE)
        graph0 = VGroup(graph1,graph2)
        line = Line(np.array([0,0,0]),np.array([10**0.5,3,0]))
        line1 = Line(np.array([0,0,0]),np.array([10**0.5,0,0]),color = GREEN)
        line2 = Line(np.array([10**0.5,0,0]),np.array([10**0.5,3,0]),color = RED)
        label1 = TextMobject("$\\cosh u$",color = GREEN).scale(0.8).next_to(line1,DOWN)
        label2 = TextMobject("$\\sinh u$",color = RED).scale(0.8).next_to(line2,RIGHT)
        sen1 = TextMobject("Right！你一定会想到那么就令$x=\\cosh u,y=\\sinh u$",color = BLUE).scale(0.7).to_edge(UP).to_edge(LEFT)
        sen2 = TextMobject("这也正是双曲线的物理图像！",color = RED).scale(0.7).next_to(sen1,DOWN)
        self.play(Write(sen1),run_time = 1.5)
        self.wait(1.5)
        self.play(ShowCreation(graph0),run_time = 1)
        self.play(Write(sen2),run_time = 1)
        self.wait(2)
        self.play(FadeOut(sen2))
        self.play(ShowCreation(line))
        self.play(ShowCreation(line1),ShowCreation(label1))
        self.play(ShowCreation(line2),ShowCreation(label2))
        self.wait(2)
        sen2 = TextMobject("但是...$u$的物理含义并不如圆心角$\\theta$那样清晰",color = BLUE).scale(0.7).next_to(sen1,DOWN)
        sen3 = TextMobject("然而数学中总有一些美丽的巧合...",color = BLUE).scale(0.7).next_to(sen2,DOWN)
        self.play(Write(sen2),run_time = 1)
        self.wait(1)
        self.play(Write(sen3),run_time = 1)
        self.wait(1.5)
        self.play(FadeOut(sen1),FadeOut(sen2),FadeOut(sen3),run_time = 1)
        rec = Rectangle(width = 7,height = 8,color = BLACK, fill_color = BLACK, fill_opacity=1).shift(LEFT*3.6)
        self.play(FadeIn(rec))
        self.wait(1.5)
        label_o=TextMobject("$O$").scale(0.8).next_to(np.array([0,0,0]))
        label_a=TextMobject("$A$").scale(0.8).next_to(np.array([1,0,0]))
        label_b=TextMobject("$B$").scale(0.8).next_to(np.array([10**0.5,0,0]))
        label_c=TextMobject("$C$").scale(0.8).next_to(np.array([10**0.5,3,0]))
        sen4 = TextMobject("如何计算类似扇形OAC的面积呢？",color = BLUE).scale(0.65).to_edge(UP).to_edge(LEFT)
        sen5 = TextMobject("$S_{OAC}=S_{OBC}-S_{ABC}$",color = RED).scale(0.65).next_to(sen4,DOWN*0.8)
        tip1 = TextMobject("那么我们只需要计算$S_{ABC}$即可",color = BLUE).scale(0.65).next_to(sen5,DOWN*0.8)
        tip2 = TextMobject("接下来将会涉及一点定积分的知识...",color = BLUE).scale(0.65).next_to(tip1,DOWN*0.8)
        tip3 = TextMobject("别担心，你可以将它理解为细分为小矩形的叠加",color = BLUE).scale(0.6).next_to(tip2,DOWN*0.8).shift(0.8*RIGHT)
        label = TextMobject("$(x_0,y_0)$").scale(0.8).next_to(label_c)
        label_0=TextMobject("$(\\cosh\\phi_0,\\sinh\\phi_0)$",color = BLUE).scale(0.8).next_to(label_c)
        self.play(FadeIn(label_o),FadeIn(label_a),FadeIn(label_b),FadeIn(label_c),FadeIn(label),run_time = 1)
        self.play(Write(sen4),run_time = 1)
        self.wait(1)
        self.play(Write(sen5),run_time = 1)
        self.wait(1)
        self.play(Write(tip1),run_time = 1)
        self.wait(1)
        self.play(Write(tip2),run_time = 1)
        self.wait(1)
        self.play(Write(tip3),run_time = 1)
        self.setup_axes(animate=True)
        graph = self.get_graph(self.func, color = RED)
        area = self.get_area(graph, 2, 8)
        self.play(FadeIn(graph),run_time = 1.5)
        self.play(ShowCreation(area),run_time = 2)
        self.wait(2)
        group1 = VGroup(tip1,tip2,tip3,self.axes,graph,area)
        self.play(FadeOut(group1),run_time = 1)
        sen6 = TextMobject("$S_{OAC}=\\displaystyle\\frac{1}{2}x_0\\sqrt{x_0 ^2-1}-\\int_{1}^{x_0}\\sqrt{x^2-1}dx$","$=\\displaystyle\\frac{1}{2}\\phi_0$",color = RED).scale(0.65).next_to(sen5,DOWN*0.8).shift(RIGHT*0.5)
        sen7 = TextMobject("熟悉定积分的同学可以试着计算一下，并不麻烦",color = BLUE).scale(0.65).next_to(sen6,DOWN*0.8)
        sen8 = TextMobject("不熟悉计算也没有关系，理解就好:)",color = BLUE).scale(0.65).next_to(sen7,DOWN*0.8)
        sen9 = TextMobject("如果我们在计算过程中令$x=\\cosh\\phi$就会得到",color = BLUE).scale(0.65).next_to(sen6,DOWN*0.8)
        self.wait(1)
        self.play(Write(sen6[0]),run_time = 1.5)
        self.wait(2)
        self.play(Write(sen7),run_time = 1)
        self.wait(1)
        self.play(Write(sen8),run_time = 1)
        self.wait(1.5)
        self.play(FadeOut(sen7),FadeOut(sen8))
        self.play(Write(sen9),run_time=1)
        self.play(ReplacementTransform(label,label_0),run_time = 1)
        self.wait(1.5)
        self.play(DrawBorderThenFill(sen6[1]),run_time = 1)
        self.wait(2)
        self.play(FadeOut(sen9))
        sen10 = TextMobject("BINGO!和扇形面积具有非常类似的形式！").scale(0.65).next_to(sen6,DOWN*0.8)
        self.play(Write(sen10),run_time = 1.5)
        self.wait(1.5)
        sen11 = TextMobject("$S=\\displaystyle\\frac{1}{2}r^2\\phi=\\frac{1}{2}\\phi$",color = RED).scale(0.65).next_to(sen10,DOWN*0.65)
        sec = Sector(start_angle = 0,angle = PI/3,inner_radius = 0,outer_radius = 4, arc_center=np.array([-6,-3.5,0]),fill_color = BLUE,fill_opacity=0.8)
        label3 = TextMobject("$\\phi$").shift(LEFT*6+DOWN*3.5)
        self.play(ShowCreation(sec),ShowCreation(label3))
        self.wait(1)
        self.play(Write(sen11),run_time = 1)
        self.wait(2)
        group2 = VGroup(sen10,sen11,label3,sec)
        self.play(FadeOut(group2))
        self.wait(0.5)
        sen12 = TextMobject("因此我们将$OAC$定义为双曲扇形",color = RED).scale(0.65).next_to(sen6,DOWN*0.8)
        sen13 = TextMobject("而将$\\phi$定义为双曲角",color = RED).scale(0.65).next_to(sen12,DOWN*0.8)
        self.play(Write(sen12),run_time = 1.5)
        self.wait(1)
        self.play(Write(sen13),run_time = 1.5)
        self.wait(3)
        group3 = VGroup(sen4,sen5,sen6,sen12,sen13,grid,rec,label_a,label_b,label_c,label_0,label_o,line,line1,line2,label1,label2,graph0)
        self.play(FadeOut(group3),run_time = 1)
        self.wait(1)

class Part08(Scene):
    def construct(self):
        sen1 = TextMobject("如正余弦去描述圆一样，双曲正余弦是描述双曲线的",color = BLUE).scale(0.8).to_edge(UP)
        sen2 = TextMobject("但是圆是封闭且对称的，双曲线则没有这样好的性质",color = BLUE).scale(0.8).next_to(sen1,DOWN)
        sen3 = TextMobject("因此双曲正余弦的出现频率也没有正余弦这样高",color = BLUE).scale(0.8).next_to(sen2,DOWN)
        sen4 = TextMobject("但是它们在结构上是很相似的",color = BLUE).scale(0.8).next_to(sen3,DOWN)
        sen5 = TextMobject("$\\sin x=\\displaystyle\\frac{e^{ix}-e^{-ix}}{2i},\\sinh x=\\frac{e^x-e^{-x}}{2}$",color = RED).scale(0.8).next_to(sen4,DOWN)
        sen6 = TextMobject("在复数域来看，$\\sinh x$也具有$2\\pi i$的周期呢！",color = GREEN).scale(0.8).next_to(sen5,DOWN)
        sen7 = TextMobject("让我们从Wiki百科中的两张图再次感受一下它们之间的联系",color = BLUE).scale(0.8).next_to(sen6,DOWN)
        self.play(Write(sen1),run_time = 1.5)
        self.wait(2)
        self.play(Write(sen2),run_time = 1.5)
        self.wait(2)
        self.play(Write(sen3),run_time = 1.5)
        self.wait(1)
        self.play(Write(sen4),run_time = 1.5)
        self.play(Write(sen5),run_time = 1.5)
        self.wait(2)
        self.play(Write(sen6),run_time = 1.5)
        self.wait(2)
        self.play(Write(sen7),run_time = 1.5)
        self.wait(2)
        group = VGroup(sen1,sen2,sen3,sen4,sen5,sen6,sen7)
        self.play(FadeOut(group),run_time = 1)
        self.wait()

class Wiki(Scene):
    CONFIG = {
        'p_a':'Circle-trig.png',
        'p_b':'Hyperbola-trig.png'
    }
    def construct(self):
        p_a = ImageMobject(self.p_a)
        p_a.set_height(6)
        p_a.shift(LEFT*4)
        p_b = ImageMobject(self.p_b)
        p_b.set_height(6)
        p_b.shift(RIGHT*3)
        self.play(FadeIn(p_b),FadeIn(p_a),run_time = 2)
        self.wait(10)
        self.play(FadeOut(p_a),FadeOut(p_b))
        self.wait()

class Part09(Scene):
    CONFIG = {
        'p_a':'Kette_Kettenkurve_Catenary_2008_PD.jpg',
        'p_b':'SpiderCatenary.jpg'
    }
    def construct(self):
        sen1 = TextMobject("事实上，双曲余弦最早来源于悬链线的研究",color = BLUE).scale(0.8).to_edge(UP)
        sen2 = TextMobject("悬链线是一个固定项链两段，在重力场中让它自然垂下，项链的曲线方程",color = RED).scale(0.8).next_to(sen1,DOWN)
        sen3 = TextMobject("它在生活中是如此的常见！",color = BLUE).scale(0.8).next_to(sen2,DOWN)
        sen4 = TextMobject("双曲正余弦也会出现在一些拉普拉斯方程的解中$\\nabla ^2u=0$",color = RED).scale(0.8).next_to(sen2,DOWN)
        sen5 = TextMobject("现在有更多地理解一点它了吗？",color = BLUE).scale(0.8).next_to(sen4,DOWN)
        sen6 = TextMobject("最后用《昆虫记》里的一段话结尾吧！拜拜~",color = BLUE).scale(0.8).next_to(sen5,DOWN)
        self.play(Write(sen1),run_time = 1)
        self.wait(1)
        self.play(Write(sen2),run_time = 2)
        self.wait(1)
        self.play(Write(sen3))
        self.wait(1)
        p_a = ImageMobject(self.p_a)
        p_a.set_height(4)
        p_a.shift(DOWN*1.7+LEFT*3)
        p_b = ImageMobject(self.p_b)
        p_b.set_height(4)
        p_b.shift(DOWN*1.7+RIGHT*3)
        self.play(FadeIn(p_a),run_time = 1)
        self.play(FadeIn(p_b),run_time = 1)
        self.wait(3)
        self.play(FadeOut(p_a),FadeOut(p_b),FadeOut(sen3))
        self.play(Write(sen4),run_time = 1)
        self.wait(1.5)
        self.play(Write(sen5),run_time = 1)
        self.wait(1)
        self.play(Write(sen6),run_time = 1)
        self.wait(2)
        group = VGroup(sen1,sen2,sen4,sen5,sen6)
        self.play(FadeOut(group),run_time = 1)
        self.wait()

class Part10(Scene):
    def construct(self):
        text=TextMobject("在一个浓雾弥漫的清晨，让我们检视一下夜间刚刚织好的网吧。粘性的蜘蛛丝，负著水滴的重量，弯曲成一条条悬链线，水滴随著曲线的弯曲排成精致的念珠，整整齐齐，晶莹剔透。当阳光穿过雾气，整张带著念珠的网映出彩虹般的亮光，就像一丛灿烂的宝石。e这个数是多么地辉煌！"
                         ,color = BLUE).scale(0.8).to_edge(UP)
        self.play(Write(text),run_time = 5)
        self.wait(3)
        self.wait(3)
        self.wait(3)
        self.wait()