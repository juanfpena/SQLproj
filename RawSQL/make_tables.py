"""This file is used to create tables in the database."""

from config import my_cursor

create_table_queries = open(
    "SQL_statements/create_and_drop_queries/create_all.sql", "r").read().split(";")


def create_tables(queries: list) -> None:
    """Create all tables"""

    for line in queries:
        try:
            my_cursor.execute(line)
        except:
            pass


if __name__ == "__main__":
    create_tables(create_table_queries)
