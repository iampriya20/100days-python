# Day 99: Browser History Simulator (Two Stacks)

class Browser:
    def __init__(self, homepage: str = "about:blank"):
        self.back_stack = []
        self.forward_stack = []
        self.current = homepage

    def visit(self, url: str):
        self.back_stack.append(self.current)
        self.current = url
        self.forward_stack.clear()
        print(f"Visited: {self.current}")

    def back(self):
        if not self.back_stack:
            print("No pages in Back history.")
            return
        self.forward_stack.append(self.current)
        self.current = self.back_stack.pop()
        print(f"Back -> {self.current}")

    def forward(self):
        if not self.forward_stack:
            print("No pages in Forward history.")
            return
        self.back_stack.append(self.current)
        self.current = self.forward_stack.pop()
        print(f"Forward -> {self.current}")

    def show(self):
        print("\n=== Browser State ===")
        print("Back   :", self.back_stack)
        print("Current:", self.current)
        print("Forward:", list(reversed(self.forward_stack)))  # top on right
        print("=====================\n")


def menu():
    print("Commands:")
    print("  v <url>  - visit url")
    print("  b        - back")
    print("  f        - forward")
    print("  s        - show")
    print("  q        - quit")
    print()

if __name__ == "__main__":
    browser = Browser("home")
    menu()
    while True:
        cmd = input("> ").strip()
        if not cmd:
            continue
        if cmd == "q":
            break
        elif cmd == "s":
            browser.show()
        elif cmd == "b":
            browser.back()
        elif cmd == "f":
            browser.forward()
        elif cmd.startswith("v "):
            _, url = cmd.split(" ", 1)
            browser.visit(url.strip())
        else:
            print("Unknown command. Try again.")
