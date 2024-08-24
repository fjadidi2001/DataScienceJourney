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



# SQL Data Types and Database Concepts

## 1. SQL Data Types
When creating a table, it is necessary to specify a data type for each field based on the nature of the data it will hold, such as numbers, text, or dates. Data types are important for several reasons:
- Different data types require different storage formats and space.
- Certain operations are applicable only to specific data types (e.g., multiplication for numbers, but not for text).

## 2. Strings
A "string" in programming is a sequence of characters, including letters and punctuation. For example, names like "Maham" and "James" are strings. SQL provides several data types for strings:
- Some types are limited to short strings (up to 250 characters), which helps save storage space.
- The `VARCHAR` data type can store strings of varying lengths, accommodating up to tens of thousands of characters, making it a flexible and commonly used option.

## 3. Integers
Integer data types are used to store whole numbers, such as the `member_year` in the patrons table. SQL includes different integer data types depending on the size of the numbers, with `INT` being a common type that stores values from just under -2 billion to just over +2 billion.

## 4. Floats
Float data types store numbers that have a fractional part, such as monetary values (e.g., 2.05 dollars). SQL offers several float data types based on the expected number of digits, with the `NUMERIC` type capable of storing floats with up to 38 total digits, including those before and after the decimal point.

## 5. Schemas
A database schema serves as a "blueprint," illustrating the database's design, including the tables it contains and any relationships between them. It also indicates the data types each field can hold. For example, in a library database schema, `VARCHAR` is used for strings like book titles, authors, and genres. The patrons table is also shown to be related to the checkouts table, but not directly to the books table.<br>
**Database schemas show data types for each field in all tables, and they also show relationships between tables. **
## 6. Database Storage
The information in a database table is stored physically on a server's hard disk. Servers are centralized computers that perform services in response to network requests. In this context, the service provided is data access. Servers can be any computer configured to offer a service, but they are typically powerful machines capable of handling high volumes of requests and data.


