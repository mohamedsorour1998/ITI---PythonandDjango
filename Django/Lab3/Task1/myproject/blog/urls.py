from django.contrib import admin
from django.urls import path
from blog.views import PostViewSet, CommentViewSet
##### REST API Endpoints #####
# List all posts: GET /posts/
# Create a new post: POST /posts/
# Retrieve a specific post: GET /posts/<post_id>/
# Update a specific post: PUT /posts/<post_id>/
# Partially update a specific post: PATCH /posts/<post_id>/
# Delete a specific post: DELETE /posts/<post_id>/
# List all comments: GET /comments/
# Create a new comment: POST /comments/
# Retrieve a specific comment: GET /comments/<comment_id>/
# Update a specific comment: PUT /comments/<comment_id>/
# Partially update a specific comment: PATCH /comments/<comment_id>/
# Delete a specific comment: DELETE /comments/<comment_id>/

# as_view() method to convert the PostViewSet and CommentViewSet into views that can handle HTTP requests.
# We also specify the HTTP methods that each view should handle
# using a dictionary with keys for each method and values that specify the view method to call.
urlpatterns = [
    path('posts/',
         PostViewSet.as_view({
             'get': 'list',
             'post': 'create'
         }),
         name='post-list'),
    path('posts/<int:pk>/',
         PostViewSet.as_view({
             'get': 'retrieve',
             'put': 'update',
             'patch': 'partial_update',
             'delete': 'destroy'
         }),
         name='post-detail'),
    path('comments/',
         CommentViewSet.as_view({
             'get': 'list',
             'post': 'create'
         }),
         name='comment-list'),
    path('comments/<int:pk>/',
         CommentViewSet.as_view({
             'get': 'retrieve',
             'put': 'update',
             'patch': 'partial_update',
             'delete': 'destroy'
         }),
         name='comment-detail'),
    path('admin/', admin.site.urls),
]

##### how to obtain tokens #####
# To obtain a JWT token for an authenticated user,
# you'll need to send a POST request to the /token/ endpoint with the user's
# credentials (i.e., username and password) in the request body.
# Here's an example of how to do this using the curl command-line tool:

# curl -X POST -H "Content-Type: application/json" -d '{"username": "<username_here>", "password": "<password_here>"}' http://127.0.0.1:8000/token/
# Replace <username_here> and <password_here> with the credentials of a valid user in your Django app.
# This will authenticate the user and generate a JWT token that can be used to make authenticated requests to your API.
# The -X option specifies the HTTP method to use (in this case, POST).
# The -H option sets the Content-Type header to indicate that the request body is JSON data.
# The -d option sends the user credentials in the request body as JSON.
# Finally, the URL for the request is http://127.0.0.1:8000/token/,
# which is the endpoint for obtaining a JWT token. If the credentials are valid,
# the server will respond with a JSON object containing the token.