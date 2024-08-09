from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.button import MDFlatButton, MDRaisedButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.screen import MDScreen
from kivymd.uix.widget import MDWidget
from sympy import symbols, solve

class Linear(MDWidget):
    Builder.load_file("kivy_file/linear.kv")

    def close_dialog(self, obj):
        self.dialog.dismiss()

    def solve(self):
        big_string = ""
        self.dialog = None
        try:
            a = float(self.ids.x.text)
            b = float(self.ids.b.text)
            n = float(self.ids.n.text)
            equation = f"{a}x     {b}   =   {n}"
            big_string += "\n\nEquation is : "
            big_string += equation
            val = (n + (-1 * b)) / a
            big_string += f"\n\n=>      {a}x = {n}+{-1 * b}\n\n=>      {a}x = {n + (-1 * b)}\n\n=>      x = {n + (-1 * b)}/{a}\n\n=>    x = {(n + (-1 * b)) / a}"
            big_string += "\n\n\n So the value of x is : " + str(val)
            MDApp.get_running_app().solution(big_string)
        except Exception as e:
            print(e)
            self.dialog = MDDialog(
                title='Aleart',
                text="Equation is invalid.\n            or\nRoot is not exists.",
                buttons=[
                    MDRaisedButton(text='OK', on_release=self.close_dialog), ]
            )
            self.dialog.open()
class Quadratic(MDWidget):
    Builder.load_file("kivy_file/quadratic.kv")
    def close_dialog(self, obj):
        self.dialog.dismiss()  #close the box
    def solve(self):
        global x2, x1
        self.dialog = None
        a = float(self.ids.x2.text)
        b = float(self.ids.x.text)
        c = float(self.ids.c.text)
        chk = (b * b) - 4 * a * c
        chk=round(chk,3)
        if chk > 0:
            x1 = (-b + (chk ** 0.5)) / (2 * a)
            x2 = (-b - (chk ** 0.5)) / (2 * a)
            x1=round(x1,3)
            x2=round(x2,3)
        elif chk < 0:
            c = ((-1*chk) ** 0.5) / (2 * a)
            c=round(c,3)
            x1=f"{-b}+{c}i"
            x2=f"{-b}-{c}i"
        elif chk==0:
            self.dialog = MDDialog(
                title='Aleart',
                text="Equation is invalid.\n            or\nRoot is not exists.",
                buttons=[
                    MDRaisedButton(text='OK', on_release=self.close_dialog), ]
            )
            self.dialog.open()
        if chk!=0:
            str=f"""
            Equation is : {a}x^2    +   {b}x    +   {c} =   0
            check,
                b^2-4ac !=0
            {b}^2-4{a}{c}={chk}
            where, b^2-4ac > 0
            So,
                the roots are exits.
            By using quadratic formula,
                
                x1 = (-{b} + ({chk}^0.5)) / (2{a})  =   {x1}
                
                x2 = (-{b} - ({chk}^0.5)) / (2{a})  =   {x2}
                
                Therefore,
                    roots are : {x1}    ,   {x2}    
            """
            MDApp.get_running_app().solution(str)
class Cubic(MDWidget):
    Builder.load_file("kivy_file/cubic.kv")
    def close_dialog(self, obj):
        self.dialog.dismiss()  #close the box
    def solve(self):
        big_string = ""
        lst = []
        val = []
        self.dialog = None
        try:
            a = float(self.ids.x3.text)
            b = float(self.ids.x2.text)
            c = float(self.ids.x.text)
            d = int(self.ids.d.text)
            equation = f"{a}x^3    {b}x^2    {c}x     {d}"
            big_string += "\n\nEquation is : "
            big_string += equation
            for i in range(1, abs(d)):
                if d % i == 0:
                    lst.append(i)
                    lst.append(-1 * i)
                    if eval(f"{a}*{i}**3+{b}*{i}**2+{c}*{i}+{d}") == 0:
                        val.append(i)
                        if (len(val) == 2):
                            break
                    i *= -1
                    if eval(f"{a}*{i}**3+{b}*{i}**2+{c}*{i}+{d}") == 0:
                        val.append(i)
                        if len(val) == 2:
                            break
            X = symbols('x')
            big_string += "\n\nFactors are : "
            big_string += str(lst)
            big_string += f"\n\nf({val[0]})=0 and f({val[1]})=0"
            big_string += "\n\nTherefore; Two roots are :"
            big_string += str(val)
            eq1 = a * X ** 3 + b * X ** 2 + c * X + d
            sol1 = X - val[0]
            sol2 = X - val[1]
            eq2 = (sol1 * sol2).simplify()
            result = eq1 / eq2
            simplified_result = result.simplify()
            val3 = solve(simplified_result, X)
            val.append(val3)
            big_string += "\n\n"
            big_string += str(result) + " = " + str(simplified_result)
            big_string += "\n\nSo the third root is : "
            big_string += str(simplified_result) + " = " + str(val3)
            big_string += "\n\n\n So the Roots are : " + str(val)
            MDApp.get_running_app().solution(big_string)
        except:
            if len(val) < 2:
                self.dialog = MDDialog(
                    title='Aleart',
                    text="Equation is invalid.\n            or\nRoot is not exists.",
                    buttons=[
                        MDRaisedButton(text='OK', on_release=self.close_dialog), ]
                )
                self.dialog.open()
class SolvePage(MDWidget):
    Builder.load_file("kivy_file/solve_page.kv")

    def set_result(self, string):
        self.ids.result.text = string
class HomePage(MDWidget):
    Builder.load_file("kivy_file/homepage.kv")
class MainApp(MDApp):
    title = "Equation Solver"
    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.screen = MDScreen()
        self.home_page = HomePage()
        self.screen.add_widget(self.home_page)
        return self.screen
    def Linear(self):
        self.linear = Linear()
        self.screen.clear_widgets()
        self.screen.add_widget(self.linear)
    def Quadratic(self):
        self.quadratic = Quadratic()
        self.screen.clear_widgets()
        self.screen.add_widget(self.quadratic)
    def Cubic(self):
        self.cubic = Cubic()
        self.screen.clear_widgets()
        self.screen.add_widget(self.cubic)
    def solution(self, string):
        sol_page = SolvePage()
        sol_page.set_result(string)
        self.screen.clear_widgets()
        self.screen.add_widget(sol_page)
    def back(self):
        self.screen.clear_widgets()
        self.screen.add_widget(self.home_page)

if __name__ == "__main__":
    MainApp().run()
