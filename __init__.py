# TODO: Add an appropriate license to your skill before publishing.  See
# the LICENSE file for more information.

# Below is the list of outside modules you'll be using in your skill.
# They might be built-in to Python, from mycroft-core or from external
# libraries.  If you use an external library, be sure to include it
# in the requirements.txt file so the library is installed properly
# when the skill gets installed later by a user.

from amazon.api import AmazonAPI

from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import LOG
from adapt.intent import IntentBuilder

# Each skill is contained within its own class, which inherits base methods
# from the MycroftSkill class.  You extend this class as shown below.

# TODO: Change "Template" to a unique name for your skill
class AudibleSkill(MycroftSkill):

    # The constructor of the skill, which calls MycroftSkill's constructor
    def __init__(self):
        super(AudibleSkill, self).__init__(name="AudibleSkill")
        # Initialize working variables used within the skill.
        self.count = 0

    @intent_handler(IntentBuilder("").require("Audible").require("Play"))
    def handle_launch_audible_intent(self, message):
        # Mycroft will randomly speak one of the lines from the file
        #    dialogs/en-us/launchmessage.dialog
        self.book_name = message.data["bookname"]
        self.speak_dialog("launchmessage")
"""
    @intent_handler(IntentBuilder("").require("Count").require("Dir"))
    def handle_count_intent(self, message):
        if message.data["Dir"] == "up":
            self.count += 1
        else:  # assume "down"
            self.count -= 1
        self.speak_dialog("count.is.now", data={"count": self.count})
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
