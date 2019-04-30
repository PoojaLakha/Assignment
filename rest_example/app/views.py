from rest_framework import generics
from .serializers import AccountSerializer
from .models import Account


class CreateView(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    def create_account(self, serializer):
        """Save the post data to create a new account."""
        serializer.save()


class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles GET, PUT and DELETE requests."""

    queryset = Account.objects.all()
    serializer_class = AccountSerializer
