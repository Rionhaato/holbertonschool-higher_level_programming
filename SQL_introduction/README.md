# SQL Introduction

This directory contains SQL scripts for the Holberton `SQL_introduction` project.

## Project Overview

The goal of this project is to practice core SQL operations using MySQL:
- Database creation and deletion
- Table creation and inspection
- Data insertion, update, deletion
- Data selection, filtering, sorting
- Aggregations and grouping

All scripts are designed to run on MySQL 8.x and follow project constraints.

## Learning Objectives

By completing these tasks, you should be able to explain:
- What a database is
- What a relational database is
- What SQL means (Structured Query Language)
- What MySQL is
- How to create and remove databases
- DDL vs DML
- How to create/alter tables
- How to select, insert, update, and delete data
- How subqueries and functions are used in MySQL

## Requirements Followed

- SQL keywords are uppercase
- Each SQL file starts with a task comment
- Each query has a comment directly above it
- Files end with a newline
- `README.md` is present at the project root (`SQL_introduction/`)

## Files and Tasks

- `0-list_databases.sql`: List all databases on the MySQL server.
- `1-create_database_if_missing.sql`: Create database `hbtn_0c_0` if missing.
- `2-remove_database.sql`: Drop database `hbtn_0c_0` if it exists.
- `3-list_tables.sql`: List all tables in the current database.
- `4-first_table.sql`: Create `first_table` with columns `id` and `name`.
- `5-full_table.sql`: Show full creation statement for `first_table`.
- `6-list_values.sql`: List all rows in `first_table`.
- `7-insert_value.sql`: Insert `(89, 'Best School')` into `first_table`.
- `8-count_89.sql`: Count rows in `first_table` where `id = 89`.
- `9-full_creation.sql`: Create `second_table` and insert initial records.
- `10-top_score.sql`: List `score, name` from `second_table` ordered by score descending.
- `11-best_score.sql`: List records where `score >= 10` ordered by score descending.
- `12-no_cheating.sql`: Update Bob's score to `10` using the `name` field.
- `13-change_class.sql`: Delete rows where `score <= 5`.
- `14-average.sql`: Compute average score as `average`.
- `15-groups.sql`: Group by score and count rows as `number`.
- `16-no_link.sql`: List rows with non-empty `name`, sorted by score descending.

## Usage

Run scripts from this directory using MySQL CLI.

Examples:

```bash
cat 0-list_databases.sql | mysql -uroot
cat 1-create_database_if_missing.sql | mysql -uroot
cat 4-first_table.sql | mysql -uroot hbtn_0c_0
cat 10-top_score.sql | mysql -uroot hbtn_0c_0
```

## Notes

- In some environments, `root` may require `-p` (password); in yours, `mysql -uroot` works.
- Some scripts are intentionally repeatable (for example, `CREATE ... IF NOT EXISTS`).