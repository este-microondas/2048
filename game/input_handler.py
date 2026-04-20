import msvcrt


class InputHandler:
    def get_input(self):
        while True:
            key = msvcrt.getch()

            if key in (b"w", b"W"):
                return "up"
            if key in (b"s", b"S"):
                return "down"
            if key in (b"a", b"A"):
                return "left"
            if key in (b"d", b"D"):
                return "right"
            if key in (b"q", b"Q"):
                return "quit"