class Browser:
    def __init__(self) -> None:
        self.url = ''
        self.back_browser = []

    def insert_url(self, url):
        self.back_browser.append(self.url)
        self.url = url

    def back(self):
        if self.back_browser:
            self.url = self.back_browser.pop()

    def brows(self):
        return self.url


brows = Browser()

brows.insert_url('google.com')
brows.insert_url('fb.com')
print(brows.brows())
brows.back()
print(brows.brows())
