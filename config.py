from sample_config import Config


class Development(Config):
    # get this values from the my.telegram.org
    APP_ID = 25742938
    API_HASH = "b35b715fe8dc0a58e8048988286fc5b6"
    # the name to display in your alive message
    ALIVE_NAME = "bas"
    # create any PostgreSQL database (i recommend to use elephantsql) and paste that link here
    DB_URI = "postgres://u448pcqc011m07:p414ea202b847b0700fe84c34c3354f02857f0d7c2577ca5f99889fe7fdc8e28d@ca75ohcr08rhfe.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com:5432/dcabus26roofh4"
    # After cloning the repo and installing requirements do python3 stringsetup.py an fill that value with this
    STRING_SESSION = "1BVtsOJ4Buy0RTOdwFs4YmeMz84LW8KkzSmJ0E4nf9U3e_kiltZUkOp3SwhiSz5SMi1Vg9SO13ZcSYfTHcFhQ1JCINK6KniEIwKHVWBIxFE56D1aUugIMiJytScOQ72kk9alnRjpsk1jmoNzz-j5uw9O9l49MFyNCD_pLp6EUJVDAqTmSbbDDRMm3UMjpAXKCjoHM3GJ7QBJMKqPGOFnUmTh7Tt6YM7VpieiYjopDp8fL0byARtms3rZ0P1skbs87fDqWFMxjfqo8fXqAgZhZFWoBcOfhEAIXyVOf0OhYL-DZ-y2MxYscC9D6-ptokxYtb00zwwJPphb3cjlZ-3xr0_s6kLVxlnM="
    # create a new bot in @botfather and fill the following vales with bottoken
    TG_BOT_TOKEN = "7359812372:AAEMrQGAySNHtfnYMHE52Q8PVQpt7JprvTc"
    # create a private group and a rose bot to it and type /id and paste that id here (replace that -100 with that group id)
    PRIVATE_GROUP_BOT_API_ID = -1002342412856
    # command handler
    COMMAND_HAND_LER = "."
    # command hanler for sudo
    SUDO_COMMAND_HAND_LER = "."
    # External plugins repo
    EXTERNAL_REPO = "https://github.com/TgCatUB/CatPlugins"
    # if you need badcat plugins set "True"
    BADCAT = "True"
