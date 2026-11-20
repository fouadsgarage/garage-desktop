import webview

webview.settings['ALLOW_DOWNLOADS'] = True

garageURL = "https://fouadsgarage.github.io/garage/"

webview.create_window(
    "Garage",
    garageURL,
    width=1200,
    height=600,
    resizable=True
)
webview.start()
