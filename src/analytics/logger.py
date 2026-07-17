from pathlib import Path


class RatioLogger:

    def __init__(self):

        self.output = Path("data") / "output"
        self.output.mkdir(parents=True, exist_ok=True)

        self.log_file = self.output / "ratio_validation.log"

    def log(self, message):

        with open(self.log_file, "a", encoding="utf-8") as f:
            f.write(message + "\n")