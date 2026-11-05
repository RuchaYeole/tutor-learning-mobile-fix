import unittest

from tutorlearningmobilefix.plugin import MOBILE_FIX_CSS


class TestMobileFixCSS(unittest.TestCase):

    def test_mobile_breakpoint_exists(self):
        self.assertIn("@media screen and (max-width: 767px)", MOBILE_FIX_CSS)

    def test_tablet_breakpoint_exists(self):
        self.assertIn(
            "@media screen and (min-width: 768px) and (max-width: 1199px)",
            MOBILE_FIX_CSS,
        )

    def test_horizontal_overflow_is_prevented(self):
        self.assertIn("overflow-x: hidden", MOBILE_FIX_CSS)

    def test_course_content_is_responsive(self):
        self.assertIn(".sequence-container", MOBILE_FIX_CSS)
        self.assertIn("flex-direction: column", MOBILE_FIX_CSS)

    def test_embedded_media_is_responsive(self):
        self.assertIn("iframe", MOBILE_FIX_CSS)
        self.assertIn("max-width: 100%", MOBILE_FIX_CSS)


if __name__ == "__main__":
    unittest.main()
