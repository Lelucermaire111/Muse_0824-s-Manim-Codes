from manimlib.imports import *

class BeginAnimation(Scene):

    def construct(self):

        ##制作开场动画
        quote = TextMobject("数学的本质在于它的自由")
        quote.set_color(RED)
        quote.to_edge(UP)
        quote2 = TextMobject("The essence of mathematics lies in its freedom.")
        quote2.set_color(BLUE)
        author1 = TextMobject("-康托尔", color = PINK)
        author2 = TextMobject("-Cantor", color = BLUE)
        author2.scale(1.6)

        author1.next_to(quote.get_corner(DOWN + RIGHT), DOWN)
        author2.next_to(quote2.get_corner(DOWN + RIGHT), DOWN)

        self.play(FadeIn(quote))
        self.play(FadeIn(author1))
        self.wait(2)
        self.play(Transform(quote, quote2),
                  ApplyMethod(author1.move_to, quote2.get_corner(DOWN + RIGHT) + DOWN + 2 * LEFT))

        self.play(Transform(author1, author2))
        self.wait(1)
        self.play(FadeOut(quote), FadeOut(author1))
        self.wait()

class Part01(Scene):

    def construct(self):

        ##制作第一部分
        sentence01 = TextMobject("本期视频为大家介绍一个等差乘等比数列的口算公式", color = BLUE)
        sentence02 = TextMobject("稍后我将解释这里的A,B是什么含义", color = BLUE)
        sentence03 = TextMobject("由于初探manim", color = LIGHT_BROWN)
        sentence04 = TextMobject("所以第一期选择了一个相对简单的高中数学trick", color = LIGHT_BROWN)
        sentence05 = TextMobject("下面让我们一起看一下这个公式吧！", color = LIGHT_BROWN)

        word01 = TextMobject("等差乘等比", color = RED)
        equation = TextMobject("$\\sum_{k=1}^n(ak+b)q^{k-1} = (An+B)q^{n}-B$" )

        self.play(FadeIn(sentence01))
        self.wait(1)
        word01.scale(1.6)
        self.play(ReplacementTransform(sentence01, word01))
        self.wait(1)
        equation.scale(1.6)
        self.play(ReplacementTransform(word01, equation))
        self.wait(1)
        sentence02.shift(DOWN)
        self.play(FadeIn(sentence02))
        self.wait(1)
        self.play(FadeOut(equation),FadeOut(sentence02))

        sentence03.shift(UP)
        sentence05.shift(DOWN)
        self.play(FadeIn(sentence03))
        self.wait(1)
        self.play(FadeIn(sentence04))
        self.wait(1)
        self.play(FadeIn(sentence05))
        self.wait(1)
        self.play(FadeOut(sentence03),FadeOut(sentence04),FadeOut(sentence05))

        self.wait()

class Part02(Scene):

    def construct(self):

        sentence01 = TextMobject("设等差为$a_k=ak+b$，等比为$q_k=q^{k-1}(q\\neq 1,0)$，所求为$p_k=a_kq_k$", color = BLUE).scale(0.5)
        sentence02 = TextMobject("tips:此处省略等比数列首项简化，并不影响计算方法", color = BLUE).scale(0.5)
        sentence03 = TextMobject("我们的思路就是将该数列转换为我们会求的数列形式，下面给出推导过程。", color = BLUE).scale(0.5)

        sentence01.to_edge(UP)
        sentence02.next_to(sentence01.get_corner(DOWN), DOWN)
        sentence03.next_to(sentence02.get_corner(DOWN), DOWN)

        self.play(FadeIn(sentence01))
        self.wait(1)
        self.play(FadeIn(sentence02))
        self.wait(1)
        self.play(FadeIn(sentence03))
        self.wait(2)
        self.play(FadeOut(sentence03))

        left_equation01 = TextMobject("$\\sum_{k=1}^np_k=$").scale(0.5).next_to(sentence02.get_corner(DOWN), DOWN + LEFT * 7)
        right_equation01 = TextMobject("$(a+b)+(2a+b)q+\\cdots +(an+b)q^{n-1}$").scale(0.5).next_to(left_equation01)
        left_equation02 = TextMobject("$q\\sum_{k=1}^np_k=\\quad$").scale(0.5).next_to(left_equation01.get_corner(DOWN), DOWN)
        right_equation02 = TextMobject("$(a+b)q+\\cdots +(an-a+b)q^{n-1}+(an+b)q^{n}$").scale(0.5).next_to(left_equation02)
        sentence04 = TextMobject("接下来该怎么做呢？我相信你已经想到了：将它们相减！",color = RED).scale(0.5).next_to(sentence02.get_corner(DOWN), DOWN * 5 )
        intial_sum_01 = TextMobject("$(1-q)\\sum_{k=1}^np_k=$").scale(0.5).next_to(left_equation02.get_corner(DOWN), DOWN)
        intial_sum_02 = TextMobject("$(1-q)\\sum_{k=1}^np_k=$").scale(0.5).next_to(intial_sum_01.get_corner(DOWN), DOWN)
        right_equation03 = TextMobject("$(a+b)-(an+b)q^{n}+$", "$aq+\\cdots +aq^{n-1}$").scale(0.5).next_to(intial_sum_01)
        sentence05 = TextMobject("利用等比求和公式", color = RED).scale(0.5).next_to(intial_sum_01.get_corner(DOWN), DOWN)
        right_equation04 = TextMobject("$(a+b)-(an+b)q^{n}+$", "$a\\displaystyle\\frac{q-q^{n}}{1-q}$").scale(0.5).next_to((intial_sum_02))
        sentence06 = TextMobject("最后经过一下移项得到", color = RED).next_to(sentence05.get_corner(DOWN), DOWN).scale(0.5)
        equation05 = TextMobject("$\\sum_{k=1}^np_k=\\displaystyle\\frac{1}{1-q}[(a+b)-(an+b)q^{n}+a\\frac{q-q^{n}}{1-q}]$").next_to(sentence02.get_corner(DOWN), DOWN * 10)

        rectangle = Rectangle(color = BLUE).surround(right_equation03[1])

        group1 = VGroup(left_equation01, left_equation02)
        group2 = VGroup(right_equation01, right_equation02)
        group3 = VGroup(rectangle, right_equation03[1])

        self.play(FadeIn(left_equation01))
        self.play(FadeIn(right_equation01))
        self.wait(1)
        self.play(FadeIn(left_equation02))
        self.play(FadeIn(right_equation02))
        self.wait(1)
        self.play(GrowFromCenter(sentence04))
        self.wait(1)
        self.play(FadeOut(sentence04))
        self.play(TransformFromCopy(group1, intial_sum_01))
        self.play(TransformFromCopy(group2, right_equation03))
        self.wait(1)
        self.play(GrowFromCenter(sentence05), GrowFromCenter(rectangle))
        self.wait(1)
        self.play(ShrinkToCenter(sentence05))
        self.play(TransformFromCopy(intial_sum_01, intial_sum_02), TransformFromCopy(right_equation03[0],right_equation04[0]))
        self.wait(1)
        self.play(TransformFromCopy(group3, right_equation04[1]), FadeOut(rectangle))
        self.wait(2)
        self.play(FadeIn(sentence06))
        self.wait(1)
        self.play(FadeOut(sentence06))
        self.play(GrowFromCenter(equation05))
        self.wait()


class Part03(Scene):

    def construct(self):

        sentence01 = TextMobject("设等差为$a_k=ak+b$，等比为$q_k=q^{k-1}(q\\neq 1,0)$，所求为$p_k=a_kq_k$", color = BLUE).scale(0.5).to_edge(UP)
        sentence02 = TextMobject("tips:此处省略等比数列首项简化，并不影响计算方法", color = BLUE).scale(0.5).next_to(sentence01.get_corner(DOWN), DOWN)
        left_equation01 = TextMobject("$\\sum_{k=1}^np_k=$").scale(0.5).next_to(sentence02.get_corner(DOWN), DOWN + LEFT * 7)
        right_equation01 = TextMobject("$(a+b)+(2a+b)q+\\cdots +(an+b)q^{n-1}$").scale(0.5).next_to(left_equation01)
        left_equation02 = TextMobject("$q\\sum_{k=1}^np_k=\\quad$").scale(0.5).next_to(left_equation01.get_corner(DOWN),DOWN)
        right_equation02 = TextMobject("$(a+b)q+\\cdots +(an-a+b)q^{n-1}+(an+b)q^{n}$").scale(0.5).next_to(left_equation02)
        intial_sum_01 = TextMobject("$(1-q)\\sum_{k=1}^np_k=$").scale(0.5).next_to(left_equation02.get_corner(DOWN), DOWN)
        intial_sum_02 = TextMobject("$(1-q)\\sum_{k=1}^np_k=$").scale(0.5).next_to(intial_sum_01.get_corner(DOWN), DOWN)
        right_equation03 = TextMobject("$(a+b)-(an+b)q^{n}+$", "$aq+\\cdots +aq^{n-1}$").scale(0.5).next_to(intial_sum_01)
        right_equation04 = TextMobject("$(a+b)-(an+b)q^{n}+$", "$a\\displaystyle\\frac{q-q^{n}}{1-q}$").scale(0.5).next_to((intial_sum_02))
        equation03 = TextMobject("$\\sum_{k=1}^np_k=\\displaystyle\\frac{1}{1-q}[(a+b)-(an+b)q^{n}+a\\frac{q-q^{n}}{1-q}]$").next_to(sentence02.get_corner(DOWN), DOWN * 10)

        group1 = VGroup(sentence01, sentence02, left_equation01, right_equation01, left_equation02, right_equation02, intial_sum_01, intial_sum_02, right_equation03, right_equation04, equation03)

        self.add(group1)

        sentence03 = TextMobject("经过进一步化简我们得到", color = RED).scale(0.5).next_to(equation03.get_corner(DOWN), DOWN)
        equation04 = TextMobject("$\\sum_{k=1}^np_k=\\displaystyle\\frac{1}{q-1}[q^n(an+b-\\frac{a}{q-1})+$", "$\\displaystyle\\frac{aq}{q-1}-(a+b)$", "$]$").scale(0.5).next_to(equation03.get_corner(DOWN),DOWN)
        sentence04 = TextMobject("这一部分通过通分再次化简", color = RED).scale(0.5).next_to(equation04.get_corner(DOWN),DOWN)
        rectangle = Rectangle(color = BLUE).surround(equation04[1])
        equation05 = TextMobject("$\\sum_{k=1}^np_k=\\displaystyle\\frac{1}{q-1}[q^n(an+b-\\frac{a}{q-1})+$", "$\\displaystyle\\frac{a}{q-1}-b$", "$]$", color = BLUE).next_to(equation04.get_corner(DOWN),DOWN)

        group2 = VGroup(rectangle, equation04[1])

        self.play(FadeIn(sentence03))
        self.wait(1)
        self.play(FadeOut(sentence03))
        self.play(TransformFromCopy(equation03, equation04))
        self.wait(2)
        self.play(FadeIn(sentence04), GrowFromCenter(rectangle))
        self.wait(1)
        self.play(FadeOut(sentence04))
        self.play(TransformFromCopy(equation04[0], equation05[0]), TransformFromCopy(equation04[2], equation05[2]))
        self.wait(2)
        self.play(TransformFromCopy(group2, equation05[1]), ShrinkToCenter(rectangle))
        self.wait(2)

        group3 = VGroup(group1, equation04)

        self.play(FadeOut(group3))
        self.wait(1)

        equation05.generate_target()
        equation05.target.scale(0.5).to_edge(UP)

        self.play(MoveToTarget(equation05))
        self.wait(2)

        self.wait()


class Part04(Scene):

    def construct(self):

        equation01 = TextMobject("$\\sum_{k=1}^np_k=\\displaystyle\\frac{1}{q-1}[q^n(an+b-\\displaystyle\\frac{a}{q-1})+$", "$\\displaystyle\\frac{a}{q-1}-b$", "$]$", color = BLUE).scale(0.5).to_edge(UP)
        sentence01 = TextMobject("让我们将$\\displaystyle\\frac{1}{q-1}$乘进括号", color = RED).scale(0.5).next_to(equation01.get_corner(DOWN), DOWN)
        equation02 = TextMobject("$\\sum_{k=1}^np_k=$","(", "$\\displaystyle\\frac{a}{q-1}$", "$n$", "$+$","$\\displaystyle\\frac{b-\\displaystyle\\frac{a}{q-1}}{q-1}$","$)q^n$","$-$","$\\displaystyle\\frac{b-\\displaystyle\\frac{a}{q-1}}{q-1}$").scale(0.5).next_to(equation01.get_corner(DOWN), DOWN)
        sentence02 = TextMobject("我相信你此时已经发现了一些东西，让我们把它写得更整齐一些~", color = RED).scale(0.5).next_to(equation02.get_corner(DOWN), DOWN)
        equation03 = TextMobject("$\\sum_{k=1}^np_k=$", "$(An+B)q^n$","$-$","$B$", color = BLUE).next_to(equation02.get_corner(DOWN), DOWN)
        sentence03 = TextMobject("$A=$", "$\\displaystyle\\frac{a}{q-1}$", "$,$", "$B=$", "$\\displaystyle\\frac{b-A}{q-1}$", color = BLUE).next_to(equation03.get_corner(DOWN), DOWN)
        sentence04 = TextMobject("这样我们就通过错位相减法得到了等差乘等比的快速计算公式！", color = RED).scale(0.5).next_to(sentence03.get_corner(DOWN), DOWN)
        sentence05 = TextMobject("这个公式并不可以直接运用，但是可以悄悄地用（小声）", color = RED).scale(0.5).next_to(sentence04.get_corner(DOWN), DOWN)
        sentence06 = TextMobject("这样就可以避免繁琐的计算或者来验证计算正确性~", color = RED).scale(0.5).next_to(sentence05.get_corner(DOWN), DOWN)

        group1 = VGroup(equation02[5], equation02[8])
        group = VGroup(equation01, equation02, equation03, sentence03, sentence04, sentence05, sentence06)

        self.add(equation01)
        self.play(FadeIn(sentence01))
        self.wait(1)
        self.play(FadeOut(sentence01))
        self.play(TransformFromCopy(equation01, equation02))
        self.wait(2)
        self.play(FadeIn(sentence02))
        self.wait(1)
        self.play(FadeOut(sentence02))
        self.play(TransformFromCopy(equation02, equation03))
        self.wait(2)
        self.play(FadeIn(sentence03[0]),FadeIn(sentence03[2]),FadeIn(sentence03[3]))
        self.wait(1)
        self.play(ApplyMethod(equation02[2].set_color, RED), ApplyMethod(group1.set_color, RED))
        self.wait(1)
        self.play(TransformFromCopy(equation02[2], sentence03[1]), TransformFromCopy(group1, sentence03[4]))
        self.wait(2)
        self.play(FadeIn(sentence04))
        self.play(FadeIn(sentence05))
        self.play(FadeIn(sentence06))
        self.wait(2)
        self.play(FadeOut(group))
        self.wait()


class Part05(Scene):

    def construct(self):

        sentence01 = TextMobject("除了错位相减法外，对于此类问题还有两种方法：裂项相消法和分组求和法", color = BLUE).scale(0.5).to_edge(UP)
        sentence02 = TextMobject("在这里我们以一道例题来分析:$\\sum_{k=1}^nn2^n=?$").next_to(sentence01.get_corner(DOWN), DOWN)
        sentence03 = TextMobject("裂项相消法", color = RED).next_to(sentence02.get_corner(DOWN), DOWN)
        sentence04 = TextMobject("我们尝试用待定系数法将$n2^n$写成两项差的形式", color = RED).scale(0.5).next_to(sentence02.get_corner(DOWN), DOWN)
        equation01 = TextMobject("$n2^n=f(n+1)2^{n+1}-f(n)2^n,f(n)=An+B$").scale(0.5).next_to(sentence04.get_corner(DOWN),DOWN)
        equation02 = TextMobject("代入后可得$n\\equiv An+2A+B,A=1,B=-2,f(n)=n-2$").scale(0.5).next_to(equation01.get_corner(DOWN), DOWN)
        sentence05 = TextMobject("这里使用恒等号\"$\\equiv$\"代表对任意$n$都有该式成立").scale(0.5).next_to(equation02.get_corner(DOWN),DOWN)
        equation03 = TextMobject("$n2^n=(n-1)2^{n+1}-(n-2)2^n$", color = BLUE).scale(0.5).next_to(equation02.get_corner(DOWN),DOWN)
        equation04 = TextMobject("$S_n=\\sum_{k=1}^n[(k-1)2^{k+1}-(k-2)2^k]=$","$0-(-1)·2+2^3-0+2·2^4-2^3+\\cdots$").scale(0.5).next_to(equation03.get_corner(DOWN), DOWN)
        equation05 = TextMobject("$S_n=$","$(n-1)2^{n+1}+2$","(如果此处不明白，可以自己试着将$k+1$与$k$项相消)", color = RED).scale(0.5).next_to(equation04.get_corner(DOWN), DOWN)

        group = VGroup(sentence01, sentence02, equation01, equation02, equation03, equation04, equation05)

        self.play(FadeIn(sentence01))
        self.wait(1)
        self.play(FadeIn(sentence02))
        self.wait(1)
        self.play(FadeIn(sentence03))
        self.wait(1)
        self.play(FadeOut(sentence03))
        self.play(FadeIn(sentence04))
        self.wait(1)
        self.play(FadeOut(sentence04))
        self.play(FadeIn(equation01))
        self.wait(2)
        self.play(FadeIn(equation02))
        self.wait(1)
        self.play(FadeIn(sentence05))
        self.wait(2)
        self.play(FadeOut(sentence05))
        self.play(FadeIn(equation03))
        self.wait(1)
        self.play(FadeIn(equation04))
        self.wait(3)
        self.play(FadeIn(equation05[0]))
        self.wait(1)
        self.play(ApplyMethod(equation04[1].set_color, RED))
        self.wait(1)
        self.play(TransformFromCopy(equation04[1],equation05[1]))
        self.play(FadeIn(equation05[2]))
        self.wait(2)
        self.play(FadeOut(group))
        self.wait()


class Part06(Scene):

    def construct(self):

        sentence01 = TextMobject("分组求和法这一部分我不再细述，有兴趣的同学可以暂停观看哟~", color = RED).scale(0.5).to_edge(UP)
        equation01 = TextMobject("$S_n=2^1+(2^2+2^2)+\\cdots+(2^n+\\cdots+2^n)=(2^1+2^2+\\cdots+2^n)+(2^2+2^3+\\cdots+2^n)+\\cdots+2^n$").scale(0.5).next_to(sentence01.get_corner(DOWN), DOWN)
        equation02 = TextMobject("$S_n=\\sum_{m=1}^n\\sum_{k=m}^n2^k=\\sum_{k=m}^n(2^{n+1}-2^m)$").scale(0.5).next_to(equation01.get_corner(DOWN), DOWN)
        equation03 = TextMobject("$S_n=n2^{n+1}-2^{n+1}+2=(n-1)2^{n+1}+2$", color = RED).next_to(equation02.get_corner(DOWN), DOWN)
        group1 = VGroup(equation01,equation02,equation03)

        self.play(FadeIn(sentence01))
        self.wait(1)
        self.add(group1)
        self.wait(10)

        sentence02 = TextMobject("推广：$p_k=(ak+b)q^k$",color = BLUE).scale(0.5).next_to(equation03.get_corner(DOWN),DOWN)
        equation04 = TextMobject("$S_n=\\sum_{k=1}^n(ak+b)q^k=a\\sum_{k=1}^nkq^k+b\\sum_{k=1}^nq^k=a\\sum_{m=1}^n\\sum_{k=m}^nq^k+b\\sum_{k=1}^nq^k$", color = BLUE).scale(0.5).next_to(sentence02.get_corner(DOWN), DOWN)
        sentence03 = TextMobject("然后分别对求和符号内求和就可以啦~", color = BLUE).scale(0.5).next_to(equation04.get_corner(DOWN), DOWN)
        group2 = VGroup(sentence02, equation04, sentence03)

        self.add(group2)
        self.wait(10)
        self.wait()