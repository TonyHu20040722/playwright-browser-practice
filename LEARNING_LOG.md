# Learning Log

## 2026-09-22 — Week 5

**Learned:** A completed click, the resulting page state, and a passed goal check are separate. A role-only locator can be ambiguous when multiple elements share the role.

**Built:** A small Playwright demonstration and four fixed exercises using synthetic HTML. The practice exercises and their reasoning were Tony's work; AI assistance helped package and edit this repository.

**Verified:** In one local run with Python 3.12, Playwright 1.55.0, and installed Chrome, the simple demo printed `Observed: Ready`. The exercise runner passed the original and corrected-locator checks, caught the two deliberate `Waiting` failures, and observed the expected strict-mode error.

**Evidence:** `button_state_demo.py` and `locator_and_checkpoint_exercises.py` exited with code 0 on 2026-09-22. Python compilation passed for both files. The output included `Checkpoint passed: False` for H3 and `strict mode violation` for H2.

**What I Can Explain Now:** Why an action can succeed while a goal fails; why `get_by_role("button")` becomes ambiguous with two buttons; why a stable test ID can identify the intended button after its text changes; and why expected failures must be named accurately.

**Next Milestone:** Add duplicate-label and reversed-order variations, then verify that the locator still selects the intended button. This is proposed work, not a completed check.

## Goal and checkpoint

The goal is for the intended button to display `Ready` after a click. The checkpoint reads the browser's current button text and compares it with that goal. A click can complete while the goal still fails.

## Exercises

1. **Original demonstration:** one `Start` button changes to `Ready`; the assertion checks the observed result.
2. **H1, changed result:** the button changes to `Waiting`, while the goal remains `Ready`. The runner catches only the expected `AssertionError: Waiting`. Changing the assertion to `Waiting` would change the goal.
3. **H2, two buttons:** a role-only read matches both buttons and produces an expected Playwright strict-mode error. A unique test ID reads the intended button after its visible label changes. The other button remains `Enter`.
4. **H3, failure evidence:** the script prints the goal, before state, proposed fixed action, completed click, after state, and failed checkpoint. The proposed action is written in code; it is not an AI model response.

## What I learned

- A locator finds elements; it does not change their text. The button's JavaScript changes the label after the click.
- `page.set_content()` replaces the page contents. Both buttons in H2 belong in one HTML string.
- A completed action, an observed state, and a passed goal check are separate pieces of evidence.
- A failed assertion interrupts normal execution. Print observations before the assertion when investigating a failure.
- A role and exact name may still match multiple identical buttons. Stable IDs or a scoped section can identify the target.
- If the goal were to save a document, clicking Save would need a different checkpoint: reopen the intended document and compare its saved contents. This project does not perform that workflow.
- An attempt limit or time limit only explains when to stop. Success still needs a positive check. These scripts have no retry loop.

## Limits

The examples use in-memory HTML and hard-coded actions. They do not test a real website or application API, browser navigation, authentication, AI decision making, or broad reliability. The duplicate-label and reversed-button-order variations discussed during practice remain ideas, not implemented checks here.
