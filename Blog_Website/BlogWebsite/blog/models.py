from django.db import models
class User(models.Model):
  id = models.AutoField(primary_key=True)  # Use AutoField for unique IDs
  Username = models.CharField(max_length=255)
  email = models.EmailField(max_length=255)
  password = models.CharField(max_length=255)

  def __str__(self):
    return f"{self.id} {self.Username}"


class Post(models.Model):
  id = models.AutoField(primary_key=True)
  Title = models.CharField(max_length=255)
  Content = models.TextField()  # Use TextField for longer content
  Category = models.CharField(max_length=255)  # Foreign key relation
  date_published = models.DateTimeField()
  def __str__(self):
    return f"{self.Title} {self.Category}"


class Comment(models.Model):
  id = models.AutoField(primary_key=True)
  post = models.ForeignKey(Post, on_delete=models.CASCADE)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  Content = models.TextField()  # Use TextField for longer content
  Date_Posted = models.DateTimeField()



class Category(models.Model):
  id = models.AutoField(primary_key=True)  # Use AutoField for unique IDs
  Name = models.CharField(max_length=255)
