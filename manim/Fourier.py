from manimlib.imports import *

class BeginAnimation(Scene):
    CONFIG = {
        'fr':'Fourier.jpg'
    }
    def construct(self):
        fr = ImageMobject(self.fr).set_height(4).shift(DOWN*2).shift(LEFT*4)
        sen1 = TextMobject("1811年，傅里叶在热传导的论文中提出了这样一个问题：",color = BLUE).scale(0.7).to_edge(UP)
        sen2 = TextMobject("任何一个周期函数是否可以用三角函数的级数和表示？",color = RED).scale(0.7).next_to(sen1,DOWN*0.9)
        sen3 = TextMobject("这也就是我们今天要讲的主题:","傅里叶级数",color = BLUE).scale(0.7).next_to(sen2,DOWN*0.9)
        sen4 = TextMobject("我仍然希望带给你一些直观感受，尽量减少大量数学公式的出现",color = BLUE).scale(0.7).next_to(sen3,DOWN*0.9)
        sen5 = TextMobject("另外需要注意的是，本期视频中所讨论的函数均是周期的喔~",color = GREEN).scale(0.7).next_to(sen4,DOWN*0.9)
        sen3[1].set_color(RED)

        group = VGroup(sen1,sen2,sen3,sen4,sen5)
        self.play(Write(sen1),FadeIn(fr),run_time = 1)
        self.wait(1)
        self.play(Write(sen2),run_time = 1)
        self.wait(1.5)
        self.play(Write(sen3[0]),run_time = 1)
        self.wait(1)
        self.play(DrawBorderThenFill(sen3[1]),run_time = 1)
        self.wait(1.5)
        self.play(Write(sen4),run_time = 1)
        self.wait(1)
        self.play(Write(sen5),run_time = 1.5)
        self.wait(2)

        self.play(FadeOut(group),FadeOut(fr),run_time = 1)
        self.wait(1)

class Part01(GraphScene):
    CONFIG = {
        "x_min": -2 * PI,
        "x_max": 2 * PI,
        "y_min": -2,
        "y_max": 2,
        "graph_origin":ORIGIN,
        "x_axis_width": 14,
        "y_axis_height": 8,
    }

    def construct(self):
        self.setup_axes(animate=True)
        x_step = 14 / 4
        y_step = 8 / 4
        line1 = Line(np.array([-2*x_step,y_step,0]),np.array([-x_step,y_step,0]),color = BLUE)
        line2 = Line(np.array([-x_step,-y_step,0]),np.array([0,-y_step,0]),color = BLUE)
        line3 = Line(np.array([0,y_step,0]),np.array([x_step,y_step,0]),color = BLUE)
        line4 = Line(np.array([x_step,-y_step,0]),np.array([2*x_step,-y_step,0]),color = BLUE)
        linegroup = VGroup(line1,line2,line3,line4)
        self.play(FadeIn(linegroup),run_time = 1)
        func = [
            lambda x:4/PI*(np.sin(x)),
            lambda x:4/PI*(np.sin(x)+1/3*np.sin(3*x)),
            lambda x:4/PI*(np.sin(x)+1/3*np.sin(3*x)+1/5*np.sin(5*x)),
            lambda x:4/PI*(np.sin(x)+1/3*np.sin(3*x)+1/5*np.sin(5*x)+1/7*np.sin(7*x)),
            lambda x:4/PI*(np.sin(x)+1/3*np.sin(3*x)+1/5*np.sin(5*x)+1/7*np.sin(7*x)+1/9*np.sin(9*x)),
            lambda x:4/PI*(np.sin(x)+1/3*np.sin(3*x)+1/5*np.sin(5*x)+1/7*np.sin(7*x)+1/9*np.sin(9*x)+1/11*np.sin(11*x))
        ]
        f_group = [
            TextMobject("$\\displaystyle f(x)=\\frac{4}{\\pi}(\\sin x)$",color = GREEN).scale(0.7).shift(UP*3+LEFT*5),
            TextMobject("$\\displaystyle f(x)=\\frac{4}{\\pi}(\\sin x+\\frac{1}{3}\\sin 3x)$",color = GREEN).scale(0.7).shift(UP*3+LEFT*4),
            TextMobject("$\\displaystyle f(x)=\\frac{4}{\\pi}(\\sin x+\\frac{1}{3}\\sin 3x+\\frac{1}{5}\\sin 5x)$",color = GREEN).scale(0.7).shift(UP*3+LEFT*3),
            TextMobject("$\\displaystyle f(x)=\\frac{4}{\\pi}(\\sin x+\\frac{1}{3}\\sin 3x+\\frac{1}{5}\\sin 5x+\\frac{1}{7}\\sin 7x)$",color = GREEN).scale(0.7).shift(UP*3+LEFT*2),
            TextMobject("$\\displaystyle f(x)=\\frac{4}{\\pi}(\\sin x+\\frac{1}{3}\\sin 3x+\\frac{1}{5}\\sin 5x+\\frac{1}{7}\\sin 7x+\\frac{1}{9}\\sin 9x)$",color = GREEN).scale(0.7).shift(UP*3+LEFT),
            TextMobject("$\\displaystyle f(x)=\\frac{4}{\\pi}(\\sin x+\\frac{1}{3}\\sin 3x+\\frac{1}{5}\\sin 5x+\\frac{1}{7}\\sin 7x+\\frac{1}{9}\\sin 9x+\\frac{1}{11}\\sin 11x)$",color = GREEN).scale(0.7).shift(UP*3 ),
            ]
        g_graph = [
            self.get_graph(f,color = RED)
            for f in func
        ]
        self.play(Write(f_group[0]),ShowCreation(g_graph[0]),run_time = 1)
        self.wait(1.5)
        for i in range(1,6):
            self.play(ClockwiseTransform(f_group[0],f_group[i]),Transform(g_graph[0],g_graph[i]),run_time = 1)
            self.wait(1.5)
        self.wait(1)
        self.play(FadeOut(self.axes),FadeOut(f_group[0]),FadeOut(g_graph[0]),FadeOut(linegroup))
        self.wait(1)

class Part02(Scene):
    def construct(self):
        sen1 = TextMobject("尽管我用了与泰勒公式那一期类似的动画形式",color = BLUE).scale(0.7).to_edge(UP)
        sen2 = TextMobject("需要明确的是，泰勒公式与傅里叶分析具有不同的体系",color = BLUE).scale(0.7).next_to(sen1,DOWN*0.9)
        sen3 = TextMobject("首先让我们来认识正交这个概念",color = BLUE).scale(0.7).next_to(sen2,DOWN*0.9)
        sen4 = TextMobject("正交",color = RED).scale(1.5).shift(UP)
        sen5 = TextMobject("Orthogonality",color = BLUE).scale(1.5).next_to(sen4,DOWN)
        self.play(Write(sen1),run_time = 1.5)
        self.wait(1)
        self.play(Write(sen2),run_time = 1.5)
        self.wait(1)
        self.play(Write(sen3),run_time = 1)
        self.wait(1.5)
        group1 = VGroup(sen1,sen2,sen3)
        group2 = VGroup(sen4,sen5)
        self.play(ReplacementTransform(group1,group2),run_time = 1)
        self.wait(1)
        self.play(FadeOut(group2),run_time = 1)
        self.wait(1)

class Part03(Scene):
    def construct(self):
        sen1 = TextMobject("正交往往和垂直联系在一起",color = BLUE).scale(0.7).to_edge(UP)
        sen2 = TextMobject("线性代数中正交被定义为内积空间中两向量内积为零",color = BLUE).scale(0.7).next_to(sen1,DOWN*0.9)
        sen3 = TextMobject("内积的定义我们并不陌生，在学习向量时就提到过",color = BLUE).scale(0.7).next_to(sen2,DOWN*0.9)
        sen4 = TextMobject("$\\vec{a}=(x_{11},x_{12}),\\vec{b}=(x_{21},x_{22})$,","$\\vec{a}\\cdot\\vec{b}=x_{11}x_{12}+x_{21}x_{22}$",color = BLUE).scale(0.7).next_to(sen3,DOWN*0.9)
        sen5 = TextMobject("当然这只是二维的情况，从某种意义上来讲你可以认为正交是垂直概念的推广",color = BLUE).scale(0.7).next_to(sen4,DOWN*0.9)
        sen6 = TextMobject("正交意味着相互独立，这往往是我们希望看到的，正如我们选取基底时经常取成相互垂直的",color = BLUE).scale(0.7).next_to(sen5,DOWN*0.9)
        sen4[1].set_color(RED)

        vec1 = Vector(np.array([4,0,0]),color = GREEN).shift(DOWN*3)
        vec2 = Vector(np.array([0,2.5,0]),color = YELLOW).shift(DOWN*3)

        self.play(Write(sen1),run_time = 1)
        self.wait(1.5)
        self.play(ShowCreation(vec1),run_time = 1)
        self.play(ShowCreation(vec2),run_time = 1)
        self.wait(1.5)
        self.play(FadeOut(vec1),FadeOut(vec2))
        self.wait(1)
        self.play(Write(sen2),run_time = 2)
        self.wait(2)
        self.play(Write(sen3),run_time = 1.5)
        self.wait(1.5)
        self.play(Write(sen4[0]),run_time = 2)
        self.wait(1)
        self.play(DrawBorderThenFill(sen4[1]))
        self.wait(1.5)
        self.play(Write(sen5),run_time = 2)
        self.wait(2)
        self.play(Write(sen6),run_time = 2.5)
        self.wait(2)

        group1 = VGroup(sen1,sen2,sen3,sen4,sen5,sen6)
        self.play(FadeOut(group1),run_time = 1)
        self.wait(1)

        sen7 = TextMobject("但是请等一等，这些又与傅里叶级数有什么关系呢？",color = BLUE).scale(0.8).to_edge(UP)
        sen8 = TextMobject("代数是用数学语言去描述这个世界，而傅里叶分析也是用另一种方式去描述函数",color = BLUE).scale(0.8).next_to(sen7,DOWN)
        sen9 = TextMobject("所以我想从代数的角度去一起认识傅里叶级数",color = BLUE).scale(0.8).next_to(sen8,DOWN)
        sen10 = TextMobject("这并不是说需要你学习过代数，所以不妨继续看下去",color = BLUE).scale(0.8).next_to(sen9,DOWN)
        word1 = TextMobject("$t$",color = RED).scale(2).shift(DOWN+LEFT*1.5)
        word2 = TextMobject("$\\omega$",color = RED).scale(2).shift(DOWN+RIGHT*1.5)
        vec3 = Arrow(word1.get_right(),word2.get_left(),color = GREEN)
        group2 = VGroup(word1,word2,vec3)


        self.play(Write(sen7),run_time = 1.5)
        self.wait(1)
        self.play(Write(sen8),run_time = 2)
        self.wait(1)
        self.play(ShowCreation(word1))
        self.play(ShowCreation(word2))
        self.play(ShowCreation(vec3),run_time = 1)
        self.wait(1.5)
        self.play(FadeOut(group2))

        self.play(Write(sen9),run_time = 1)
        self.wait(1)
        self.play(Write(sen10),run_time = 1)
        self.wait(1)
        group3=VGroup(sen7,sen8,sen9,sen10)
        self.play(FadeOut(group3),run_time = 1)
        self.wait(1)

class Part04(Scene):
    def construct(self):
        sen1 = TextMobject("让我们回到正题，傅里叶级数是一系列三角函数的求和",color = BLUE).scale(0.7).to_edge(UP)
        sen2 = TextMobject("那么如何定义函数的内积呢？",color = RED).scale(0.7).next_to(sen1,DOWN*0.9)
        self.play(Write(sen1),run_time = 1)
        self.wait(1)
        self.play(Write(sen2),run_time = 1)
        self.wait(1.5)
        self.play(FadeOut(sen1))
        self.play(FadeOut(sen2))

        sen3 = TextMobject("我们知道向量的内积是将对应维度的坐标相乘后的求和",color = BLUE).scale(0.7).to_edge(UP)
        sen4 = TextMobject("而向量的坐标你可以理解是一种映射",color = RED).scale(0.7).next_to(sen3,DOWN*0.9)
        sen5 = TextMobject("第一维映射到其坐标，","第二维也映射到对应坐标，以此类推",color = BLUE).scale(0.7).next_to(sen4,DOWN*0.9)

        word1 = TextMobject("$1$",color = RED).scale(1.5).shift(LEFT*6+DOWN)
        word2 = TextMobject("$2$",color = RED).scale(1.5).shift(LEFT*6+DOWN*3)
        res1 = TextMobject("$x_1$",color = BLUE).scale(1.5).shift(LEFT*2+DOWN)
        res2 = TextMobject("$x_2$",color = BLUE).scale(1.5).shift(LEFT*2+DOWN*3)
        group1 = VGroup(word1,word2,res1,res2)
        arr1 = Arrow(word1.get_right(),res1.get_left(),color = GREEN)
        arr2 = Arrow(word2.get_right(),res2.get_left(),color = GREEN)

        self.play(Write(sen3),run_time = 1.5)
        self.wait(1.5)
        self.play(Write(sen4),run_time = 1.5)
        self.wait(1.5)
        self.play(ShowCreation(group1))
        self.play(Write(sen5[0]),ShowCreation(arr1),run_time = 1)
        self.wait(1)
        self.play(Write(sen5[1]),ShowCreation(arr2),run_time = 1)
        self.wait(1)

        sen6 = TextMobject("而函数正是一种映射，只不过其是连续的",color = BLUE).scale(0.7).next_to(sen5,DOWN*0.9)

        line1 = Line(np.array([2,0,0]),np.array([2,-3,0]),color = RED)
        line2 = Line(np.array([6,0,0]),np.array([6,-3,0]),color = BLUE)
        dot1 = Circle(color = RED, radius=0.05,fill_color = RED,fill_opacity=1.0).shift(RIGHT*2)
        dot2 = Circle(color = RED, radius=0.05,fill_color = RED,fill_opacity=1.0).shift(RIGHT*2+DOWN*3)
        word3 = TextMobject("$a$",color = RED).scale(1.5).next_to(dot1,LEFT)
        word4 = TextMobject("$b$",color = RED).scale(1.5).next_to(dot2,LEFT)
        vec1 = Arrow(np.array([2,0,0]),np.array([6,0,0]),color = GREEN)
        vec2 = Arrow(np.array([2,-1,0]),np.array([6,-1,0]),color = GREEN)
        vec3 = Arrow(np.array([2,-2,0]),np.array([6,-2,0]),color = GREEN)
        vec4 = Arrow(np.array([2,-3,0]),np.array([6,-3,0]),color = GREEN)
        vec_group = VGroup(vec1,vec2,vec3,vec4)
        item_group = VGroup(group1,arr1,arr2,line1,line2,dot1,dot2,word3,word4,vec_group)


        self.play(Write(sen6),run_time = 1.5)
        self.play(ShowCreation(line1),ShowCreation(line2),run_time=1)
        self.play(ShowCreation(dot1),ShowCreation(dot2),run_time = 1)
        self.play(ShowCreation(word3),ShowCreation(word4),run_time = 1)
        self.play(ShowCreation(vec_group))

        self.wait(3)
        sen7 = TextMobject("所以你现在想到要如何定义函数的内积了吗？",color = BLUE).scale(0.7).next_to(sen6,DOWN*0.9)
        self.play(Write(sen7),run_time = 1)
        self.wait(1.5)
        tip = TextMobject("我们一般用$<>$来表示内积",color = GREEN).scale(0.7).next_to(sen7,DOWN*0.9)

        self.play(Write(tip),run_time = 1.5)
        self.wait(2)
        group2 = VGroup(sen3,sen4,sen5,sen6,sen7,tip)
        self.play(FadeOut(group2))

        sen8 = TextMobject("$<\\vec a,\\vec b>=a_1b_1+a_2b_2+a_3b_3+...=\\sum a_ib_i$",color = BLUE).scale(0.8).to_edge(UP)
        sen9 = TextMobject("那么对于定义在$[a,b]$的函数，其内积可以自然想到就是积分的形式",color = BLUE).scale(0.7).next_to(sen8,DOWN*0.9)
        sen10 = TextMobject("$<f,g>=\\int_{a}^{b}f(x)g(x)dx$",color = RED).scale(0.8).next_to(sen8,DOWN)
        sen11 = TextMobject("也许有点不太容易理解，前者其维度是离散的，而对于函数而言，$[a,b]$就是它的维度",color = BLUE).scale(0.7).next_to(sen10,DOWN*0.9)
        sen12 = TextMobject("我们需要将每个维度相应的值相乘并求和，也就得到了上面的形式",color = BLUE).scale(0.7).next_to(sen11,DOWN*0.9)
        group3 = VGroup(sen8,sen10,sen11,sen12,vec_group,item_group)

        self.play(Write(sen8),run_time = 1)
        self.wait(2)
        self.play(Write(sen9),run_time = 1.5)
        self.wait(2)
        self.play(FadeOut(sen9))
        self.play(Write(sen10),run_time = 1.5)
        self.wait(1.5)
        self.play(Write(sen11),run_time = 2)
        self.wait(1.5)
        self.play(Write(sen12),run_time = 1.5)
        self.wait(2)
        self.play(FadeOut(group3),run_time = 1)
        self.wait(1)

class Part05(Scene):
    CONFIG = {
        'sz':'shaizi.jpg'
    }
    def construct(self):
        sz = ImageMobject(self.sz).set_height(4).shift(DOWN*2+LEFT*3)
        sen1 = TextMobject("如果还是不太明白，我举一个思想类似的例子",color = BLUE).scale(0.7).to_edge(UP)
        sen2 = TextMobject("对于掷骰子问题来说，点数$2-4$的概率是多少",color = BLUE).scale(0.7).next_to(sen1,DOWN*0.9)
        sen3 = TextMobject("这非常简单，我们只需要将点数为$2-4$的概率相加求和即可",color = BLUE).scale(0.7).next_to(sen2,DOWN*0.9)
        sen4 = TextMobject("那么对于另一个问题，位于$x$处的几率密度为$\\rho (x)$，那么$x$位于$a-b$之间的概率是多少呢",color = BLUE).scale(0.7).next_to(sen3,DOWN*0.9)
        sen5 = TextMobject("你可以将几率密度近似地看是结果取值为$x$的几率",color = GREEN).scale(0.7).next_to(sen4,DOWN*0.9)
        sen6 = TextMobject("$P_{ab}=\\int_a^b\\rho(x)dx$",color = RED).scale(0.8).next_to(sen4,DOWN)
        sen7 = TextMobject("又是一个分立到连续，求和到积分的过程，Right?",color = BLUE).scale(0.7).next_to(sen6,DOWN*0.9)

        self.play(Write(sen1),run_time = 1.5)
        self.wait(1)
        self.play(Write(sen2), run_time=1.5)
        self.play(FadeIn(sz))
        self.wait(1)
        self.play(Write(sen3), run_time=1.5)
        self.wait(1)
        self.play(FadeOut(sz))
        self.play(Write(sen4), run_time=2)
        self.wait(1)
        self.play(Write(sen5), run_time=1.5)
        self.wait(2)
        self.play(FadeOut(sen5))
        self.wait(1)
        self.play(Write(sen6), run_time = 1)
        self.wait(1.5)
        self.play(Write(sen7),run_time = 1.5)
        self.wait(2)
        group = VGroup(sen1,sen2,sen3,sen4,sen6,sen7)
        self.play(FadeOut(group))

class Part06(Scene):
    def construct(self):
        sen1 = TextMobject("在明白了正交的概念后，你可以想象取一组正交的基底，它们可以张成一个空间", color = BLUE).scale(0.7).to_edge(UP)
        sen2 = TextMobject("就像我们选取$\\vec{i},\\vec{j},\\vec{k}$，那么就会张成空间直角坐标系",color = BLUE).scale(0.7).next_to(sen1,DOWN*0.9)
        sen3 = TextMobject("现在让我们回到三角函数，考虑以下结论",color = BLUE).scale(0.7).next_to(sen2,DOWN*0.9)
        sen4 = TextMobject("$\\int_0^{2\\pi} \\sin mx=0$",color = RED).scale(0.8).next_to(sen3,DOWN)
        sen5 = TextMobject("$\\int_0^{2\\pi} \\cos mx=0$",color = RED).scale(0.8).next_to(sen4,DOWN)
        sen6 = TextMobject("$\\int_0^{2\\pi} \\sin mx\\cos mx=0$",color = RED).scale(0.8).next_to(sen5,DOWN)
        sen7 = TextMobject("$\\int_0^{2\\pi} \\sin mx\\sin nx=0(m\\neq n)$",color = RED).scale(0.8).next_to(sen6,DOWN)
        sen8 = TextMobject("$\\int_0^{2\\pi} \\cos mx\\cos nx=0(m\\neq n)$",color = RED).scale(0.8).next_to(sen7,DOWN)
        sen9 = TextMobject("以上$m,n$皆为正整数",color = GREEN).scale(0.7).next_to(sen8,DOWN*0.9)
        sen10 = TextMobject("这些并不难验证，你需要用到积化和差公式",color = BLUE).scale(0.7).next_to(sen9,DOWN*0.9)
        sen11 = TextMobject("Bingo!结合到内积的概念我们有了一组正交的基底$\\lbrace 1,\\sin x,\\cos x,\\sin 2x,\\cos 2x\\cdots\\rbrace$",color = BLUE).scale(0.7).to_edge(UP)
        sen12 = TextMobject("我们可以用这样一组正交的函数坐标系去描述数学世界！",color = BLUE).scale(0.7).next_to(sen11,DOWN*0.9)
        tip = TextMobject("另外，这里的范围是$[0,2\\pi]$，这是由函数周期所决定的空间范围，如果为$T$只需把基频改为$\\displaystyle\\frac{2\\pi}{T}$",color = GREEN).scale(0.6).next_to(sen8,DOWN*0.9)
        small_group = VGroup(sen9,sen10)
        self.play(Write(sen1),run_time = 2)
        self.wait(1.5)
        self.play(Write(sen2),run_time = 2)
        self.wait(1.5)
        self.play(Write(sen3),run_time = 1)
        self.wait(1)
        self.play(Write(sen4),run_time = 1)
        self.play(Write(sen5),run_time = 1)
        self.play(Write(sen6),run_time = 1)
        self.play(Write(sen7),run_time = 1)
        self.play(Write(sen8),run_time = 1)
        self.play(DrawBorderThenFill(sen9))
        self.wait(2)
        self.play(Write(sen10),run_time = 1)
        self.wait(2)
        self.play(Transform(small_group,tip),run_time = 1)
        self.wait(2.5)
        self.play(ClockwiseTransform(sen1,sen11),run_time = 1)
        self.wait(2)
        self.play(ClockwiseTransform(sen2,sen12),run_time = 1)
        self.wait(2)
        group = VGroup(sen1,sen2,sen3,sen4,sen5,sen6,sen7,sen8,sen9,sen10)
        self.play(FadeOut(group))
        self.wait(1)

class Part07(Scene):
    CONFIG = {
        'sq':'Sq.png',
        'am':'Am.png'
    }
    def construct(self):
        sq = ImageMobject(self.sq).set_height(2.5).shift(DOWN*2+LEFT*3.5)
        am = ImageMobject(self.am).set_height(2.5).shift(DOWN*2+RIGHT*3.5)
        sen1 = TextMobject("$\\displaystyle f(t)=\\frac{a_0}{2}+\\sum_{n=1}^{\\infty}(a_n\\cos \\frac{n\\pi t}{l}+b_n\\sin\\frac{n\\pi t}{l})$",color = RED).scale(0.7).to_edge(UP)
        sen2 = TextMobject("让我们来重新审视傅里叶级数公式",color = BLUE).scale(0.7).next_to(sen1,DOWN*0.9)
        sen3 = TextMobject("$\\lbrace 1,\\sin x,\\cos x,\\sin 2x,\\cos 2x \\cdots\\rbrace$也就是我们的基底",color = RED).scale(0.7).next_to(sen2,DOWN*0.9)
        sen4 = TextMobject("那么$(a_0,a_1,b_1,a_2,b_2\\cdots)$也就是我们的坐标，也就是说我们用这样的一组坐标去描述$f(x)$",color = RED).scale(0.7).next_to(sen3,DOWN*0.9)

        self.play(Write(sen1),run_time = 2)
        self.wait(1.5)
        self.play(Write(sen2),run_time = 1)
        self.wait(1)
        self.play(Write(sen3),run_time = 1.5)
        self.wait(1.5)
        self.play(Write(sen4),run_time = 2)
        self.wait(1)
        arr = Arrow(sq.get_right(),am.get_left(),color = GREEN)
        self.play(FadeIn(sq))
        self.play(ShowCreation(arr))
        self.play(FadeIn(am))
        self.wait(1)
        group1 = VGroup(sen1,sen2,sen3,sen4)
        self.play(FadeOut(group1))

        sen5 = TextMobject("那么我们如何求出这样一组坐标呢？","只需要利用一下正交的性质",color = BLUE).scale(0.7).to_edge(UP)
        sen6 = TextMobject("也就是$f(x)$与$\\sin mx(\\cos mx)$的内积只等于$\\sin mx(\\cos mx)$自身的内积，因为其他项均为$0$",color = BLUE).scale(0.7).next_to(sen5,DOWN*0.9)
        sen7 = TextMobject("$$a_n=\\displaystyle\\frac{1}{\\pi}\\int_{-\\pi}^{\\pi}f(x)\\cos nxdx$$",color = RED).scale(0.7).next_to(sen6,DOWN*0.9)
        sen8 = TextMobject("$$b_n=\\displaystyle\\frac{1}{\\pi}\\int_{-\\pi}^{\\pi}f(x)\\cos nxdx$$",color = RED).scale(0.7).next_to(sen7,DOWN*0.9)

        self.play(Write(sen5[0]),run_time = 1)
        self.wait(1)
        sen5[1].set_color(RED)
        self.play(Write(sen5[1]),run_time = 1)
        self.wait(1)
        self.play(Write(sen6),run_time = 1.5)
        self.wait(2)
        self.play(Write(sen7),run_time = 1)
        self.play(Write(sen8),run_time = 1)
        self.wait(2)
        group2 = VGroup(sen5,sen6,sen7,sen8)
        self.play(FadeOut(group2),FadeOut(sq),FadeOut(am),FadeOut(arr))
        self.wait(1)

        sen9 = TextMobject("本期视频内容大概就是这样啦，希望能帮你建立或加深傅里叶级数的认识",color = BLUE).scale(0.7).to_edge(UP)
        sen10 = TextMobject("下期视频我们将去了解这样做又怎样的意义", color = BLUE).scale(0.7).next_to(sen9,DOWN*0.9)
        sen11 = TextMobject("在结尾我依然放了函数动画，你实际上已经可以试着自己去计算这些坐标",color = BLUE).scale(0.7).next_to(sen10,DOWN*0.9)
        sen12 = TextMobject("需要注意的是这样的拟合和泰勒的原理并不同",color = BLUE).scale(0.7).next_to(sen11,DOWN*0.9)
        sen13 = TextMobject("我们的函数系是无穷的，因此用有限的坐标描述必定会损失一些信息，就像高维向量投影到低维空间一样",color = RED).scale(0.7).next_to(sen12,DOWN*0.9)
        self.play(Write(sen9),run_time = 1)
        self.wait(2)
        self.play(Write(sen10),run_time = 1)
        self.wait(2)
        self.play(Write(sen11),run_time = 1.5)
        self.wait(1.5)
        self.play(Write(sen12),run_time = 1.5)
        self.wait(1.5)
        self.play(Write(sen13),run_time = 2)
        self.wait(2)
        group3  = VGroup(sen9,sen10,sen11,sen12,sen13)
        self.play(FadeOut(group3))
        self.wait(1)

class Add_Animation(GraphScene):
    CONFIG = {
        "x_min": -2 * PI,
        "x_max": 2 * PI,
        "y_min": -4,
        "y_max": 4,
        "graph_origin":ORIGIN,
        "x_axis_width": 14,
        "y_axis_height": 8,
    }

    def construct(self):
        self.setup_axes(animate=True)
        x_step = 14 / 4
        y_step = 8 / 8
        line1 = Line(np.array([-2*x_step,0,0]),np.array([-x_step,0,0]),color = BLUE)
        line2 = Line(np.array([-x_step,-y_step*PI,0]),np.array([0,0,0]),color = BLUE)
        line3 = Line(np.array([0,0,0]),np.array([x_step,0,0]),color = BLUE)
        line4 = Line(np.array([x_step,-y_step*PI,0]),np.array([2*x_step,0,0]),color = BLUE)
        linegroup = VGroup(line1,line2,line3,line4)
        self.play(FadeIn(linegroup),run_time = 1)
        func = [
            lambda x:-PI/4,
            lambda x:-PI/4+2/PI*np.cos(x),
            lambda x:-PI/4+2/PI*np.cos(x)+np.sin(x),
            lambda x:-PI/4+2/PI*np.cos(x)+np.sin(x)-1/2*np.sin(2*x),
            lambda x:-PI/4+2/PI*np.cos(x)+np.sin(x)-1/2*np.sin(2*x)+2/9/PI*np.cos(3*x),
            lambda x:-PI/4+2/PI*np.cos(x)+np.sin(x)-1/2*np.sin(2*x)+2/9/PI*np.cos(3*x)+1/3*np.sin(3*x),
            lambda x:-PI/4+2/PI*np.cos(x)+np.sin(x)-1/2*np.sin(2*x)+2/9/PI*np.cos(3*x)+1/3*np.sin(3*x)-1/4*np.sin(4*x),
            lambda x:-PI/4+2/PI*np.cos(x)+np.sin(x)-1/2*np.sin(2*x)+2/9/PI*np.cos(3*x)+1/3*np.sin(3*x)-1/4*np.sin(4*x)+2/PI/25*np.cos(5*x),
        ]
        f_group = [
            TextMobject("$\\displaystyle f(x)=-\\frac{4}{\\pi}$",color = GREEN).scale(0.7).shift(UP*3+LEFT*5),
            TextMobject("$\\displaystyle f(x)=-\\frac{4}{\\pi}+\\frac{2}{\\pi}\\cos x$",color = GREEN).scale(0.7).shift(UP*3+LEFT*4),
            TextMobject("$\\displaystyle f(x)=-\\frac{4}{\\pi}+\\frac{2}{\\pi}\\cos x+\\sin x$",color = GREEN).scale(0.7).shift(UP*3+LEFT*3),
            TextMobject("$\\displaystyle f(x)=-\\frac{4}{\\pi}+\\frac{2}{\\pi}\\cos x+\\sin x-\\frac{1}{2}\\sin 2x$",color = GREEN).scale(0.7).shift(UP*3+LEFT*2),
            TextMobject("$\\displaystyle f(x)=-\\frac{4}{\\pi}+\\frac{2}{\\pi}\\cos x+\\sin x-\\frac{1}{2}\\sin 2x+\\frac{2}{9\\pi}\\cos 3x$",color = GREEN).scale(0.7).shift(UP*3+LEFT*1),
            TextMobject("$\\displaystyle f(x)=-\\frac{4}{\\pi}+\\frac{2}{\\pi}\\cos x+\\sin x-\\frac{1}{2}\\sin 2x+\\frac{2}{9\\pi}\\cos 3x+\\frac{1}{3}\\sin 3x$",color = GREEN).scale(0.7).shift(UP*3+LEFT*0),
            TextMobject("$\\displaystyle f(x)=-\\frac{4}{\\pi}+\\frac{2}{\\pi}\\cos x+\\sin x-\\frac{1}{2}\\sin 2x+\\frac{2}{9\\pi}\\cos 3x+\\frac{1}{3}\\sin 3x-\\frac{1}{4}\\sin 4x$",color = GREEN).scale(0.7).shift(UP*3+RIGHT),
            TextMobject("$\\displaystyle f(x)=-\\frac{4}{\\pi}+\\frac{2}{\\pi}\\cos x+\\sin x-\\frac{1}{2}\\sin 2x+\\frac{2}{9\\pi}\\cos 3x+\\frac{1}{3}\\sin 3x-\\frac{1}{4}\\sin 4x+\\frac{2}{25\\pi}\\cos 5x$",color = GREEN).scale(0.7).shift(UP*3+RIGHT*2),

            ]
        g_graph = [
            self.get_graph(f,color = RED)
            for f in func
        ]
        self.play(Write(f_group[0]),ShowCreation(g_graph[0]),run_time = 1)
        self.wait(1.5)
        for i in range(1,7):
            self.play(ClockwiseTransform(f_group[0],f_group[i]),Transform(g_graph[0],g_graph[i]),run_time = 1)
            self.wait(1.5)
        self.wait(1)
        self.play(FadeOut(self.axes),FadeOut(f_group[0]),FadeOut(g_graph[0]),FadeOut(linegroup))
        self.wait(1)

class Add_Animation2(GraphScene):
    CONFIG = {
        "x_min": -2 * PI,
        "x_max": 2 * PI,
        "y_min": -4,
        "y_max": 4,
        "graph_origin":ORIGIN,
        "x_axis_width": 14,
        "y_axis_height": 8,
    }

    def construct(self):
        self.setup_axes(animate=True)
        x_step = 14 / 4
        y_step = 8 / 8
        line1 = Line(np.array([-2*x_step,0,0]),np.array([-x_step,y_step*PI,0]),color = BLUE)
        line2 = Line(np.array([-x_step,-y_step*PI,0]),np.array([0,0,0]),color = BLUE)
        line3 = Line(np.array([0,0,0]),np.array([x_step,y_step*PI,0]),color = BLUE)
        line4 = Line(np.array([x_step,-y_step*PI,0]),np.array([2*x_step,0,0]),color = BLUE)
        linegroup = VGroup(line1,line2,line3,line4)
        self.play(FadeIn(linegroup),run_time = 1)
        func = [
            lambda x:2*(np.sin(x)),
            lambda x:2*(np.sin(x)-1/2*np.sin(2*x)),
            lambda x:2*(np.sin(x)-1/2*np.sin(2*x)+1/3*np.sin(3*x)),
            lambda x:2*(np.sin(x)-1/2*np.sin(2*x)+1/3*np.sin(3*x)-1/4*np.sin(4*x)),
            lambda x:2*(np.sin(x)-1/2*np.sin(2*x)+1/3*np.sin(3*x)-1/4*np.sin(4*x)+1/5*np.sin(5*x)),
            lambda x:2*(np.sin(x)-1/2*np.sin(2*x)+1/3*np.sin(3*x)-1/4*np.sin(4*x)+1/5*np.sin(5*x)-1/6*np.sin(6*x)),
        ]
        f_group = [
            TextMobject("$\\displaystyle f(x)=2\\sin x$",color = GREEN).scale(0.7).shift(UP*3+LEFT*5),
            TextMobject("$\\displaystyle f(x)=2(\\sin x-\\frac{1}{2}\\sin 2x)$",color = GREEN).scale(0.7).shift(UP*3+LEFT*4),
            TextMobject("$\\displaystyle f(x)=2(\\sin x-\\frac{1}{2}\\sin 2x+\\frac{1}{3}\\sin 3x)$",color = GREEN).scale(0.7).shift(UP*3+LEFT*3),
            TextMobject("$\\displaystyle f(x)=2(\\sin x-\\frac{1}{2}\\sin 2x+\\frac{1}{3}\\sin 3x-\\frac{1}{4}\\sin 4x)$",color = GREEN).scale(0.7).shift(UP*3+LEFT*2),
            TextMobject("$\\displaystyle f(x)=2(\\sin x-\\frac{1}{2}\\sin 2x+\\frac{1}{3}\\sin 3x-\\frac{1}{4}\\sin 4x+\\frac{1}{5}\\sin 5x)$",color = GREEN).scale(0.7).shift(UP*3+LEFT*1),
            TextMobject("$\\displaystyle f(x)=2(\\sin x-\\frac{1}{2}\\sin 2x+\\frac{1}{3}\\sin 3x-\\frac{1}{4}\\sin 4x+\\frac{1}{5}\\sin 5x-\\frac{1}{6}\\sin 6x)$",color = GREEN).scale(0.7).shift(UP*3),

            ]
        g_graph = [
            self.get_graph(f,color = RED)
            for f in func
        ]
        self.play(Write(f_group[0]),ShowCreation(g_graph[0]),run_time = 1)
        self.wait(1.5)
        for i in range(1,6):
            self.play(ClockwiseTransform(f_group[0],f_group[i]),Transform(g_graph[0],g_graph[i]),run_time = 1)
            self.wait(1.5)
        self.wait(1)
        self.play(FadeOut(self.axes),FadeOut(f_group[0]),FadeOut(g_graph[0]),FadeOut(linegroup))
        self.wait(1)
