"""Fixed Playwright exercises, including deliberately failed checkpoints."""

from playwright.sync_api import Error as PlaywrightError
from playwright.sync_api import sync_playwright


def original_demo(page):
    page.set_content('<button onclick="this.textContent=\'Ready\'">Start</button>')
    page.get_by_role("button", name="Start", exact=True).click()
    observed = page.get_by_role("button").inner_text()
    assert observed == "Ready", observed
    print("Observed:", observed)


def changed_result(page):
    page.set_content('<button onclick="this.textContent=\'Waiting\'">Start</button>')
    page.get_by_role("button", name="Start", exact=True).click()
    observed = page.get_by_role("button").inner_text()
    print("Goal: Ready")
    print("Observed:", observed)
    assert observed == "Ready", observed


def two_buttons(page):
    page.set_content("""
        <button data-testid="result-button"
                onclick="this.textContent='Ready'">Start</button>
        <button data-testid="other-button">Enter</button>
    """)
    print("Number of buttons:", page.get_by_role("button").count())
    page.get_by_role("button", name="Start", exact=True).click()

    try:
        page.get_by_role("button").inner_text()
    except PlaywrightError as error:
        if "strict mode violation" not in str(error).lower():
            raise
        print("Expected locator error:", str(error).splitlines()[0])
    else:
        raise AssertionError("The two-button read should be ambiguous.")

    observed = page.get_by_test_id("result-button").inner_text()
    other_text = page.get_by_test_id("other-button").inner_text()
    assert observed == "Ready", observed
    assert other_text == "Enter", other_text
    print("Corrected locator:", observed)


def failure_evidence(page):
    page.set_content('<button onclick="this.textContent=\'Waiting\'">Start</button>')
    goal = "Ready"
    before = page.get_by_role("button").inner_text()
    proposed_action = "Click the Start button."
    print("Goal:", goal)
    print("Before:", before)
    print("Proposed action:", proposed_action)
    page.get_by_role("button", name="Start", exact=True).click()
    print("Executed action: the click completed.")
    observed = page.get_by_role("button").inner_text()
    print("After:", observed)
    print("Checkpoint passed:", observed == goal)
    assert observed == goal, observed


def run_exercise(page, title, exercise, expected_failure=None):
    print("\n" + title)
    try:
        exercise(page)
    except AssertionError as error:
        if expected_failure is None or str(error) != expected_failure:
            raise
        print("Expected checkpoint failure:", f"AssertionError: {error}")
    else:
        if expected_failure is not None:
            raise AssertionError("The expected checkpoint failure did not occur.")


def main():
    if not __debug__:
        raise RuntimeError("Run normally, without Python's -O option.")

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(channel="chrome", headless=True)
        try:
            page = browser.new_page()
            page.set_default_timeout(5000)
            run_exercise(page, "Original demonstration", original_demo)
            run_exercise(page, "H1: Changed result", changed_result, "Waiting")
            run_exercise(page, "H2: Two buttons", two_buttons)
            run_exercise(page, "H3: Failed-run evidence", failure_evidence, "Waiting")
        finally:
            browser.close()

    print("\nFinished: both Ready checks passed; both Waiting failures were expected.")


if __name__ == "__main__":
    main()
