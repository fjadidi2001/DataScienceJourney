# Introducing Databases

A database is a system for storing and organizing data. For example, in a library, a database can hold information about patrons, books, and checkouts, organized into tables with rows and columns. 

## Key Concepts

| Concept             | Description                                                                                 |
|---------------------|---------------------------------------------------------------------------------------------|
| **Patrons Table**   | Contains data such as library card number, name, membership year, and overdue fines.       |
| **Relational Database** | Establishes relationships between tables to answer complex queries (e.g., books checked out by a patron). |
| **SQL**             | Structured Query Language used for creating, querying, and updating relational databases.    |
| **Tables**          | Core component of a database, consisting of rows (records) and columns (fields).             |

## Structure of a Table

- **Rows (Records)**: Each row represents a single observation in the table.
- **Columns (Fields)**: Each column provides specific information about the records.

### Naming Conventions

#### Table Naming Best Practices

- Use lowercase letters without spaces.
- Opt for underscores to separate words.
- Use collective or plural names (e.g., `inventory`, `products`).

#### Field Naming Best Practices

- Use lowercase letters and singular nouns.
- Avoid spaces in names.
- Ensure uniqueness within a table.
- Avoid naming fields the same as the table to prevent confusion.

## Unique Identifiers

- A unique identifier (or "key") distinguishes records within a table. 
- Example: In the patrons table, `card_num` can serve as the unique identifier to avoid ambiguity among patrons with the same name.

## Table Organization

- It is preferable to have multiple tables focused on specific subjects rather than consolidating different subjects into fewer tables.
- Consolidation can lead to confusion due to duplicated information (e.g., merging patrons and checkout tables).

## SQL and Data Connection

- SQL allows for the connection and querying of data across separate tables when needed. 

This organization helps maintain clarity and integrity in the database design, facilitating efficient data retrieval and management.
