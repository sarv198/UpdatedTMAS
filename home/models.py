from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone

# Create your models here.

class Category(models.Model):
    """Categories for organizing books (e.g., Programming, Data Science, Web Development)"""
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField(max_length=100, unique=True)
    created_at = models.DateTimeField(default=timezone.now)
    
    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['name']
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('category-books', kwargs={'slug': self.slug})

class Author(models.Model):
    """Authors of the books"""
    name = models.CharField(max_length=200)
    bio = models.TextField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='authors/', blank=True, null=True)
    
    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name

class Book(models.Model):
    """Main Book model for the resources page"""
    
    # Book difficulty levels
    DIFFICULTY_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ]
    
    # Book types
    TYPE_CHOICES = [
        ('free', 'Free'),
        ('paid', 'Paid'),
        ('subscription', 'Subscription'),
    ]
    
    title = models.CharField(max_length=200)
    authors = models.ManyToManyField(Author, related_name='books')
    description = models.TextField()
    short_description = models.CharField(max_length=300, help_text="Brief description for cards/previews")
    
    # Book details
    isbn = models.CharField(max_length=13, blank=True, null=True, help_text="ISBN-13 number")
    publication_date = models.DateField(blank=True, null=True)
    pages = models.PositiveIntegerField(blank=True, null=True)
    language = models.CharField(max_length=50, default='English')
    
    # Categorization
    categories = models.ManyToManyField(Category, related_name='books')
    difficulty_level = models.CharField(max_length=20, choices=DIFFICULTY_CHOICES, default='beginner')
    
    # Pricing and access
    book_type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='free')
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    
    # Links and resources
    purchase_url = models.URLField(blank=True, null=True, help_text="Link to buy/access the book")
    preview_url = models.URLField(blank=True, null=True, help_text="Link to preview/sample")
    download_url = models.URLField(blank=True, null=True, help_text="Direct download link for free books")
    
    # Media
    cover_image = models.ImageField(upload_to='book_covers/', blank=True, null=True)
    
    # SEO and metadata
    slug = models.SlugField(max_length=200, unique=True)
    meta_description = models.CharField(max_length=160, blank=True, help_text="SEO meta description")
    
    # Tracking
    is_featured = models.BooleanField(default=False, help_text="Show on homepage/featured sections")
    is_published = models.BooleanField(default=True)
    views_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = "Book"
        verbose_name_plural = "Books"
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('book-detail', kwargs={'slug': self.slug})
    
    def get_authors_display(self):
        """Return comma-separated list of authors"""
        return ", ".join([author.name for author in self.authors.all()])
    
    def increment_views(self):
        """Increment view count"""
        self.views_count += 1
        self.save(update_fields=['views_count'])

class BookReview(models.Model):
    """User reviews for books"""
    
    RATING_CHOICES = [
        (1, '1 Star'),
        (2, '2 Stars'), 
        (3, '3 Stars'),
        (4, '4 Stars'),
        (5, '5 Stars'),
    ]
    
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    reviewer_name = models.CharField(max_length=100)
    reviewer_email = models.EmailField(blank=True)
    rating = models.IntegerField(choices=RATING_CHOICES)
    review_text = models.TextField()
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering = ['-created_at']
        unique_together = ['book', 'reviewer_email']  # One review per email per book
    
    def __str__(self):
        return f"{self.reviewer_name} - {self.book.title} ({self.rating} stars)"

class ResourceCollection(models.Model):
    """Curated collections of books (e.g., "Best Python Books", "Data Science Essentials")"""
    title = models.CharField(max_length=200)
    description = models.TextField()
    books = models.ManyToManyField(Book, related_name='collections')
    slug = models.SlugField(max_length=200, unique=True)
    cover_image = models.ImageField(upload_to='collections/', blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('collection-detail', kwargs={'slug': self.slug})