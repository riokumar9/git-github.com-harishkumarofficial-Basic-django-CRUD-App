from django.db import models
from django.template.defaultfilters import slugify

#This Function is Creted a Unique_Slug 
def unique_slugify(instance,slug):
    model = instance.__class__
    unique_slug = slug
    record_count = 0
    while model.objects.filter(slug = unique_slug).exists():
        unique_slug = slug + "-1"
        while model.objects.filter(slug = unique_slug).exists():
            record_count = record_count+1
            unique_slug = slug + "-" +str(record_count)
    return unique_slug

# Category Of Books 
class BookCategory(models.Model):
    category_name = models.CharField(max_length = 50,blank = False,null = False)
    slug = models.SlugField(max_length = 100,null = True,editable = False)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now_add = True)

    # This Function is object to identity name
    def __str__(self):
        return str(self.category_name)

    # This Function is Models Name Standart
    class Meta:
        verbose_name_plural = "BooksCategory"

    # This Function is Save For Slug and Call the unique_slugify.
    def save(self, *args, **kwargs):
        if not self.slug:
            slug_text = slugify(self.category_name)
            self.slug = unique_slugify(self, slug_text)
        self.clean()                    
        super().save(*args, **kwargs)


# Books Informations
class BookDeatils(models.Model):
    title = models.CharField(max_length = 50,blank = False,null = False)
    slug = models.SlugField(max_length=250, null=True, editable=False)
    author_name = models.CharField(max_length = 50,blank = False,null = False)
    thumbnail_image = models.ImageField(null=True, blank=True, upload_to='images')
    category = models.ForeignKey(BookCategory,null=False, blank=False, on_delete=models.CASCADE, related_name='Book_category_name')
    created_at = models.DateTimeField(auto_now_add = True)
    updtated_at = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return self.author_name

    class Meta:
         verbose_name_plural = "BookDeatils"
        

    def save(self, *args, **kwargs):
        if not self.slug:
            slug_text = slugify(self.author_name)
            self.slug = unique_slugify(self, slug_text)
        self.clean()
        super().save(*args, **kwargs)
