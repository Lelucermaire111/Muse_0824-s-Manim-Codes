from manimlib.imports import *

class Begin(Scene):
    CONFIG = {
        'universe':'universe.jpg'
    }
    def construct(self):
        sen1 = TextMobject("节选自《伤心者》",color = RED).scale(2)
        self.play(DrawBorderThenFill(sen1))
        self.wait(5)

class Part01(ThreeDScene):
    def get_axis(self, min_val, max_val, axis_config):
        new_config = merge_config([
            axis_config,
            {"x_min": min_val, "x_max": max_val},
            self.number_line_config,
        ])
        return NumberLine(**new_config)
    def construct(self):
        axes = ThreeDAxes()

        plane = ParametricSurface(
            lambda u, v:np.array([
                u,
                v,
                2-u-v
            ]),u_min = -2, u_max = 2,v_min = -2, v_max = 2, checkerboard_colors = None,
            fill_color = BLUE, fill_opacity = 0.5,
            resolution=(40,40)).scale(1)

        cone = ParametricSurface(
            lambda u, v: np.array([
                u * np.cos(v),
                u * np.sin(v),
                u
            ]), v_min=0, v_max=TAU, u_min=-2, u_max=2, checkerboard_colors=[GREEN_D, GREEN_E],
            resolution=(40,40)).scale(1)
        self.add(axes)

        self.set_camera_orientation(phi=75 * DEGREES)
        self.begin_ambient_camera_rotation(rate=0.3)

        self.play(Write(cone))
        self.play(Write(plane))

        line1 = ParametricFunction(lambda t: np.array([
                                   2/(np.cos(t)+np.sin(t)+1)*np.cos(t),
                                   2/(np.cos(t)+np.sin(t)+1)*np.sin(t),
                                   2/(np.cos(t)+np.sin(t)+1)]),
                                   t_min = -TAU/5, t_max = TAU/2.5, color = RED, stroke_width = 8
                                   )
        self.wait(3)
        self.stop_ambient_camera_rotation()
        self.play(Write(line1))
        self.wait(2)
        plane_ = ParametricSurface(
            lambda u, v:np.array([
                u,
                v,
                2-2*u-2*v
            ]),u_min = -2, u_max = 2,v_min = -2, v_max = 2, checkerboard_colors = None,
            fill_color = BLUE, fill_opacity = 0.5,
            resolution=(40,40)).scale(1)
        self.play(FadeOut(line1))
        self.play(Transform(plane,plane_),run_time = 2)
        self.wait(3)
        _plane_ = ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                2 - 0.5 * u - 0.5 * v
            ]), u_min=-2, u_max=2, v_min=-2, v_max=2, checkerboard_colors=None,
            fill_color=BLUE, fill_opacity=0.5,
            resolution=(40,40)).scale(1)

        self.play(Transform(plane,_plane_),run_time = 2)

        self.wait(3)


class Part02(Scene):
    CONFIG = {
        'aplo':"Apolloni.jpg",
        'kepler':"Kepler.jpg"
    }
    def construct(self):
        aplo = ImageMobject(self.aplo).set_height(5).shift(LEFT*4+UP)
        kepler = ImageMobject(self.kepler).set_height(5).shift(LEFT*4+UP)
        sen1 = TextMobject("古希腊几何学家阿波罗尼斯总结了圆锥曲线理论",color = BLUE).scale(0.8).shift(DOWN*3.5)
        sen2 = TextMobject("一千八百年后由德国天文家开普勒将其应用于行星轨道理论",color = RED).scale(0.8).shift(DOWN*3.5)

        note = TextMobject("开普勒三定律", color = RED).shift(UP*3).shift(RIGHT*3)
        note1 = TextMobject("1.椭圆定律",color = BLUE).next_to(note,1.5*DOWN).align_to(note,LEFT)
        note2 = TextMobject("2.面积定律", color = BLUE).next_to(note1, 1.5*DOWN).align_to(note1,LEFT)
        note3 = TextMobject("3.调和定律", color = BLUE).next_to(note2, 1.5*DOWN).align_to(note2,LEFT)
        law = VGroup(note,note1,note2)

        great = TextMobject("阿波罗尼斯（前262-前190年）",color = RED).scale(0.8).next_to(aplo,DOWN)
        great1 = TextMobject("开普勒（1571-1630）",color = RED).scale(0.8).next_to(kepler,DOWN)

        self.play(Write(sen1))
        self.play(FadeIn(aplo),Write(great))
        self.wait(3)
        self.play(FadeOut(aplo),FadeOut(great))
        self.play(Transform(sen1,sen2))
        self.play(FadeIn(kepler),Write(great1))
        self.play(Write(law),run_time = 3)
        self.play(Write(note3))
        self.wait(5)

class Part02_anim(ThreeDScene):
    def construct(self):
        r = 7
        sun = Sphere(radius = 1, fill_color = RED, fill_opacity = 0.8).shift(RIGHT*math.sqrt(28))
        planet = Sphere(radius = 0.4).shift(UP*6)
        orbit = ParametricFunction(lambda t: np.array([
                                   8*np.cos(t),
                                   6*np.sin(t),
                                   0]),
                                   t_min = 0, t_max = TAU, color = RED, stroke_width = 8
                                   )
        system = VGroup(orbit,sun,planet)

        F_vector = Vector(np.array([math.sqrt(28),-6,0]),color = YELLOW).next_to(planet,DOWN*0.6).shift(RIGHT*3)
        F_formula = TextMobject("$\\vec {F}=G m_1 m_2\\displaystyle \\frac{(\\vec{r_1}-\\vec{r_2})}{r^3}$",color = RED)
        F_formula.rotate_about_origin(PI)
        F_formula.next_to(F_vector,LEFT*0.4).shift(RIGHT*2)
        self.set_camera_orientation(phi=65 * PI / 180, theta=PI / 2)

        self.play(ShowCreation(orbit))
        self.play(FadeIn(sun),FadeIn(planet))
        self.wait(1)
        self.play(ShowCreation(F_vector))
        self.play(Write(F_formula))
        self.wait(1)



class Part03(Scene):
    CONFIG = {
        'galois':"Galois.jpg",
        'group':"group_theory.jpg"
    }
    def construct(self):
        galois = ImageMobject(self.galois).set_height(5).shift(LEFT*4+UP)
        group = ImageMobject(self.group).set_height(5)
        great = TextMobject("伽罗瓦（1811-1832）",color = RED).next_to(galois,DOWN)
        sen1 = TextMobject("数学家伽罗瓦公元1831年创立群论",color = BLUE).scale(0.8).shift(DOWN*3.5)
        sen2 = TextMobject("一百余年后获得物理应用",color = RED).scale(0.8).shift(DOWN*3.5)

        title = TextMobject("Group Theory",color = RED).shift(UP*3.5+RIGHT*4)
        group.next_to(title,DOWN)

        self.play(Write(sen1))
        self.play(FadeIn(galois))
        self.play(Write(great))
        self.wait(2)
        self.play(Transform(sen1,sen2))
        self.play(Write(title))
        self.play(FadeIn(group))
        self.wait(5)

class Part04(Scene):

    def construct(self):
        sen1 = TextMobject("公元1860年创立的矩阵理论","在六十年后应用于量子力学").scale(0.8).shift(DOWN*3.5)
        sen1[0].set_color(BLUE)
        sen1[1].set_color(RED)

        equation = TextMobject("$$\\bra{\\phi}=\\begin{bmatrix} \\bra{\\psi _1} \\bra{\\psi _2} \\cdots \\bra{\\psi _n} \\cdots \\end{bmatrix} \\begin{bmatrix} C_1 \\\\ C_2 \\\\ \\vdots \\\\ C_n \\\\ \\vdots \\end{bmatrix}$$").set_color(BLUE)
        self.play(Write(sen1[0]))
        self.wait(1)
        self.play(Write(sen1[1]))
        self.play(Write(equation))
        self.wait(5)

class Part05(Scene):
    CONFIG = {
        'gauss':'Gauss.jpg',
        'riemann':'Riemann.jpg',
        'lobach':'Lobach.jpg',
        'mobius':'mobius.jpg',
        'relative':'Relative.jpg'
    }
    def construct(self):
        gauss = ImageMobject(self.gauss).set_height(5).shift(LEFT*4+UP)
        mobius = ImageMobject(self.mobius).set_height(3).shift(RIGHT*4)
        relative = ImageMobject(self.relative).set_height(3.5).shift(RIGHT*4 + DOWN)

        great = TextMobject("高斯（1777-1855）",color = RED).next_to(gauss,DOWN)
        sen1 = TextMobject("数学家高斯，黎曼，罗马切夫斯基等人提出并发展了非欧几何",color =BLUE).scale(0.8).shift(DOWN*3.5)
        sen2 = TextMobject("高斯一生都在探索非欧几何的实际应用，但他抱憾而终",color = BLUE).scale(0.8).shift(DOWN*3.5)
        sen3 = TextMobject("非欧几何诞生一百七十年后",color = RED).scale(0.8).shift(DOWN*3.5)
        sen4 = TextMobject("这种在当时毫无用处的理论以及由之发展而来的张量分析理论",color = BLUE).scale(0.8).shift(DOWN*3.5)
        sen5 = TextMobject("成为爱因斯坦广义相对论的核心基础",color = RED).scale(0.8).shift(DOWN*3.5)

        equation = TextMobject("$$[ij,k]=\\displaystyle\\frac{1}{2}(\\frac{\\partial g_{ik}}{\\partial x^j}+\\frac{\\partial g_{jk}}{\\partial x^i}+\\frac{\\partial g_{ij}}{\\partial x^k})$$")
        equation.set_color(BLUE).shift(RIGHT*3.5+UP*2)

        self.play(Write(sen1))
        self.play(FadeIn(gauss))
        self.play(Write(great))
        self.wait(2)
        self.play(Transform(sen1,sen2))
        self.play(ApplyWave(great))
        self.play(FadeIn(mobius))
        self.wait(2)
        self.play(FadeOut(mobius))
        self.play(Transform(sen1,sen3))
        self.wait(3)
        self.play(Transform(sen1,sen4))
        self.play(Write(equation),run_time = 2)
        self.wait(2)
        self.play(Transform(sen1,sen5))
        self.play(FadeIn(relative))
        self.wait(5)

class Part06(Scene):
    def construct(self):
        sen1 = TextMobject("何夕(小说虚构人物)提出并于公元1999年完成的微连续理论",color = BLUE).shift(UP*0.5)
        sen2 = TextMobject("一百五十年后这一成果最终导致了大一统场理论方程式的诞生",color = BLUE).shift(DOWN*1)
        sen3 = TextMobject("世界沉默着，为了这些伤心的名字，",color = BLUE).shift(UP*0.5)
        sen4 = TextMobject("为了这些伤心的名字后面那千百年的寂寞时光",color = BLUE).shift(DOWN)

        self.play(Write(sen1))
        self.wait(2)
        self.play(Write(sen2))
        self.wait(3)
        self.play(FadeOut(sen1),FadeOut(sen2))
        self.play(DrawBorderThenFill(sen3))
        self.wait(2)
        self.play(DrawBorderThenFill(sen4))
        self.wait(5)