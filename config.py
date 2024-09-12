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
    STRING_SESSION = "1BVtsOJ4Bu4ay-3wY0vB7HjfkFzpFN6s8sxx6ybTGr1iZGSZeq7MXsCblxV-_CXVXMv88KEfQWqFOf0ptMwQYJ0CpGon5Eg2KaQwMNliurLdSZIqU3g3tj6QfPxsHeIHd6UMdwXvJsBqLNH7kmiXEwHPvozoXMES3ELqQ4uTdH_WsylTu0gZX8i9hKvIdJRp1NhhJleQes-sJoWLLp4uCY3wFv7hrKwjuRTPmwXvSHr9fw7ixYPp72ikVsASos6qIoVZ4OgMM2Yfl2Pn40-ST8ywiV7U5MJpokoCoE8NbV-8CthIDxCOPPc0nqPOUfzVzDB-tRKJpYRefNy2q8y9ny-twBfAbUro="
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
