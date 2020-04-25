from django.db import models
from django.utils.text import slugify
class Author(models.Model):
    first_Name = models.CharField('Nome', max_length=10, blank=False, null=True)
    last_Name = models.CharField('Sobrenome', max_length=50, null=True)
    description = models.TextField('Descrição', blank=True, null=True)
    contact_Site = models.URLField('Site pessoal', blank=True, null=True)
    contact_Facebook = models.URLField('Facebook', blank=True, null=True)
    contact_Twiter = models.URLField('Twiter', blank=True, null=True)
    contact_Instagram = models.URLField('Instagram',blank=True, null=True)
    contact_GitHub = models.URLField('GitHub', blank=True, null=True)
    contact_Linkedin = models.URLField('Linkedin', blank=True, null=True)
    photo = models.ImageField('Imagem de Perfil', blank=True, null=True) 
    
    def __str__(self):
        return self.first_Name + ' ' + self.last_Name
class Category(models.Model):
    name = models.CharField('Nome da Categoria', null=True, blank=True, max_length=20)
    def __str__(self):
        return self.name

class imagens_for_post(models.Model):
    image = models.ImageField('Imagem')
    position = models.IntegerField()
    imagetitle = models.CharField(max_length=10)
    class Meta:
        ordering=['position']
    def __str__(self):
        return self.imagetitle

class Post(models.Model):
    """
        Model to storage posts.
        The imagelist will receive images from de classes imagens_for_post, this is Because may have
        more that on image in post.
    """
    posts_choices =[
        ("simplePost","Post Simples"),
        ("postQuote","Citação na Tela Inicial"),
        ("postAudio","Post com Audio"),
        ("postVideo","Post com Video"),
        ("postMultipleImagens","Post com Multiplas Imagens in Carrousel") ]
    type_of_post=models.CharField('Tipo de Post',max_length=20, choices=posts_choices, blank=False)
    title = models.CharField('Titulo',max_length=100)
    date_of_publication=models.DateTimeField('Data de Publicacao',auto_now_add=True)
    modified_in=models.DateTimeField('Data de Modificacao',auto_now=True, blank=True, null=True)
    label =models.SlugField('Url', unique=True, blank=True)
    summary_post = models.TextField('Resumo do Post, ou Citação')
    text_html = models.TextField('Texto em Html')
    author_in_quote = models.CharField('Autor da citação', max_length= 15, null=True, blank=True)
    image_thumb = models.ImageField("Imagem da Thumb", blank=True)
    imagelist = models.ManyToManyField(imagens_for_post, blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, blank=True, null=True)
    categorys = models.ManyToManyField(Category, blank=True) 
    class Meta:
        ordering=["-date_of_publication"]

    def save(self, *args, **kwargs):
        self.label = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class postQuote(models.Model):
    type_of_post=models.CharField('Tipo de Post',max_length=20, default='postQuote')
    quote = models.CharField('Citação', max_length=244, unique=True)
    quote_author = models.CharField('Autor da Citação', max_length=25)

    def __str__(self):
        return self.quote[0:30]