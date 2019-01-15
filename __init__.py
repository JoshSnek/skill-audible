"""
The MIT License (MIT)	

Copyright (c) 2019 JoshSnek

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
# If you use an external library, be sure to include it
# in the requirements.txt file so the library is installed properly
# when the skill gets installed later by a user.

#from amazon.api import AmazonAPI

from mycroft.skills.core import MycroftSkill, intent_handler, intent_file_handler
from mycroft.util.log import LOG
from adapt.intent import IntentBuilder

# Each skill is contained within its own class, which inherits base methods
# from the MycroftSkill class.  You extend this class as shown below.

# TODO: Change "Template" to a unique name for your skill
class AudibleSkill(MycroftSkill):
    def __init__(self):
        super(AudibleSkill, self).__init__(name="AudibleSkill")
        # Initialize working variables used within the skill.

    @intent_file_handler('launchwith.intent')
    def handle_launch_audible_intent(self, message):
        # Mycroft will randomly speak one of the lines from the file
        #    dialogs/en-us/launchmessage.dialog
        self.book_name = message.data["bookname"]
        self.speak_dialog("launchmessage")
"""
    @intent_handler(IntentBuilder("").require("Audible").require("Play"))
    def handle_launch_audible_intent(self, message):
        # Mycroft will randomly speak one of the lines from the file
        #    dialogs/en-us/launchmessage.dialog
        self.book_name = message.data["bookname"]
        self.speak_dialog("launchmessage")
"""
    # The "stop" method defines what Mycroft does when told to stop during
    # the skill's execution. In this case, since the skill's functionality
    # is extremely simple, there is no need to override it.  If you DO
    # need to implement stop, you should return True to indicate you handled
    # it.
    #
    # def stop(self):
    #    return False

# The "create_skill()" method is used to create an instance of the skill.
# Note that it's outside the class itself.
def create_skill():
    return AudibleSkill()
