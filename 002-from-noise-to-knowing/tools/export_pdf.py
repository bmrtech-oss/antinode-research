"""Export the MkDocs print page to a PDF using headless Chromium."""
from pathlib import Path

from playwright.sync_api import sync_playwright


ROOT = Path(__file__).resolve().parents[2]
SITE = ROOT / "_site"
OUTPUT = SITE / "FromNoiseToKnowing.pdf"


def main():
    print_page = SITE / "print_page" / "index.html"
    if not print_page.is_file():
        print_page = SITE / "print_page.html"
    if not print_page.is_file():
        raise FileNotFoundError(f"MkDocs print page not found under {SITE}")

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        try:
            page = browser.new_page()
            page.goto(print_page.resolve().as_uri(), wait_until="networkidle")
            page.emulate_media(media="print")
            page.evaluate("document.documentElement.dataset.theme = 'light'")
            page.evaluate("document.fonts.ready")
            page.pdf(
                path=str(OUTPUT),
                format="A4",
                print_background=True,
                display_header_footer=True,
                header_template=(
                    '<div style="width:100%;margin:0 18mm;font:8px sans-serif;'
                    'color:#666">From Noise to Knowing</div>'
                ),
                footer_template=(
                    '<div style="width:100%;margin:0 18mm;text-align:right;'
                    'font:8px sans-serif;color:#666">'
                    '<span class="pageNumber"></span></div>'
                ),
                margin={
                    "top": "18mm",
                    "right": "18mm",
                    "bottom": "18mm",
                    "left": "18mm",
                },
            )
        finally:
            browser.close()

    if not OUTPUT.is_file() or OUTPUT.stat().st_size == 0:
        raise RuntimeError(f"PDF export failed to create {OUTPUT}")
    print(f"Created {OUTPUT} ({OUTPUT.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
