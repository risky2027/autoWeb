from selenium.webdriver import Chrome, Remote

NEGATIVE_LOGIN_CREDENTIALS = [
    ("", "!QAZ2wsx"),
    ("qa_test@test.ru", ""),
    ("qa_test", "!QAZ2wsx"),
    ("test@test.ru", "1QAZ2wsx")
]

POSITIVE_LOGIN_CREDENTIALS = {"email": "qa_test@test.ru",
                              "password": "!QAZ2wsx"}


class Links:
    base_url = {"prod": "https://qastand.valhalla.pw/",
                "stage": "https://qastand-dev.valhalla.pw/"}
    login = "login"
    profile = "profile"
    blog = "blog"


VALID_BROWSERS = {
    "chrome": Chrome,
    "remote": Remote
    #"opera": Opera
}

BROWSER_REMOTE_CAPABILITIES = {"browserName": "chrome", "version": "110.0"}

SELENOID_URL = "http://localhost:4444/wd/hub"
