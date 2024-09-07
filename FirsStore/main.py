import pyrebase
import flet as ft

firebaseconfig ={
    'apiKey': "AIzaSyCe3AOYttBOSqy3WJU3tsYpcwYy4r6j_0s",
    'authDomain': "pushgram-mobile.firebaseapp.com",
    'projectId': "pushgram-mobile",
    'storageBucket': "pushgram-mobile.appspot.com",
    'messagingSenderId': "605706942308",
    'appId': "1:605706942308:web:80385154abe5fb64882c71",
    'measurementId': "G-LBXDNVD3T3",
    "databaseURL": "https://pushgram-mobile-default-rtdb.firebaseio.com/"
}
fbase = pyrebase.initialize_app(firebaseconfig)
authorization = fbase.auth()

class Login(ft.Column):
    def __init__(self):
        super().__init__()
        self.email = ft.TextField(border_radius=5,hint_text="Email",hint_style=ft.TextStyle(color="white"),
                                  border_color="white",color="white")
        self.password = ft.TextField(can_reveal_password=True,
                                    color="white",hint_text="Password",hint_style=ft.TextStyle(color="white"),
                                    password=True,border_color="white",
                                    border_radius=5)
        self.Signin_btn = ft.OutlinedButton(text="Sign in",on_click=self.Sign_in,
                                            style=ft.ButtonStyle(
                                                color="white",
                                                side=ft.border.BorderSide(1,"white"),
                                                shape=ft.RoundedRectangleBorder(radius=5)
                                            ),width=300,height=45)
        self.alert_text = ft.Text(size=20,visible=False)
        
        self.forgot_btn = ft.TextButton("Forgot password?",style=ft.ButtonStyle(color="white"))
        self.signup_btn = ft.TextButton("Sign up",style=ft.ButtonStyle(color="white"))
        self.help_btn = ft.TextButton("Help",style=ft.ButtonStyle(color="white"))

        self.signin_layout = ft.Container(
            ft.Row(
                [
                    ft.Column(
                        [
                            ft.Row(
                                [
                                    ft.Text("Sign in",size=30,weight="bold",color="white")
                                ],
                                width=300,
                                alignment=ft.MainAxisAlignment.CENTER
                            ),
                            self.email,
                            self.password,
                            self.Signin_btn,
                            ft.Row(
                                [
                                    self.alert_text,
                                ],
                                width=300,
                                alignment=ft.MainAxisAlignment.CENTER
                            ),
                            ft.Divider(),
                            ft.Row(
                                [
                                    self.forgot_btn,
                                    self.signup_btn,
                                    self.help_btn
                                ],
                                alignment=ft.MainAxisAlignment.CENTER
                            )
                        ]
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            height=950,
            # width=500,
            border_radius=20,
            shadow= ft.BoxShadow(
                blur_radius=3,
                color="black",
                blur_style=ft.ShadowBlurStyle.OUTER
            ),
            gradient=ft.LinearGradient(
                begin=ft.alignment.top_right,
                end=ft.alignment.bottom_right,
                colors=[
                    "#cb1fc8",
                    "#1a67ac"
                ]
            ),
            margin=ft.margin.only(top=-30,left=-30,right=-30),
            padding=ft.padding.only(top=80)
        )
        self.controls = [ft.Column(
            [
                self.signin_layout
            ],
            scroll=ft.ScrollMode.HIDDEN
        )]
    def Sign_in(self, e):
        email_verify = self.email.value
        password_verify = self.password.value
        try:
            print("click")
            signin_base = authorization.sign_in_with_email_and_password(email_verify,password_verify)
            self.alert_text.visible = True
            self.alert_text.value = "Sign in completed"
            self.alert_text.color = ft.colors.GREEN
            print("sign in completed")
            
        except:
            self.alert_text.visible = True
            self.alert_text.value = "Wrong email or password"
            self.alert_text.color = ft.colors.RED
            print("Wrong email or password")
        self.update()


def main(page: ft.Page):
    # page.bgcolor = '#5e0c5d'
    page.add(Login())
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_width = 380
    page.window.height = 830
    page.update()

if __name__ == "__main__":
    ft.app(target=main)