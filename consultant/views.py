from django.shortcuts import render
from consultant.models import Answer
from consultant.serializers import AnswerSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

class AnswerListView(APIView):
    def get(self, request):
        answers = Answer.objects.all()
        serializer = AnswerSerializer(answers, many=True)
        return Response(serializer.data, status=200)
    
    def post(self, request):
        serializer = AnswerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
class AnswerDetailView(APIView):
    def get(self, request, pk):
        answer = get_object_or_404(Answer, id=pk)
        serializer = AnswerSerializer(answer)
        return Response(serializer.data, status=200)

    def put(self, request, pk):
        answer = get_object_or_404(Answer, id=pk)
        serializer = AnswerSerializer(answer, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        answer = get_object_or_404(Answer, id=pk)
        answer.delete()
        return Response(status=204)
                        