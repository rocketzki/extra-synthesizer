from django.urls import path

from extra_synthesizer.app import view

urlpatterns = [
    path('', view.index, name='index'),
    path('synthesize', view.synthesize, name='synthesize')
]
