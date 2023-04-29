import time

from .troubleshoot_page import TroubleshootPage

from selenium.webdriver.common.keys import Keys


class AppiqPage(TroubleshootPage):
    """
    This is AppIQ Page class which inherits from TroubleshootPage
    AppIQ implementations are defined here
    """

    def select_source_instance(self, ip_addr):
        """
        This method is to select source instance by ip address
        """
        self.log.info(f"Destination Address: {ip_addr}")
        try:
            self.input_text(self.locator.txaSrc, ip_addr)
            self.input_text(self.locator.txaSrc, Keys.DOWN)
            self.input_text(self.locator.txaSrc, Keys.ENTER)
            self.wait_element_visible(self.locator.txaDest)
        except Exception as e:
            raise Exception("Failed to select source instance: %s" % e)

    def select_destination_instance(self, ip_addr):
        """
        This method is to select source instance by ip address
        """
        self.log.info(f"Source Address: {ip_addr}")
        try:
            self.input_text(self.locator.txaDest, ip_addr)
            self.input_text(self.locator.txaDest, Keys.DOWN)
            self.input_text(self.locator.txaDest, Keys.ENTER)
            self.wait_element_visible(self.locator.btnSubmit)
        except Exception as e:
            raise Exception("Failed to select destination instance: %s" % e)

    def input_port(self, port):
        """
        This method is to input port
        """
        try:
            self.input_text(self.locator.txaPort, port)
            self.wait_element_visible(self.locator.btnSubmit)
        except Exception as e:
            raise Exception("Failed to input port: %s" % e)

    def select_protocol_icmp(self):
        """
        This method is to select protocol ICMP
        """
        try:
            self.click_element(self.locator.txaProtocol)
            self.click_element(self.locator.txaIcmp)
            self.wait_element_visible(self.locator.btnSubmit)
        except Exception as e:
            raise Exception("Failed to select destination instance: %s" % e)

    def click_submit(self):
        """
        This method is to click submit in AppIQ page
        """
        self.log.info("Click Submit")
        try:
            self.click_element(self.locator.btnSubmit)
        except Exception as e:
            raise Exception("Failed to click submit: %s" % e)

    def retrieve_status(self):
        """
        This method is to verify AppIQ page
        """
        self.log.info("Verify AppIQ")
        try:
            self.wait_element_visible(self.locator.imgCanvas, timeout=120)
            status = self.get_elements(self.locator.txtResult)
            return [s.text for s in status]
        except Exception as e:
            raise Exception("Failed to verify appiq page: %s" % e)
        finally:
            self.actionchains().send_keys(Keys.ESCAPE).perform()

    def close_message_box(self):
        """
        This method is to close message box
        """
        if self.is_element_visible(self.locator.btnMessageBoxClose, timeout=5):
            self.click_element(self.locator.btnMessageBoxClose)
            time.sleep(2)
