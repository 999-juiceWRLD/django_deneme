"""
Philosophy

A model is the single, definitive source of information 
about your data. It contains the essential fields and
behaviors of the data you’re storing. Django follows the 
DRY Principle. The goal is to define your data model in
one place and automatically derive things from it.

This includes the migrations - unlike in Ruby On Rails, 
for example, migrations are entirely derived from your models 
file, and are essentially a history that Django can roll 
through to update your database schema to match your current
models.

In our poll app, we’ll create two models: Question and Choice.
A Question has a question and a publication date. A Choice has 
two fields: the text of the choice and a vote tally. Each 
Choice is associated with a Question.
"""