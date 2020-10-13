from selenium.webdriver.common.by import By


class LoginForm:
    LOGIN_LINK = "ocs-app.local:8019"
    EMAIL = (By.NAME, "email")
    PASSWORD = (By.NAME, "password")
    BUTTON = (By.TAG_NAME, "span")


class Monitor:
    MONITOR_LINK = (By.NAME, "menu_monitoring")
