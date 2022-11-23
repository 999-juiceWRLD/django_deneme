""" 
render()
render(request, template_name, context=None, 
       content_type=None, status=None, using=None)
       
Combines a given template with a given context 
dictionary and returns an HttpResponse object with 
that rendered text.

REQUIRED ARGUMENTS

request
The request object used to generate this response.

template_name
The full name of a template to use or sequence of 
template names. If a sequence is given, the first 
template that exists will be used.
"""