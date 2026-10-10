# Objective 

- This is data access layer. 
- takes in db session and returns orm models
- Its implementation is tied to specific database / ORM
- Separate repository per entity like UserRepository.
- In case more that 1 databases then can extend like MongoUserRepository, MySQLUserRepository, etc.
- Example -> get_user_by_id, get_user_by_email, create_post, etc
