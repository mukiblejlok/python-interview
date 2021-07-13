"""
Question

Find the bug in generate_report implementation.

When you run the __main__ you will see that the Reports 1, 2, 4 are same and somehow combined,
while the Report 3 looks OK.
Why it's so?
How to fix it?

"""
from typing import List, Sequence

DEFAULT_TEMPLATE = ("First Page", "TOC")


def generate_report(results: int, template: Sequence[str] = DEFAULT_TEMPLATE) -> List[str]:
    # Start from provided template
    report = list(template)
    # Add introduction
    report.append("Introduction")
    # Add analysis results
    report.append(f"Analysis results: {results}")
    # Add Summary
    report.append("Summary")

    return report


if __name__ == '__main__':
    # First report with default template
    report1 = generate_report(results=1)

    # Second report with default template
    report2 = generate_report(results=2)

    # Report with custom template
    report3 = generate_report(results=3, template=["New First Page", "Slim - TOC"])

    # Third report with default template
    report4 = generate_report(results=4)

    # Print results
    print(report1)
    print(report2)
    print(report3)
    print(report4)
