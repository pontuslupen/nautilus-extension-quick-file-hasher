import unittest
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]


class ReadmeTaglineTests(unittest.TestCase):
    def test_tagline_is_centered_emphasized_and_ends_with_exclamation_mark(self):
        readme_lines = (REPOSITORY_ROOT / "README.md").read_text(
            encoding="utf-8"
        ).splitlines()

        tagline_lines = [
            line.strip()
            for line in readme_lines
            if "Verify your files with speed and confidence" in line
        ]

        self.assertEqual(
            tagline_lines,
            [
                '<p align="center"><em>Verify your files with speed and confidence!'
                "</em></p>"
            ],
        )


if __name__ == "__main__":
    unittest.main()
