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
    STRING_SESSION = "1BJWap1wBu2tycBO1CQppq5oyMqieh5Efm559SH8i7Djk9B4w23szf8cvxDlinmOVGcOkqyiCcNdhZ9FWijyNKry9OuCbrvRIJ8P-SScYBUezPgZlV6Tr1CLlPzTpg8jInOGLTFDVJosSuEeSfVcQv6sWG1WAj2WYMKfpoM9RTS3Hltx3n4o5--3apxyK5pp5N_tsY8x_0WedHx_gLChKg22cqTXBuObduFLmnyQ-OARA2IzY8tLS6e1a2jegl_JPolvP7ncw60tZJ5DW7wq9D0HmKgJAuT0fNFSv-0EJfQ-GSb7tR0-f5GRud1uy2OHHt-9hqUDDJeDyUOAIHkf8WcKk6iV4DkE="
    # create a new bot in @botfather and fill the following vales with bottoken
    TG_BOT_TOKEN = "7052737706:AAGqYPdQxxH7576wOTkkoXOAgdXe6RsUr2Y"
    # create a private group and a rose bot to it and type /id and paste that id here (replace that -100 with that group id)
    PRIVATE_GROUP_BOT_API_ID = -1002181404437
    # command handler
    COMMAND_HAND_LER = "."
    # command hanler for sudo
    SUDO_COMMAND_HAND_LER = "."
    # External plugins repo
    EXTERNAL_REPO = "https://github.com/TgCatUB/CatPlugins"
    # if you need badcat plugins set "True"
    BADCAT = "False"
