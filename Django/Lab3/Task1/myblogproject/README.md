requirements:
LAB3 ( all the question are related )
------------------------------------------
Create a Django app called blog and create a Post model with fields title, content, and date_published. Then, create a DRF serializer for the Post model.
		
Create a DRF viewset for the Post model that allows users to list, create, retrieve, update, and delete posts.

Add authentication to the Post viewset using token authentication.

Add filtering to the Post viewset so that users can filter posts by date_published.

Add pagination to the Post viewset so that users can see a limited number of posts per page.

Create a DRF viewset for comments that allows users to list, create, retrieve, update, and delete comments for a particular post.

Add authorization to the Comment viewset so that users can only modify comments they have created.

Add validation to the Comment model so that only authenticated users can create comments.

Create a DRF endpoint that allows users to search for posts by title.