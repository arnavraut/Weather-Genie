from view.home_layout import HomeLayout
from control.app_control import AppController

"""Main script"""
control = AppController(HomeLayout())
control.run_app()