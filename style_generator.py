from bs4 import BeautifulSoup

STYLE_THEMES = {
    "modern": """
        body {
            font-family: 'Segoe UI', sans-serif;
            background-color: #f0f2f5;
            color: #333;
            margin: 2em;
        }
        h1, h2, h3 {
            color: #2a7ae2;
        }
        a {
            color: #007bff;
        }
    """,

    "old school": """
        body {
            font-family: 'Times New Roman', serif;
            background-color: #fffff0;
            color: #000;
            margin: 2em;
        }
        h1, h2, h3 {
            color: #800000;
        }
        a {
            color: #000080;
        }
    """,

    "minimalist": """
        body {
            font-family: Arial, sans-serif;
            background: white;
            color: #111;
            padding: 2rem;
            max-width: 700px;
            margin: auto;
        }
        h1, h2, h3 {
            border-bottom: 1px solid #eee;
        }
        a {
            color: black;
            text-decoration: underline;
        }
    """,

    "brutalist": """
        body {
            font-family: monospace;
            background: #fff;
            color: #000;
            padding: 2rem;
        }
        h1, h2, h3 {
            background: #000;
            color: #fff;
            padding: 0.5rem;
        }
        a {
            color: #f00;
        }
    """,

    "cyberpunk": """
        body {
            font-family: 'Orbitron', sans-serif;
            background-color: #0f0f2f;
            color: #f0f;
            padding: 2rem;
        }
        h1, h2, h3 {
            color: #0ff;
        }
        a {
            color: #ff0;
        }
    """,

    "print-friendly": """
        body {
            font-family: Georgia, serif;
            background: white;
            color: black;
            margin: 1in;
        }
        a {
            color: black;
            text-decoration: underline;
        }
    """
}


def style_html(input_file: str, style_keyword: str, output_file: str = "styled_output.html"):
    with open(input_file, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")

    style = STYLE_THEMES.get(style_keyword.lower())
    if not style:
        raise ValueError(f"Style '{style_keyword}' not found.")

    style_tag = soup.new_tag("style")
    style_tag.string = style

    if soup.head:
        soup.head.append(style_tag)
    else:
        head = soup.new_tag("head")
        head.append(style_tag)
        soup.insert(0, head)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(str(soup))

    print(f"✅ Styled HTML written to: {output_file}")


if __name__ == "__main__":
    print("Available styles:")
    for style in STYLE_THEMES.keys():
        print(f"- {style}")

    keyword = input("\nEnter a style keyword: ").strip().lower()

    if keyword not in STYLE_THEMES:
        print(f"❌ Style '{keyword}' not found.")
    else:
        style_html("input.html", keyword)


