from django.shortcuts import render
from rest_framework import viewsets
from .models import Livro, Autor, Editora, Emprestimo, Reserva, Usuario
from .serializers import LivroSerializer, AutorSerializer, EditoraSerializer, EmprestimoSerializer, ReservaSerializer, UsuarioSerializer
import requests

from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from django.db.models import Count, Max, Min, Sum

class LivroViewSet(viewsets.ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer 

    @action(detail=False, methods=['get'])
    def autores_livros(self, request):
        livro_id = request.query_params.get('livro_id')
        autor = Autor.objects.filter(livro_id=livro_id)
        serializer = AutorSerializer(autor, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def editoras_livros(self, request):
        livro_id = request.query_params.get('livro_id')
        editora = Editora.objects.filter(livro_id=livro_id)
        serializer = EditoraSerializer(editora, many=True)
        return Response(serializer.data)

class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

    @action(detail=False, methods=['get'])
    def livro_autor(self, request):
        livro_id = request.query_params.get('livro_id')
        autor_livro = Autor.objects.filter(livro_id=livro_id)
        serializer = AutorSerializer(autor_livro, many=True)
        return Response(serializer.data)

class EditoraViewSet(viewsets.ModelViewSet):
    queryset = Editora.objects.all()
    serializer_class = EditoraSerializer 

class EmprestimoViewSet(viewsets.ModelViewSet):
    queryset = Emprestimo.objects.all()
    serializer_class = EmprestimoSerializer 

    @action(detail=False, methods=['get'])
    def emprestimo_livros(self, request):
        livro_id = request.query_params.get('livro_id')
        emprestimo = Emprestimo.objects.filter(livro_id=livro_id)
        serializer = EmprestimoSerializer(emprestimo, many=True)
        return Response(serializer.data)

class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer 

    @action(detail=False, methods=['get'])
    def reserva_livros(self, request):
        livro_id = request.query_params.get('livro_id')
        reserva = Reserva.objects.filter(livro_id=livro_id)
        serializer = ReservaSerializer(reserva, many=True)
        return Response(serializer.data)

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer 

    @action(detail=False, methods=['get'])
    def emprestimo_user(self, request):
        emprestimo_id = request.query_params.get('emprestimo_id')
        usuario = Usuario.objects.filter(emprestimo_id=emprestimo_id)
        serializer = UsuarioSerializer(usuario, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def reserva_user(self, request):
        reserva_id = request.query_params.get('reserva_id')
        usuario_reserva = Reserva.objects.filter(reserva_id=reserva_id)
        serializer = ReservaSerializer(usuario_reserva, many=True)
        return Response(serializer.data)


BASE_URL = 'http://localhost:8000/api/'

def get_livros():
    response = requests.get(BASE_URL + 'livros/')
    if response.status_code == 200:
        return response.json()
    else:
        return None
    
if __name__ == '__main__':
    livros = get_livros()
    for livro in livros:
        print('Livro', livro)
