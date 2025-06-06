KANAKING
========

About
-----
KanaKing (or かなキング) is a free, open-source piece of software dedicated to helping learners master Japanese's syllabary alphabets. It was created by a developer who is an amateur programmer and Japanese learner using Python TKinter, and several rolls of duct tape.

KanaKing aims to reinforce the user's kana reading abilities by giving them examples of real Japanese words and asking them to convert from Japanese script to Romaji. While this association with Romaji may not be ideal long-term, the repeated examples and reading exercises should help learners to build confidence in their reading. It is recommended that users say the words out loud as they use the software. Future versions may include text-to-speech exercises.

KanaKing is a unique piece of software because it tracks your proficiency for each character. Your speed and accuracy are tracked for every word you are shown. If you respond to a word slowly or incorrectly, the score for all of the characters in that word will go up; if you respond quickly and accurately, the score for that word will go down. Characters with the highest scores will appear more often.

KanaKing does not claim to teach you Japanese, or even Kana. The purpose of this software is to reinforce what you have already learned. If you don't know any Kana yet, you should probably make use of a different resource before practicing with KanaKing.

Basic Use
---------
KanaKing is designed to be simple and intuitive to use. You may be surprised at first to see that most of the buttons are labeled in Japanese, but this is simply a stylistic choice - you can see their English translation by hovering over them with a mouse. To begin a new study session, click on "Study" ("べんきょうする") to begin a new study session. You will be directed to a new page, where you can choose your session type (Hiragana, Katakana, or Both) and the number of questions in your session (anywhere between 1 and 200). Once you begin your session, you will be presented with two types of questions: Kana to Romaji, and Romaji to Kana. For the Kana to Romaji exercises, simply select the text box and enter the romaji equivalent of the kana provided. For the Romaji to Kana exercises, a digital kana keyboard will be displayed. Simply click on the characters you want to add to the word. To delete a character or to type a character with a diacritic, use the orange buttons on the navigation bar at the top of the keyboard. When you are finished entering your response, click "Submit" at the bottom right of the screen. After completing all of the questions in the session, your score will be displayed.

If you would like to see your progress on your kana and what characters you're struggling with, you can navigate to the "Stats" page, which shows you your five best Hiragana and Katakana and your five worst Hiragana and Katakana.

If you need to see the answer to a question _before_ submitting your response (such as for debugging purposes), you can enable "Cheat Mode" in Settings.

Installation and Running
------------------------
To install KanaKing, ensure you have a relatively recent version of Python (3.10 or higher is recommended) and that you install all of the dependencies listed in `requirements.txt`. You can install these dependencies in bulk using `python -m pip install -r requirements.txt`. To run the script, make sure you are in the `kanaking` directory (the root directory of the project) and then run `python src/main.py`.

License
-------
The source code for this project is licensed under the MIT license, which means that you are free to create derivatives of this project as long as you include a copy of the license in your work. The data used to generate the word lists, however, is covered by separate licenses determined by the creators of that data. For more information, please consult the LICENSE and THIRD_PARTIES files.
