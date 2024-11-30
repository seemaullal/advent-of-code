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

Once this variable is exported, you can use the following command to download the input (this assumes you have ruby installed, ideally the version in `.ruby-version`):

```console
ruby gi.rb 04
```

The above will download the input for day 4 of the current year, create some starter code, and open the problem in your browser (opening the browser currently will only work in MacOS). To specify a different year, you can include it as a second argument:

```console
ruby gi.rb 4 2021
```

This will download the input and set up the initial files for day 4 of 2021 instead of the current year.
