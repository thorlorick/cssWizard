from bs4 import BeautifulSoup
import os

STYLE_THEMES = {
    "modern": {
        "body": {
            "background-color": "#f9f9f9",
            "font-family": "'Segoe UI', sans-serif",
            "color": "#333",
            "padding": "2rem",
        },
        "h1": {"color": "#2a2a2a"},
        "p": {"line-height": "1.6"},
        "button": {
            "background-color": "#007BFF",
            "color": "white",
            "border": "none",
            "padding": "10px 20px",
            "border-radius": "4px"
        }
    },

    "old school": {
        "body": {
            "background-color": "#fff8dc",
            "font-family": "'Courier New', monospace",
            "color": "#000",
        },
        "h1": {"color": "darkred", "text-decoration": "underline"},
        "p": {"font-style": "italic"},
        "button": {
            "background-color": "gray",
            "color": "white",
            "border": "2px solid black"
        }
    }
}

def generate_css_from_theme(theme_dict):
    css = ""
    for selector, rules in theme_dict.items():
        rule_str = "; ".join(f"{k}: {v}" for k, v in rules.items())
        css += f"{selector} {{ {rule_str}; }}\n"
    return css

def style_html(html_path, style_keyword, output_path="styled_output.html"):
    with open(html_path, "r") as f:
        soup = BeautifulSoup(f, "html.parser")

    theme = STYLE_THEMES.get(style_keyword.lower())
    if not theme:
        raise ValueError(f"No theme found for '{style_keyword}'.")

    css = generate_css_from_theme(theme)

    style_tag = soup.new_tag("style")
    style_tag.string = css
    soup.head.append(style_tag)

    with open(output_path, "w") as f:
        f.write(str(soup))

    print(f"Styled HTML written to {output_path}")

if __name__ == "__main__":
    print("Available styles:")
    for name in STYLE_THEMES.keys():
        print(f"- {name}")

    keyword = input("\nEnter a style keyword: ").strip().lower()

    if keyword not in STYLE_THEMES:
        print(f"❌ Style '{keyword}' not found.")
    else:
        style_html("input.html", keyword)

