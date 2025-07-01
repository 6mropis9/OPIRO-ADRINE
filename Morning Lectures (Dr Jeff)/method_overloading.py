class Printer:
    def print_content(self, content=None):
        if isinstance(content, str):
            print(f"Printing document: {content}")
        elif isinstance(content, int):
            print(f"Printing {content} copies of the document")
        elif content is None:
            print("Printing default test page...")
        else:
            print("Unsupported content type")

# Test
printer = Printer()
printer.print_content("Invoice")     # Output: Printing document: Invoice
printer.print_content(3)            # Output: Printing 3 copies of the document
printer.print_content()             # Output: Printing default test page...