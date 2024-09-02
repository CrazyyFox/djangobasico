from django.urls import path
from . import views

urlpatterns = [
    # aqui se mantem o padrão vazio, pois o arquivo urls do projeto
    # já inclui o arquivo urls da aplicação e este aponta para a raiz
    # path('o caminho', o que será abberto)
    
    path('', views.pagina_produtos),
    
    # por exemplo, se dentro de /produtos/ quisérmos mostrar celular
    # fáriamos da seguinte forma:
    # patch('celulares/',),
    path('celulares/', views.celulares)
    # seria algo tipo meusite.com/produtos/celulares/
]
