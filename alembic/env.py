from logging.config import fileConfig
from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context

config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = None


def run_migrations_offline() -> None:
    """
    Выполняет миграции базы данных в автономном режиме.

    Этот метод настраивает контекст миграции с помощью URL базы данных, метаданных целевой схемы и других параметров, необходимых для выполнения миграций.
    Он также открывает транзакцию и запускает миграции.

    Returns:
        None
    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """
    Выполняет миграции базы данных в онлайн-режиме.

    Этот метод создает подключаемый объект из конфигурации SQLAlchemy, настраивает контекст миграции с подключением к базе данных
    и запускает миграции. Он также открывает транзакцию и запускает миграции.

    Returns:
        None
    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
