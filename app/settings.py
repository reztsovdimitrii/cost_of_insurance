import environs

env = environs.Env()
env.read_env('.env')

DATABASE_CONFIG = {
    "connections": {
        "default": env('DATABASE_CONNECTION_URL'),
    },
    "apps": {
        "models": {
            "models": ["app.models.cargo_rate", "aerich.models"],
            "default_connection": "default",
        },
    },
}
