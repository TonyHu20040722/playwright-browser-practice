# Playwright Browser Practice

## Problem

A browser click can succeed while the intended result fails. These exercises make the goal, action, observed result, and checkpoint visible in a small example.

## Data

Each script creates synthetic HTML in memory with `page.set_content()`. There is no dataset, account, or real website.

## What I Built

- `button_state_demo.py` clicks a `Start` button and verifies that its label becomes `Ready`.
- `locator_and_checkpoint_exercises.py` runs four fixed exercises: the successful check, two deliberate `Waiting` outcomes that fail the `Ready` goal, and a two-button case that exposes an ambiguous locator before reading the intended button by test ID.
- `LEARNING_LOG.md` explains the reasoning and the limits of these checks.

The practice exercises and explanations were completed by Tony. AI assistance helped organize them into this standalone repository and edit the presentation; the browser behavior and scope are described from the code and local run.

## Methods

The scripts use Playwright's synchronous Python API to launch Chrome headlessly, set HTML content, locate and click buttons, read their text, and compare observed text with the goal. The runner catches only the expected `AssertionError: Waiting` in the two deliberate failure exercises. An unexpected error still stops the run.

## Validation

On 2026-09-22, the scripts were run locally with Python 3.12, Playwright 1.55.0, and installed Google Chrome. `button_state_demo.py` exited successfully and printed `Observed: Ready`. `locator_and_checkpoint_exercises.py` exited successfully: both `Ready` checks passed; H1 and H3 printed the expected `Waiting` checkpoint failures; H2 printed the expected strict-mode locator error, then verified the corrected `Ready` read. Both files also passed Python compilation. This is a report of one local run, not a claim of broad compatibility.

## Results

The exercises show that a completed click is different from a passed goal check. They also show that a locator matching two elements needs a more specific target. The two `Waiting` outcomes are intentionally unsuccessful goals, even though the exercise runner finishes successfully.

## Repository Structure

```text
button_state_demo.py                 Minimal successful button check
locator_and_checkpoint_exercises.py Four fixed exercises and expected-failure runner
LEARNING_LOG.md  Reasoning, observations, and limits
requirements.txt Python dependency
```

## How to Reproduce

Use Python 3 and Google Chrome. From this directory:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python button_state_demo.py
.venv/bin/python locator_and_checkpoint_exercises.py
```

The scripts launch Chrome headlessly. If Chrome is unavailable, follow the [Playwright Python installation instructions](https://playwright.dev/python/docs/intro) for a Playwright Chromium browser and change `channel="chrome"` in both scripts to the default Chromium launch. Browser installation was not part of this project's local check.

## Limitations and Next Steps

These fixed actions use synthetic pages. They do not visit a real site, use an application API, authenticate, save a document, retry failed actions, or call an AI model. This is browser automation practice, not an autonomous agent. A useful next exercise would test duplicate button labels and reversed button order without relying on element position; that variation has not been implemented here.
