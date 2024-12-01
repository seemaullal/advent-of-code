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

For convenience, I recommend adding a function to your `.zshrc` or `.bashrc` file so the command `aoc` will call the script and can be run from any directory:

```bash
aoc() {
 day=$(printf %02d $1)
  if [ -n "$2" ]
  then
    year=$2
  else
    year=$(date +'%Y')
  fi
  base_dir=~/Developer/advent-of-code
  cd $base_dir
  python3 aoc.py $1 $2
  code . -g $year/$day/$day.py
  cd $base_dir/$year/$day
}
```

You can replace the `~/Developer/advent-of-code` directory and `code` with wherever you want to run the script from and how you want to open the editor. Then, run the command `aoc` with the day number and optionally the year:

```bash
aoc 1
aoc 4 2021
aoc 04 2022 # leading 0 is optional
```
