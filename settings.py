from configs.connection import DATABASE_URL

db_url=DATABASE_URL()
TORTOISE_ORM={
    "connections":{'default':db_url},
    "app":{
        "models":{
            "models":['user.models','aerich.models'],
            "default_connection":'default',
        },
    },
}