import re

def validate_olx_request(request):
    data = request.json
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    keyword = data.get('keyword', None)
    email = data.get('email', None)
    size = data.get('size', None)
    errors = {}
    if not keyword:
        errors['keyword'] = 'Keyword is required.'
    elif  not isinstance(keyword,str):
        errors['keyword'] = 'Keyword is string.'
    if not email:
        errors['email'] = 'Email is required.'
    elif not re.match(pattern, email):
        errors['email'] = 'Invalid email address.'
    if not size:
        errors['size'] = 'Size is required.'
    elif not isinstance(size,int):
        errors['size'] = 'Size must be a number.'
    elif size < 20 :
        errors['size'] = 'Size must be at least 20.'
    elif size > 300 :
        errors['size'] = 'Size must be at less than 300.'
    return errors, {"keyword":keyword.lower(),"email":email,"size":size}