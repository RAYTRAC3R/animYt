from django.db import models

# Create your models here.
class Creator(models.Model):
    name = models.CharField(max_length=32)
    added_date = models.DateTimeField("addition date")
    link = models.URLField()
    thumbnail = models.URLField(null=True, blank=True)
    
    ACTIVE = "Active" # Videos within the past year.
    MIA = "Missing / Gone" # Total inactivity across all accounts, with no information.
    DELETED = "Deleted" # Majority of main accounts deleted or wiped.
    ARCHIVE = "Archived" # Channel still exists, but is confirmed to no longer post videos.
    HIATUS = "Hiatus" # No videos within the past year, but has activity elsewhere.
    INACTIVE = "Inactive" # Any other forms of inactivity.
    OTHER = "Other" # Special situations.
    STATUS_CHOICES = {
        ACTIVE: "Active",
        HIATUS: "Hiatus",
        ARCHIVE: "Archived",
        DELETED: "Deleted",
        MIA: "Missing / Gone",
        INACTIVE: "Inactive",
        OTHER: "Other"
    }
    status = models.CharField(
        max_length=32,
        choices=STATUS_CHOICES,
        default=OTHER,
    )
    
    def was_added_recently(self):
        return self.added_date >= timezone.now() - datetime.timedelta(days=1)
    def __str__(self):
        return self.name

class Character(models.Model):
    name = models.CharField(max_length=320)
    added_date = models.DateTimeField("addition date")
    thumbnail = models.URLField(null=True, blank=True)
    link = models.URLField("more info")
    creator = models.ForeignKey(Creator, on_delete=models.SET_NULL, null=True, related_name="characters")
    
    def __str__(self):
        return self.name + " by " + self.creator.name
    def was_added_recently(self):
        return self.added_date >= timezone.now() - datetime.timedelta(days=1)

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
    creator = models.ForeignKey(Creator, on_delete=models.SET_NULL, null=True, related_name="memes_made")
    characters = models.ManyToManyField(Character, blank=True, related_name="meme_appearances")
    entry_name = models.CharField(max_length=320)
    added_date = models.DateTimeField("addition date")
    upload_date = models.DateField("original upload date")
    thumbnail = models.URLField(null=True, blank=True)
    link = models.URLField()
    original_meme = models.ForeignKey('self', blank=True, on_delete=models.SET_NULL, null=True, related_name='derived_meme')
    related_memes = models.ManyToManyField('self', blank=True)
    
    def __str__(self):
        return self.entry_name + " by " + self.creator.name
    def was_added_recently(self):
        return self.added_date >= timezone.now() - datetime.timedelta(days=1)