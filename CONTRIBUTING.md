CONTRIBUTING
============
KanaKing is a side project, and while I'll occasionally release some bug fixes or optimizations, I won't personally develop very many updates. For this reason, support from the open-source community is very much appreciated. In particular, here are some issues that could use your help:

- Some sections of code are fairly messy. I've done my best to be clear and to abstract using functions and classes, but there are admittedly several places that could use a little cleaning up, especially in `src/graphic_utils.py` and `src/main.py`
- Currently, KanaKing only supports Waapuro romaji. While this is a useful default and should be fine with most users, support for Hepburn would be beneficial to make KanaKing a little more well-rounded.
- The wordlists could still be larger.
- The software could be better packaged.
- The score evaluating system is somewhat flawed for incorrect answers because it will grade all of the characters in a word as wrong even if some of them are correct.
- Lots of improvements to the software's accessibility should be made, such as translating the English text into other languages. However, this may be best accomplished by creating forks rather than editing the original copy.
- I didn't write very many unit tests and I'm still not entirely sure what else to test, so some more comprehensive testing would be great.

Guidelines for Contribution
---------------------------
While any help you are able to give is much appreciated, your contributions will be more likely to be merged into the main copy if you adhere to the following guidelines.

1. **Adhere to standard Python convention as described in PEP 8.** I won't be super nitpicky about this, but I'd much prefer if you stuck to `snake_case` for variables and functions, `UPPER_CASE` for constants, and `PascalCase` for classes. This will make styling more consistent and will make it easier to reference things in the future. In short, if Pylint is yelling at you, consider changing your code to please it. :)
2. **Don't change the main function and purpose of the software.** Adding new features and improving old ones is both acceptable and encouraged, but if you want to make changes to the fundamental structure or methods of the software, such as changing the way it determines which kana to focus on or the types of exercises, you may want to make your own derivative rather than trying to change the original copy.
3. **Keep in mind that this software is for use by a general audience in an educational setting** This applies especially to editing the word list. Try to avoid including vocabulary words that are offensive either in Japanese or English, especially words that are profane, suggestive, excessively violent, insensitive, derogatory, crude, or otherwise likely to offend a significant number of users. As these word lists were algorithmically generated using an automated scraper, it's quite possible that there are already some offensive words that human supervision has overlooked. If you happen to find one, please make note of it so that it can be removed.
