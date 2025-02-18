import environ

# Initialize environment
env = environ.Env(
    # DEBUG
    DEBUG=(bool, False),

    # ALLOWED HOSTS
    ALLOWED_HOSTS=(list, []),

    # SECRET KEY
    SECRET_KEY=(str, ''),

    # PostgresDB
    PGSQL_NAME=(str, ''),
    PGSQL_USER=(str, ''),
    PGSQL_PASSWORD=(str, ''),
    PGSQL_HOST=(str, ''),
    PGSQL_PORT=(str, ''),
)

env.read_env()