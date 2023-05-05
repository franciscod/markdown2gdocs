"""sample generated markdown"""

import datetime


def gen_md():
    now = datetime.datetime.now().strftime("%y-%m-%d %H:%M")
    return f"""last updated at: {now}
# Heading 1
## Heading 2 A
foo
## Heading 2 B
bar"""


if __name__ == "__main__":
    print(gen_md())
