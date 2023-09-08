# SQL - Structured Query Language

### Creating a table

We can create tables by using ‘CREATE TABLE’ statement

```sql
CREATE TABLE table_name (
	column1 datatype,
	column2 datatype,
	column3 datatype,
	...
);
```

- **************Output:**************

| coulumn1  | column2 | column3 |
| --- | --- | --- |
|  |  |  |

### Creating table from another table

```sql
CREATE TABLE new_table_name AS
	SELECT column1, column2
	FROM existing_table_name;
```

### Inserting values

Values can be inserted using ‘INSERT INTO’ statement.

```sql
INSERT INTO table_name(column1, column2, column3)
VALUES (value1, value2, value3);
```

- ********Output:********

| column1  | column2 | column3 |
| --- | --- | --- |
| value1 | value2  | value3 |

### Inserting in particular column

Let’s suppose we have a table which contains the name, age and gender of children in a society. Since we don’t their age, we can skip it if we want. 

```sql
INSERT INTO Children (Name, Gender)
VALUE ('Musa', 'm')
```

- ************Output:************

| Name  | Age | Gender |
| --- | --- | --- |
| Musa | null | m |
|  |  |  |