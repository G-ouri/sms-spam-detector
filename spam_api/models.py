from django.db import models

class ScanResult(models.Model):
    message     = models.TextField()
    verdict     = models.CharField(max_length=10)   # spam / safe / unknown
    confidence  = models.IntegerField()
    explanation = models.TextField()
    scanned_at  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"[{self.verdict}] {self.message[:50]}"
