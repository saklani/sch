# ScriptChain Health

All data: /test

1. What is the difference between select_related and prefetch_related
Demo path: /test1

selected_related - Fetch related (via foreign keys) object in a single SQL join query. Is limited to one-to-one and one-to-many. Does not transform objects in python.

prefetch_related - Fetch related objects using multiple SQL queries. Queries the base object than the related objects then matches them on the server. Adds support for complex queries like many-to-many, many-to-one relations.

2. Explain Q objects in Django ORM and illustrate an example via code?
Demo path: /test2
Adds ability to compose queries with AND, OR, and NOT that can't be expressed with filter (which are always AND).

3. How would you set up your app using Django on AWS EC2 while also keeping your cost to a minimum? Walk us through how you would deploy the application and what steps would you need to do in order to deploy successfully. Give an example.

1. Docker - Configure a docker container for the Django app (let's you move application around and easy to scale when needed)
2. Compute - Deploy on AWS EC2 t3.micro (~$8) on ubuntu
3. Static Objects - S3 (storage) + Cloudfront (caching)
4. Database - SQLite on the AWS EC2 (for lower workload) or Postgres RDS on AWS (~$7/month) (if I want to keep the stack on AWS) or maybe Supabase free tier which supports 50k users
5. Certificates - AWS Certificate Manager + Nginx reverse proxy  
6. Email - SES 

Everything should be less than $20/month for a basic setup.