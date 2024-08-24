# Introducing Databases

A database is a system for storing and organizing data. For example, in a library, a database can hold information about patrons, books, and checkouts, organized into tables with rows and columns. 

The **patrons table** contains data such as library card number, name, membership year, and overdue fines. A **relational database** establishes relationships between these tables, allowing us to answer questions like which books a patron checked out or which books are most frequently checked out.

While tables in databases may resemble those in spreadsheet applications like Excel, databases offer greater storage capacity and enhanced security through encryption. A key advantage of databases is that multiple users can simultaneously write queries to extract insights from the data without altering it.

**SQL** (Structured Query Language) is the primary programming language used to create, query, and update relational databases. Familiarity with the data and its organization allows us to write SQL queries to gain insights, which will be explored further in Chapter Two.

The core component of a database is tables, which store related data about specific subjects. Tables consist of rows (referred to as records) and columns (called fields). While the number of rows is unlimited, the fields are fixed upon table creation.

When naming tables, it's best to use lowercase letters without spaces, opting for underscores instead. A good practice is to use collective or plural names for tables, such as "inventory" or "products."

A record represents a single row in a table and contains data about one observation. For instance, a patron table would include records for each patron, detailing information like membership dates and outstanding fines. Conversely, fields are the table's columns, providing specific information about each record, such as a patron's name.

Field naming is crucial since they are referenced in SQL queries. It's recommended that field names be lowercase, singular, and devoid of spaces. Moreover, field names should be unique within a table and should not mimic the table's name to avoid confusion.

A unique identifier, often called a "key," distinguishes records within a table. For the patron's table, the "card_num" serves as the unique identifier, ensuring clarity as patrons may share names.

Having multiple tables, each focused on a specific subject, is preferable to consolidating different subjects into fewer tables, as this leads to confusion due to duplicated information. For example, merging patrons and checkout tables can result in non-unique identifiers and less clarity. SQL can still be utilized to connect data across these separate tables when needed.
