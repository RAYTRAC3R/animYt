from django.db import models

# Create your models here.
class Creator(models.Model):
    name = models.CharField(max_length=32)
    added_date = models.DateTimeField("addition date")
    link = models.URLField()
    def was_added_recently(self):
        return self.added_date >= timezone.now() - datetime.timedelta(days=1)
    def __str__(self):
        return self.name



class Entry(models.Model):
    MEME = "Animation Meme"
    MV = "Music Video"
    OTHER = "Other Video"
    CATEGORY_CHOICES = {
        MEME: "Animation Meme",
        MV: "Music Video",
        OTHER: "Other Video"
    }
    category = models.CharField(
        max_length=32,
        choices=CATEGORY_CHOICES,
        default=MEME,
    )
    creator = models.ForeignKey(Creator, on_delete=models.SET_NULL, null=True)
    entry_name = models.CharField(max_length=320)
    added_date = models.DateTimeField("addition date")
    upload_date = models.DateField("original upload date")
    thumbnail = models.ImageField(null=True, upload_to="thumbnails/entries/%Y/%m/%d")
    link = models.URLField()
    def __str__(self):
        return self.entry_name + " by " + self.creator.name
    def was_added_recently(self):
        return self.added_date >= timezone.now() - datetime.timedelta(days=1)