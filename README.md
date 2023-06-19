# Replacer CLI

Finds and replaces all instances of a string found throughout a given
directory.

Note that you must pass the full Python executable path as the first argument
in the CLI commands, as the Replacer CLI performs its search and replace
operations in the current working directory.

## Prepare the CLI

Execute the following commands to prepare the Replacer CLI:

1. Clone the Replacer CLI repository:

   `git clone https://github.com/pauljwil/replacer-cli`

2. Navigate to the directory where you want to search for or replace a string
   of text:

   `cd <path/to/target/directory>`

## Count string instances

Count the number of times that a string appears in the current directory:

`python3 <path>/replacer-cli/replacer/__main__.py --find <text-to-search>`

## Replace string instances

Find and replace all instances of a string throughout the current directory:

`python3 <path>/replacer-cli/replacer/__main__.py --replace <text-to-search> <replacement-text>`

Example:

`python3 <path>/replacer-cli/replacer/__main__.py --replace Python snake`

Finds every instance of "Python" in the current directory and replaces it with
"snake".

## CLI flags

| CLI flag | Description | Arguments |
| --- | --- | --- |
| --find, -f | Count the number of times that a string appears in the current directory. | `<text-to-search>` |
| --replace, -r | Find every instance of a string in the current directory and replace it with a new string. | `<text-to-search>` `<replacement-text>` |
| --version, -v | Display the current Replacer CLI version number. | None |