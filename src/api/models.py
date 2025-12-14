from django.db import models
from django.contrib.auth.models import User


class BaseContent(models.Model):
    content = models.TextField()
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="%(class)s_author",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Blogs(BaseContent):
    title = models.CharField(max_length=30)
    img=models.ImageField(null=True,blank=True,upload_to='img')

    def __str__(self):
        return self.title


class Comments(BaseContent):
    blog = models.ForeignKey(
        Blogs,
        on_delete=models.CASCADE,
        related_name='comments'
    )

    def __str__(self):
        return f"{self.author} - {self.blog.title}"



