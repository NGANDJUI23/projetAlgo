from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from difflib import SequenceMatcher
from .models import DocumentComparison
from .serializers import DocumentComparisonSerializer

def calculate_similarity(doc1, doc2):
    """Calcule la similarité entre deux documents."""
    return SequenceMatcher(None, doc1, doc2).ratio()

class CompareDocumentsView(APIView):
    def post(self, request):
        doc1 = request.data.get('doc1')
        doc2 = request.data.get('doc2')
        if not doc1 or not doc2:
            return Response({'error': "Both 'doc1' and 'doc2' are required."}, status=status.HTTP_400_BAD_REQUEST)

        similarity = calculate_similarity(doc1, doc2)
        comparison = DocumentComparison.objects.create(
            document_1=doc1,
            document_2=doc2,
            similarity_score=similarity
        )
        serializer = DocumentComparisonSerializer(comparison)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class GroupDocumentsView(APIView):
    def post(self, request):
        documents = request.data.get('documents')
        if not documents or len(documents) < 2:
            return Response({'error': "'documents' must contain at least two entries."}, status=status.HTTP_400_BAD_REQUEST)

        n = len(documents)
        results = []

        for i in range(n):
            for j in range(i + 1, n):
                similarity = calculate_similarity(documents[i], documents[j])
                results.append({
                    "doc1": documents[i],
                    "doc2": documents[j],
                    "similarity": similarity
                })

        return Response(results, status=status.HTTP_200_OK)
