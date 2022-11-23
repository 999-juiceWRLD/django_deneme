"""
path() argument: route
route is a string that contains a URL pattern. When processing a request, 
Django starts at the first pattern in urlpatterns and makes its way down 
the list, comparing the requested URL against each pattern until it finds 
one that matches.

path() argument: view
When Django finds a matching pattern, it calls the specified view function 
with an HttpRequest object as the first argument and any “captured” values 
from the route as keyword arguments. We’ll give an example of this in a bit.

path() argument: kwargs
Arbitrary keyword arguments can be passed in a dictionary to the target view. 

path() argument: name
Naming your URL lets you refer to it unambiguously from elsewhere in Django, 
especially from within templates. This powerful feature allows you to make 
global changes to the URL patterns of your project while only touching a single 
file.
"""