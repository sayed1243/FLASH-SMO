from flet import *
def main(page:Page):
    page.title = "FLASH Light SMO"
    page.scroll = 'auto'
    page.window.width= 400
    page.window.height= 750
    page.bgcolor = "#FFE8B6"
    page.window.top = 1
    page.window.left = 960
    page.theme_mode = ThemeMode.LIGHT
    
    FlashLight = Flashlight()
    page.overlay.append(FlashLight)
    
    PH = PermissionHandler()
    page.overlay.append(PH)
    
    def open_app(D):
        PH.open_app_settings()
    
    page.add(
        AppBar(
            title= Text('Flash Light SMO'),
            color='white',
            bgcolor='#77B254',
            actions=[
                IconButton(icons.SETTINGS,on_click=open_app)  
            ]
        ),
        Row([ 
            Image(src="FLASH.png",width=360)
        ],alignment=MainAxisAlignment.CENTER),
        Row([
            ElevatedButton(
                "ON",
                width=100,
                icon=icons.PLAY_ARROW,
                style=ButtonStyle(
                    bgcolor="#909",
                    color='white',
                    padding=5,
                    shape=ContinuousRectangleBorder(radius=10)
                ),
                on_click=lambda _: FlashLight.turn_on()
            ),
            ElevatedButton(
                "ON",
                width=100,
                icon=icons.PLAY_DISABLED_SHARP,
                style=ButtonStyle(
                    bgcolor="#909",
                    color='white',
                    padding=5,
                    shape=ContinuousRectangleBorder(radius=10)
                ),
                on_click=lambda _: FlashLight.turn_off()
            )
        ])
    )
app(main)