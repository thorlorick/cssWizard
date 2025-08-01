from bs4 import BeautifulSoup
import os

THEME_DIR = "themes"
AVAILABLE_THEMES = {
    "modern": "modern.css",
    "old school": "old_school.css",
    "minimalist": "minimalist.css",
    "brutalist": "brutalist.css",
    "cyberpunk": "cyberpunk.css",
    "print-friendly": "print_friendly.css"
}


def clean_existing_css(soup):
    for style_tag in soup.find_all("style"):
        style_tag.decompose()
    for link_tag in soup.find_all("link", rel="stylesheet"):
        link_tag.decompose()


def inject_external_css(soup, css_filename):
    if not soup.head:
        head = soup.new_tag("head")
        soup.insert(0, head)
    else:
        head = soup.head

    link_tag = soup.new_tag("link", rel="stylesheet", href=f"{THEME_DIR}/{css_filename}")
    head.append(link_tag)


def style_html(input_file, theme_key, output_file="styled_output.html"):
    css_file = AVAILABLE_THEMES.get(theme_key)
    if not css_file:
        raise ValueError(f"❌ Theme '{theme_key}' not found.")

    with open(input_file, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")

    clean_existing_css(soup)
    inject_external_css(soup, css_file)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(str(soup))

    print(f"✅ Applied theme '{theme_key}' -> {output_file}")


if __name__ == "__main__":
    print("Available themes:")
    for theme in AVAILABLE_THEMES:
        print(f"- {theme}")

    selected = input("\nEnter a theme: ").strip().lower()

    if selected not in AVAILABLE_THEMES:
        print(f"❌ Theme '{selected}' not found.")
    else:
        style_html("input.html", selected)
