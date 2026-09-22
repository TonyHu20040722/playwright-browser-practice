"""A minimal browser check against HTML created in memory."""

from playwright.sync_api import sync_playwright


def main():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(channel="chrome", headless=True)
        try:
            page = browser.new_page()
            page.set_content(
                '<button onclick="this.textContent=\'Ready\'">Start</button>'
            )
            page.get_by_role("button", name="Start").click()
            observed = page.get_by_role("button").inner_text()
            assert observed == "Ready", observed
            print("Observed:", observed)
        finally:
            browser.close()


if __name__ == "__main__":
    main()
