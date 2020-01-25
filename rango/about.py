
# coding: utf-8

# In[ ]:


# coding: utf-8

# In[ ]:


from django.urls import path
from rango import views

app_name = 'rango'

urlpatterns = [path('', views.about, name='about'),]

