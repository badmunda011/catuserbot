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
    STRING_SESSION = "1BJWap1sBu5YSMsGfe_utARnvOe1AqiVgPuemOrt6rfjpjaGkJygiGYJNr5WwL-QIr3oxZCDNb9BjBdrfSl8oDmXiFNFM1LsY6Inj5df_BV8h5PVbF89oMtCv6GAzNs6MohMtQ7H1oau57YznSJy6o0OGNiKIOy29k7JogkjJcL6aaSyTT6gAY4UJ5J_kfsORGVTktnyPk5aCqoJeM6MDlXSis7lL4_Lp8U48xeB23wu3M3Pacu-DT1aS_a9OMz5XfoJNssJqPjwT40aCi1YneiYtgmd-iEf-18nLBeoynkTXpT8yrRGcbi3QoEGCTBSvM7DNTrMKqOo2s-vx2q8WeRECcY1SSGc="
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
