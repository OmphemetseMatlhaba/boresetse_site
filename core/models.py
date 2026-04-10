# core/models.py

from django.db import models

class School(models.Model):
    name = models.CharField(max_length=200)
    tagline = models.CharField(max_length=200)
    logo = models.ImageField(upload_to="logo/")

    def __str__(self):
        return self.name


class Hero(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.TextField()
    background = models.ImageField(upload_to="hero/")


class About(models.Model):
    vision = models.TextField()
    mission = models.TextField()
    values = models.CharField(max_length=200)
    image = models.ImageField(upload_to="about/")


class GalleryImage(models.Model):
    image = models.ImageField(upload_to="gallery/")
    caption = models.CharField(max_length=200, blank=True)


class Post(models.Model):
    title = models.CharField(max_length=200)
    summary = models.TextField()
    image = models.ImageField(upload_to="posts/")
    created_at = models.DateTimeField(auto_now_add=True)


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    # core/models.py

class PrincipalMessage(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField()
    image = models.ImageField(upload_to="principal/")
    title = models.CharField(max_length=100, default="Principal")


class MuralActivity(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="mural_activities/")
    date = models.DateField()
   

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title


class TopStudent(models.Model):
    GRADE_CHOICES = [
        (8, 'Grade 8'),
        (9, 'Grade 9'),
        (10, 'Grade 10'),
        (11, 'Grade 11'),
        (12, 'Grade 12'),
    ]
    name = models.CharField(max_length=100)
    grade = models.IntegerField(choices=GRADE_CHOICES)
    position = models.IntegerField(help_text="Position in top 10, e.g., 1 for top student")
    average = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    class Meta:
        ordering = ['grade', 'position']
        unique_together = ['grade', 'position']

    def __str__(self):
        return f"{self.name} - Grade {self.grade} (#{self.position})"


class StaffMember(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    image = models.ImageField(upload_to="staff/")
    bio = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} - {self.position}"


class SGBMember(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    image = models.ImageField(upload_to="sgb/")
    bio = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} - {self.position}"


class CodeOfConduct(models.Model):
    title = models.CharField(max_length=200)
    document = models.FileField(upload_to="documents/code_of_conduct/", blank=True, null=True, help_text="Upload PDF document")
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Code of Conduct"

    def __str__(self):
        return self.title


class Newsletter(models.Model):
    title = models.CharField(max_length=200)
    summary = models.TextField(max_length=500)
    content = models.TextField()
    image = models.ImageField(upload_to="newsletters/")
    published_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-published_date']

    def __str__(self):
        return self.title

class RCL (models.Model):
    
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} - {self.position}"
    
class head_of_rcl(models.Model):
    image= models.ImageField(upload_to="rcl/")
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} - {self.position}" 
    

class rcl_group(models.Model):
    image= models.ImageField(upload_to="rcl/")
    year = models.CharField(max_length=20)
    def __str__(self):
        return f"RCL Group - {self.year}"
    
    
