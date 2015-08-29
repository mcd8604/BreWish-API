# BreWish-API  
This API is written using the Django REST Framework: http://www.django-rest-framework.org  

If you need to explore the API, simply navigate to the root API url.  

Default response format is HTML wrapped JSON. This is to allow easy browsing of the full API.
When developing to the API, it is recommended to always include the preferred format: <root API URL>?format={preferred format}  

Supported Formats: (API, JSON, XML)  

Dependencies

defusedxml==0.4.1  
Django==1.8.3  
djangorestframework==3.2.1  
djangorestframework-xml==1.2.0  
Markdown==2.6.2  
meld3==1.0.2  
pbr==1.4.0  
six==1.9.0  
stevedore==1.7.0  

Recommendations

virtualenv==13.1.0  
virtualenv-clone==0.2.6  
virtualenvwrapper==4.6.0  
supervisor==3.1.3  
gunicorn==19.3.0  
psycopg2==2.6.1  
