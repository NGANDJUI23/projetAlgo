from django.db import models

class DocumentComparison(models.Model):
    document_1 = models.TextField()
    document_2 = models.TextField()
    similarity_score = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comparison {self.id} - Similarity: {self.similarity_score:.2f}"
