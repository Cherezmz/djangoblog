The idea of the project is to create a blog that can be used as a portfolio storage.

All users can:

- see all the posts
- create posts
- comments posts
- update user's posts and comments

The authorized user may:

- delete posts and comments
- update posts and comments

Preliminary ideas to implement (if I have time and enough knowledge):

- send info to user's email

The models:

1. User:

- name
- last name
- bio
- picture
- email

  2.Post:

- date
- title
- tag
- body
- link to GH
- code snippet (image)
- author (user)
- comments

3. Comments (for Post)

- date
- author (user)
- body

localhost:8000 - articles list
http://127.0.0.1:8000/accounts/signup/ - signup
http://127.0.0.1:8000/accounts/login/ - log in
