#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import datetime
import sys

# Change CWD to the script's own director.
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

# language code are in ISO 639-2
# https://en.wikipedia.org/wiki/List_of_ISO_639-2_codes
lang_files_dir = "translations/"
langs = [{"code": "deu", "name": "German"}, {"code": "fra", "name": "French"},
         {"code": "hrv", "name": "Croatian"}, {"code": "ind", "name": "Indonesian"},
         {"code": "ita", "name": "Italian"}, {"code": "lit", "name": "Lithuanian"}, {"code": "msa", "name": "Malay"},
         {"code": "meme", "name": "Meme-nglish"}, {"code": "pol", "name": "Polish"},
         {"code": "por", "name": "Portuguese"}, {"code": "rus", "name": "Russian"},
         {"code": "spa", "name": "Spanish"}, {"code": "tur", "name": "Turkish"},
         {"code": "ukr", "name": "Ukrainian"}]
lang_stats = {}

# Generate the stats
for lang in langs:
    lang_code = lang["code"]
    lang_file = lang_files_dir + lang_code + ".po"
    message_count = 0.0
    missing_translations = 0.0
    with open(lang_file, 'r', encoding="utf8") as f:
        for line in f:
            if line.startswith("msgstr"):
                message_count += 1
            if line == "msgstr \"\"\n":
                missing_translations += 1
    lang_stats[lang_code] = {"total": message_count,
                             "missing": missing_translations}
    f.close()

# Write the README
readme_file = "README.md"
with open(readme_file, 'w', encoding="utf8", newline='\n') as f:
    f.write("[//]: # \"This file is automatically generated by " +
            os.path.basename(__file__) + "\"\n")
    f.write("# ppl-i18n\n")
    f.write("This repository contains the translated strings for the game [PewPew Live](https://pewpew.live).\n")
    f.write("## Contributing\n")
    f.write("Any contribution helps, even if its only a few words or phrases.\n")
    f.write("(but please only contribute to languages you can speak; no Google Translate)\n")
    f.write("\n")
    f.write("For information on how to submit changes on GitHub, take a look at this [guide](https://docs.github.com/en/free-pro-team@latest/github/managing-files-in-a-repository/editing-files-in-another-users-repository).\n")
    f.write("\n")
    f.write("If you contribute a significant amount, I'll put you in the credits!\n")
    f.write("\n")
    f.write("A few tips for contributing:\n")
    f.write("* Keep the `%s` as they later get replaced by some other text.\n")
    f.write("* Try to have the translations be approximately the same length as the English text.\n")
    f.write("* Don't hesitate the reword the text to better fit the language.\n")
    f.write("* In order to reduce merge conflicts, avoid working on a single pull request for multiple days. It's better if you create one pull request per day.\n")
    f.write("## Adding new languages\n")
    f.write("If you want to add support for a new language, create a GitHub Issue so that we can discuss\n")
    f.write("the feasibility.\n")
    f.write("## Status\n")
    for lang in langs:
        lang_code = lang["code"]
        lang_name = lang["name"]
        stats = lang_stats[lang_code]
        percentage = stats["missing"] / stats["total"]
        percentage = int(100 - percentage * 100)
        comment = " (" + str(percentage) + "% complete; " + \
            str(int(stats["missing"])) + " remaining)"
        if stats["missing"] == 0:
            comment = " (100% complete! 🎉)"
        lang_link = "[" + lang_name + "](/translations/" + lang_code + ".po)"
        f.write("* " + lang_link + comment + "\n")

    date = datetime.datetime.utcnow()
    date_str = date.strftime("%b %d %Y %H:%M:%S")
    f.write("> Report generated on " + date_str + " UTC")
