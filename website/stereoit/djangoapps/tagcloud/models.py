from django.db import models

# Create your models here.
class Tag(models.Model):
	'''
	Tag is a short name for a specific thing.
	'''
	name = models.CharField(max_length=24,help_text='Short descriptive name of the Tag')
	slug = models.SlugField(max_length=24,help_text="urlized version of tag name")
	description = models.TextField(help_text='Complete description of the tag', blank=True)
	intensity = models.IntegerField(help_text="1-100 importance of the tag", default=50)
	created	= models.DateTimeField(auto_now_add=True)
	active = models.BooleanField(help_text="Is the tag activated?",default=True)
	wiki_powered = models.BooleanField('Reference', help_text="Description is taken from Wikipedia?", default=False)
	wiki_keyword = models.CharField('Keyword',max_length=150,help_text='Wikipedia keyword for given tag',blank=True)

	def __unicode__(self):
		return '%s [%s]' % (self.name, self.intensity)

	@models.permalink
	def get_absolute_url(self):
		return ('tag_detail', [str(self.slug)])
		#return '/tags/%s/' % self.slug
	
class TagCloud(models.Model):
	'''
	TagCloud is an object representig set of tag. Its purpose is to be rendered 
	'''
	name = models.CharField(max_length=24,help_text='Short descriptive name of the Cloud')
	slug = models.SlugField(max_length=24,help_text="urlized version of tag name")
	description = models.TextField(help_text="Short generic decsription of cloud intended usage")
	tags = models.ManyToManyField('Tag')
	active = models.BooleanField(help_text="Is the Cloud activated?", default=True)
	created	= models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = 'cloud'

	def __unicode__(self):
		return '%s' % self.name

	@models.permalink
	def get_absolute_url(self):
		return ('tagcloud_detail', [str(self.slug)])

	def list_of_tags(self):
		'returns stringified list of all tags'
		return ' '.join([tag.name for tag in self.tags.all()])

	
