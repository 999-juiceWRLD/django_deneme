"""
Migrations are Django’s way of propagating changes 
you make to your models (adding a field, deleting a 
model, etc.) into your database schema. They’re 
designed to be mostly automatic, but you’ll need to 
know when to make migrations, when to run them, and 
the common problems you might run into.

Commands:

- migrate: which is responsible for applying and unapplying 
migrations.

- makemigrations: which is responsible for creating new 
migrations based on the changes you have made to your 
models.

You should think of migrations as a version control 
system for your database schema. makemigrations is 
responsible for packaging up your model changes into
individual migration files - analogous to commits - 
and migrate is responsible for applying those to your 
database.

The migration files for each app live in a “migrations” 
directory inside of that app, and are designed to be 
committed to, and distributed as part of, its codebase. 
You should be making them once on your development machine 
and then running the same migrations on your colleagues’ 
machines, your staging machines, and eventually your 
production machines.

Migrations will run the same way on the same dataset 
and produce consistent results, meaning that what you 
see in development and staging is, under the same 
circumstances, exactly what will happen in production.

Django will make migrations for any change to your 
models or fields - even options that don’t affect 
the database - as the only way it can reconstruct a 
field correctly is to have all the changes in the 
history, and you might need those options in some 
data migrations later on (for example, if you’ve set 
custom validators).

========================================================

- The exact output will vary depending on the database you 
are using. The example above is generated for PostgreSQL.

- Table names are automatically generated by combining the 
name of the app (polls) and the lowercase name of the 
model – question and choice. (You can override this behavior.)

- Primary keys (IDs) are added automatically. (You can override 
this, too.)

- By convention, Django appends "_id" to the foreign key field name.
(Yes, you can override this, as well.)

- The foreign key relationship is made explicit by a FOREIGN KEY 
constraint. Don’t worry about the DEFERRABLE parts; it’s telling 
PostgreSQL to not enforce the foreign key until the end of the 
transaction.

- It’s tailored to the database you’re using, so database-specific 
field types such as auto_increment (MySQL), bigint PRIMARY KEY 
GENERATED BY DEFAULT AS IDENTITY (PostgreSQL), or integer primary 
key autoincrement (SQLite) are handled for you automatically. Same 
goes for the quoting of field names – e.g., using double quotes 
or single quotes.

- The sqlmigrate command doesn’t actually run the migration on your 
database - instead, it prints it to the screen so that you can see 
what SQL Django thinks is required. It’s useful for checking what 
Django is going to do or if you have database administrators who 
require SQL scripts for changes.
"""