import unittest

from display.fbtft import Display

class FBTFTDisplayMethods(unittest.TestCase):

    def setUp(self):
        self.display = Display()

    def test_enable_backlight(self):
        self.display.backlight = True;
        self.assertTrue(self.display.backlight)

    def test_disable_backlight(self):
        self.display.backlight = False;
        self.assertFalse(self.display.backlight)

if __name__ == '__main__':
    unittest.main()
