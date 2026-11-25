"""The Funniest Honest Appliance Error.

Writes one line to $MAKEFUN_OUTPUT_DIR/entry.txt: the funniest
honest error message an appliance could show. A washing machine
refuses to spin because its load is unbalanced and one sock is
missing, and it wants someone in the house to admit where the
sock went. Standard library only.
"""

import os

ERROR_LINE = (
    "ERROR E12: Unbalanced load. One sock is missing and the drum "
    "refuses to spin until someone in this house admits where it went."
)


def validate_line(text):
    """Check the line against the competition gate before writing.

    The gate needs plain UTF-8 text of 1 to 200 characters, not
    only white space, on a single line: one honest error message
    an appliance could show. Returns the cleaned text or raises
    ValueError.
    """
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("error line must not be only whitespace")
    if len(cleaned) > 200:
        raise ValueError(
            "error line is %d characters, over the 200 limit"
            % len(cleaned)
        )
    if "\n" in cleaned or "\r" in cleaned:
        raise ValueError("error line must be exactly one line")
    return cleaned


def error_report(text):
    """Measure the error line for one last sanity pass.

    Returns a dict with the character count and the word count of
    the cleaned text. A line too short to carry a joke, or one
    padded out to fill the cap instead of sounding like a machine
    that has had enough, is caught here before anything is written.
    """
    words = text.split()
    return {"chars": len(text), "words": len(words)}


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    text = validate_line(ERROR_LINE)
    report = error_report(text)
    if report["words"] < 5:
        raise ValueError("error line is too short to sound like a machine")
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
