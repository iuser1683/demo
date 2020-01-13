import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
import time

class NavigationPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    # Locators
    _total_home_links = "//div/ul/li//a"
    _home_navigation_link = "//div/ul/li//a[@href=\"{0}\"]"
    _ab_test = _home_navigation_link.format("/abtest")
    _add_remove = _home_navigation_link.format("/add_remove_elements/")
    _basic_auth = _home_navigation_link.format("/basic_auth")
    _broken_images = _home_navigation_link.format("/broken_images")
    _challenging_dom = _home_navigation_link.format("/challenging_dom")
    _checkboxes = _home_navigation_link.format("/checkboxes")
    _context_menu = _home_navigation_link.format("/context_menu")
    _digest_auth = _home_navigation_link.format("/digest_auth")
    _disappearing_elements = _home_navigation_link.format("/disappearing_elements")
    _drag_and_drop = _home_navigation_link.format("/drag_and_drop")
    _dropdown = _home_navigation_link.format("/dropdown")
    _dynamic_content = _home_navigation_link.format("/dynamic_content")
    _dynamic_controls = _home_navigation_link.format("/dynamic_controls")
    _dynamic_loading = _home_navigation_link.format("/dynamic_loading")
    _entry_ad = _home_navigation_link.format("/entry_ad")
    _exit_intent = _home_navigation_link.format("/exit_intent")
    _download = _home_navigation_link.format("/download")
    _upload = _home_navigation_link.format("/upload")
    _floating_menu = _home_navigation_link.format("/floating_menu")
    _forgot_password = _home_navigation_link.format("/forgot_password")
    _login = _home_navigation_link.format("/login")
    _frames = _home_navigation_link.format("/frames")
    _geolocation = _home_navigation_link.format("/geolocation")
    _horizontal_slider = _home_navigation_link.format("/horizontal_slider")
    _hovers = _home_navigation_link.format("/hovers")
    _infinite_scroll = _home_navigation_link.format("/infinite_scroll")
    _inputs = _home_navigation_link.format("/inputs")
    _jqueryui = _home_navigation_link.format("/jqueryui/menu")
    _javascript_alerts = _home_navigation_link.format("/javascript_alerts")
    _javascript_error = _home_navigation_link.format("/javascript_error")
    _key_presses = _home_navigation_link.format("/key_presses")
    _large = _home_navigation_link.format("/large")
    _windows = _home_navigation_link.format("/windows")
    _nested_frames = _home_navigation_link.format("/nested_frames")
    _notification_message = _home_navigation_link.format("/notification_message")
    _redirector = _home_navigation_link.format("/redirector")
    _download_secure = _home_navigation_link.format("/download_secure")
    _shifting_content = _home_navigation_link.format("/shifting_content")
    _slow = _home_navigation_link.format("/slow")
    _tables = _home_navigation_link.format("/tables")
    _status_codes = _home_navigation_link.format("/status_codes")
    _typos = _home_navigation_link.format("/typos")
    _tinymce = _home_navigation_link.format("/tinymce")

    _add_button = "//div[@id='content']//button[.='Add Element']"



    def totalElementsInHomePage(self):
        return self.getElementList(self._total_home_links, "xpath")

    def navigate_AbTest(self):
        self.elementClick(self._ab_test, "xpath")

    def url_verify(self, expected):
        return self.verifyUrl(expected)


    def navigate_add_remove(self):
        self.elementClick(self._add_remove, "xpath")

    def navigate_basic_auth(self):
        self.elementClick(self._basic_auth, "xpath")

    def navigate_broken_images(self):
        self.elementClick(self._broken_images, "xpath")

    def navigate_challenging_dom(self):
        self.elementClick(self._challenging_dom, "xpath")

    def navigate_checkboxes(self):
        self.elementClick(self._checkboxes, "xpath")

    def navigate_context_menu(self):
        self.elementClick(self._context_menu, "xpath")

    def navigate_digest_auth(self):
        self.elementClick(self._digest_auth, "xpath")

    def navigate_disappearing_elements(self):
        self.elementClick(self._disappearing_elements, "xpath")

    def navigate_drag_and_drop(self):
        self.elementClick(self._drag_and_drop, "xpath")

    def navigate_dropdown(self):
        self.elementClick(self._dropdown, "xpath")

    def navigate_dynamic_content(self):
        self.elementClick(self._dynamic_content, "xpath")

    def navigate_dynamic_controls(self):
        self.elementClick(self._dynamic_controls, "xpath")

    def navigate_entry_ad(self):
        self.elementClick(self._entry_ad, "xpath")

    def navigate_exit_intent(self):
        self.elementClick(self._exit_intent, "xpath")

    def navigate_download(self):
        self.elementClick(self._download, "xpath")

    def navigate_upload(self):
        self.elementClick(self._upload, "xpath")

    def navigate_floating_menu(self):
        self.elementClick(self._floating_menu, "xpath")

    def navigate_forgot_password(self):
        self.elementClick(self._forgot_password, "xpath")

    def navigate_login(self):
        self.elementClick(self._login, "xpath")

    def navigate_frames(self):
        self.elementClick(self._frames, "xpath")

    def navigate_geolocation(self):
        self.elementClick(self._geolocation, "xpath")

    def navigate_horizontal_slider(self):
        self.elementClick(self._horizontal_slider, "xpath")

    def navigate_hovers(self):
        self.elementClick(self._hovers, "xpath")

    def navigate_infinite_scroll(self):
        self.elementClick(self._infinite_scroll, "xpath")

    def navigate_inputs(self):
        self.elementClick(self._inputs, "xpath")

    def navigate_jqueryui(self):
        self.elementClick(self._jqueryui, "xpath")

    def navigate_javascript_alerts(self):
        self.elementClick(self._javascript_alerts, "xpath")

    def navigate_javascript_error(self):
        self.elementClick(self._javascript_error, "xpath")

    def navigate_key_presses(self):
        self.elementClick(self._key_presses, "xpath")

    def navigate_large(self):
        self.elementClick(self._large, "xpath")

    def navigate_windows(self):
        self.elementClick(self._windows, "xpath")

    def navigate_nested_frames(self):
        self.elementClick(self._nested_frames, "xpath")

    def navigate_notification_message(self):
        self.elementClick(self._notification_message, "xpath")

    def navigate_redirector(self):
        self.elementClick(self._redirector, "xpath")

    def navigate_download_secure(self):
        self.elementClick(self._download_secure, "xpath")

    def navigate_shifting_content(self):
        self.elementClick(self._shifting_content, "xpath")

    def navigate_slow(self):
        self.elementClick(self._slow, "xpath")

    def navigate_tables(self):
        self.elementClick(self._tables, "xpath")

    def navigate_status_codes(self):
        self.elementClick(self._status_codes, "xpath")

    def navigate_typos(self):
        self.elementClick(self._typos, "xpath")

    def navigate_tinymce(self):
        self.elementClick(self._tinymce, "xpath")

