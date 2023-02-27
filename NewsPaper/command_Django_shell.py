user1=User.objects.create_user(username='Ivan')

user2 = User.objects.create_user(username='Roman')

Author.objects.create(authorUser=user1)

Author.objects.create(authorUser=user2)

Category.objects.create(name='IT')

Category.objects.create(name='Sport')

Category.objects.create(name='Books')

Category.objects.create(name='Games')

author_1=Author.objects.get(id=1)

author_2=Author.objects.get(id=2)

Post.objects.create(author_1, categoryType='NW', title='Atomic Heart or Hogwarts Legacy?', text='One day - one games')

Post.objects.get(id=1).postCategory.add(Category.objects.get(id=1))

Post.objects.get(id=1).postCategory.add(Category.objects.get(id=4))

Post.objects.create(author=author_2, categoryType='NW', title='Updates Python', text='somebigtext')

Post.objects.get(id=2).postCategory.add(Category.objects.get(id=1))

Post.objects.create(author=author_1, categoryType='AR', title='Artical_1', text='text_artical_1')

Post.objects.create(author=author_1, categoryType='AR', title='Artical_2', text='text_artical_2')

Comment.objects.create(commentPost=Post.objects.get(id=1), commentUser=Author.objects.get(id=2).authorUser, text='useing Python in Atomic Heart?')

Comment.objects.create(commentPost=Post.objects.get(id=1), commentUser=Author.objects.get(id=1).authorUser, text='otvet dam potom')

Comment.objects.create(commentPost=Post.objects.get(id=2), commentUser=Author.objects.get(id=2).authorUser, text='comment_text_2')

Comment.objects.create(commentPost=Post.objects.get(id=3), commentUser=Author.objects.get(id=2).authorUser, text='comment_text_3')

Comment.objects.create(commentPost=Post.objects.get(id=4), commentUser=Author.objects.get(id=1).authorUser, text='comment_text_4')

Comment.objects.get(id=1).like()

Comment.objects.get(id=2).like()

Comment.objects.get(id=3).dislike()

author_1.upgrade_rating()

author_1.ratingAuthor

Post.objects.get(id=1).like()

author_1.ratingAuthor

ratA=Author.objects.order_by('-ratingAuthor')[:1]

ratA

comR=Post.objects.order_by('-rating')[:1]
>>>
>>> for i in comR:    ion
...     i.dateCreation
...     i.author
...     i.rating
...     i.title
...     i.preview()

Author.objects.get(id=1).authorUser

com=Comment.objects.all()

