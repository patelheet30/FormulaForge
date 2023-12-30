class URLBuilder:
    def __init__(self, base_url: str) -> None:
        self.base_url = base_url

    def __call__(self, *args, **kwargs) -> str:
        """Builds the URL with the given arguments.
        The first argument is added with ? while the rest are added with &.
        """
        url = self.base_url
        if args:
            url += f"/{args[0]}"
        if kwargs:
            url += "?"
            for key, value in kwargs.items():
                url += f"{key}={value}&"
            url = url[:-1]

        return url


def convert_new_line_to_url_encoding(formula_without_newline_encoding: str) -> str:
    """Converts \n to %0A"""
    return formula_without_newline_encoding.replace("\n", "%0A")