Feature: Audible Requirements
from Alexa app <https://www.howtogeek.com/253209/how-to-listen-to-audiobooks-on-the-amazon-echo/>:
"""
"Alexa, play the book [title]."
"Alexa, play the Audiobook [title]."
"Alexa, play [title] from Audible."

"Alexa, pause."
"Alexa, resume."
"Alexa, go back." (This will rewind the audiobook by one paragraph.)
"Alexa, go forward." (This will fast forward the audiobook by one paragraph.)

"Alexa, next chapter."
"Alexa, previous chapter."
"Alexa, go to chapter number (#)."
"Alexa, go to last chapter."
"""

Scenario Outline: Letting Mycroft know you want to use Audible
 Given "Mycroft" has been linked to an "Audible account"
   And that account contains the book "The Art of War"
  When "Mycroft" is given the instruction: <Instruction>
  Then "The Art of War" is played
 Examples:
 | Play the book "The Art of War"      |
 | Play the Audiobook "The Art of War" |
 | Play "The Art of War" from Audible  |

Scenario: Pausing and resuming
 Given "Mycroft" is playing "The Art of War"
  When "Mycroft" is given the instruction: "Pause"
  Then "The Art of War" stops playing
  When "Mycroft" is given the instruction: "Resume"
  Then "The Art of War" is played

Scenario Outline: Jumping chapters
 Given "Mycroft" is playing "The Art of War" on Chapter "2"
  When "Mycroft" is given the instruction: "<Direction> chapter"
  Then "The Art of War" is played from Chapter <ChapterNumber>
 Examples: 
 | Direction | ChapterNumber |
 | Next      | 3             |
 | Previous  | 1             |

Scenario: Going to a chapter
 Given "Mycroft" is playing "The Art of War"
  When "Mycroft" is given the instruction: "Go to chapter number 7"
  Then "The Art of War" is played from Chapter "7"

Scenario Outline: title
 Given "Mycroft" is playing "The Art of War"
  When "Mycroft" is given the instruction: "Go <Direction>"
  Then the playback goes <Direction> ~30 seconds
 Examples: 
 | Direction |
 | back      |
 | forward   |
 