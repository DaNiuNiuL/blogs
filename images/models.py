from django.db import models
from django.conf import settings
from django.urls import reverse
from uuslug import slugify
# Create your models here.

class Image(models.Model):
    #user 这是一个连接到user模型的外键 用户与图片是一个一对多的关系 一个用户可以上传多个图片
    user = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='image_created',on_delete=models.CASCADE)
    #图片的名称
    title = models.CharField(max_length=200)
    #slug 图片的简称 用来动态建立该图片的url
    slug = models.CharField(max_length=200,blank=True)
    url = models.URLField()
    image = models.ImageField(upload_to='images/%Y/%m/%d')
    description = models.TextField(blank=True)
    #存储那些用户喜欢这个图片 由于一个用户可能喜欢多个图片，一个图片页可能被多个用户喜欢 所以用多对多的关系
    user_like = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='image_liked',blank=True)
    created = models.DateField(auto_now_add=True,db_index=True)


    def __str__(self):
        return self.title
    def save(self, *args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Image,self).save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('images:detail',args=[self.id,self.slug])
