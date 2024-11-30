Solutions to [Advent of Code problems](https://adventofcode.com/)

## Downloading Input

In order for the download input script to work, you must provide your Advent of Code session cookie
to the program in an environment variable (you can place this in your .zshrc or .bashrc file; the
cookie should be valid for about a month):

```console
export AOC_SESSION=your_cookie
```

To obtain the cookie, sign into Advent of Code through your browser, then use the
developer tools to examine the cookies. For example, in Chrome, this will be under the Application
tab of the developer tools. Here, there will be a value under "session" that should be a long
value of characters and numbers. This is the value you will want to copy and replace "your_cookie" in
the above example with.

Once this variable is exported, you can use either the ruby or python input scripts to download the input and create correct directory structure.

For convenience, I would recommend adding a function to your `.zshrc` or `.bashrc` file so the command `aoc` will call the script and can be run from any directory:

```bash
aoc() {
  cd ~/Developer/p/advent-of-code && python3 aoc.py $1 $2 && code .
}
```

You can replace the directory and `code` with wherever you want to run the script from and how you want to open the editor. Then, run the command `aoc` with the day number and optionally the year:

```bash
aoc 01
aoc 04 2021
```
