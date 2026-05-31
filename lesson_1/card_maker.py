class CardMaker():
    def __init__(self, title: str, type: str, padding: int = 2):
        self.title = title
        self.type = type
        self.padding = padding

    def make(self, data: float) -> str:
        text_data = self._format(data)
        return "\n".join(self._get_lines(text_data))

    def _format(self, data: float) -> str:
        if (self.type == "%"):
            return f"{data*100:.0f}%"
        if (self.type == "$"):
            return f"${data:.2f}"
        return f"{data}"

    def _get_lines(self, text: str):
        width = max(len(self.title), len(text)) + self.padding * 2
        yield f"╔{"═"*width}╗"
        yield f"║{self.title:^{width}}║"
        yield f"║{text:^{width}}║"
        yield f"╚{"═"*width}⁠╝"


def main():
    percent_card_maker = CardMaker("Проценты", "%")
    percent_card = percent_card_maker.make(0.6)
    print(percent_card)

    currency_card_maker = CardMaker("Цена", "$")
    currency_card = currency_card_maker.make(25)
    print(currency_card)


if __name__ == "__main__":
    main()
