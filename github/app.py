#!/usr/bin/env python
import toga

class GitHub(toga.App):
    def startup(self):
        self.main_window = toga.MainWindow(self.name, size=(800, 1000))
        self.main_window.app = self

        self.webview = toga.WebView()
        self.webview.url = "https://github.com/login"

        self.main_window.content = self.webview
        self.main_window.show()

    def open_document(self, url):
        pass

if __name__ == '__main__':
    app = GitHub('GitHub', 'org.pybee.github')
    app.main_loop()
