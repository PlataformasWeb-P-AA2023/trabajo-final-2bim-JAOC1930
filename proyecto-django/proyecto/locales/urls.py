from django.urls import path
# se importa las vistas de la aplicación
from . import views


urlpatterns = [
        path('', views.index, name='index'),
        path('index2', views.index2, name='index2'),
        path('crear/Barrio', views.crear_Barrio, name = 'crear_Barrio'),
        path('crear/Persona', views.crear_Persona, name = 'crear_Persona'),
        path('crear/local/Comida', views.crear_LocalComida, name = 'crear_LocalComida'),
        path('crear/Local/Respuestos', views.crear_LocalRespuestos, name = 'crear_LocalRespuestos'),
        path('editar/Barrio/<int:id>', views.editar_Barrio, name = 'editar_Barrio'),
        path('editar/Persona/<int:id>', views.editar_Persona, name = 'editar_Persona'),
        path('editar/Local/Comida/<int:id>', views.editar_LocalComida, name = 'editar_LocalComida'),
        path('editar/Local/Respuesto/<int:id>', views.editar_LocalRespuestos, name = 'editar_LocalRespuestos'),
        path('eliminar/Barrio/<int:id>', views.eliminar_Barrio, name = 'eliminar_Barrio'),
        path('eliminar/Persona/<int:id>', views.eliminar_Persona, name = 'eliminar_Persona'),
        path('eliminar/Local/Comida/<int:id>', views.eliminar_LocalComida, name = 'eliminar_LocalComida'),
        path('eliminar/Local/Respuesto/<int:id>', views.eliminar_LocalRespuestos, name = 'eliminar_LocalRespuestos'),
        


 ]