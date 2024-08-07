# Module: main
# Description:
# This module provides a main menu to interact with OpenAI services
# -----------------------------------------------------------------------------

from src import Config, OpenAIInterfaceFT


def main_heliostuner():
    config = Config()

    app = OpenAIInterfaceFT(config)
    app.mainloop()


if __name__ == "__main__":
    main_heliostuner()
