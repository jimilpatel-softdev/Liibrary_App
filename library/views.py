from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Book, Member, Loan
from .serializers import BookSerializer, MemberSerializer, LoanSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
        queryset = Book.objects.all()
        title = self.request.query_params.get('title', None)
        author = self.request.query_params.get('author', None)
        genre = self.request.query_params.get('genre', None)

        if title:
            queryset = queryset.filter(title__icontains=title)
        if author:
            queryset = queryset.filter(author__icontains=author)
        if genre:
            queryset = queryset.filter(genre__icontains=genre)

        return queryset

class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['get'])
    def my_loans(self, request, pk=None):
        member = self.get_object()
        loans = Loan.objects.filter(member=member)
        return Response(LoanSerializer(loans, many=True).data)

# class LoanViewSet(viewsets.ModelViewSet):
#     queryset = Loan.objects.all()
#     serializer_class = LoanSerializer
#     permission_classes = [IsAuthenticated]

#     @action(detail=True, methods=['post'])
#     def borrow(self, request, pk=None):
#         book = self.get_object()
#         member = request.user.member  # Assuming a User has a related Member model
#         if book.copies_available <= 0:
#             return Response({"error": "No copies available"}, status=status.HTTP_400_BAD_REQUEST)
#         loan = Loan.objects.create(book=book, member=member, due_date=timezone.now().date() + timedelta(days=14))
#         book.available_copies -= 1
#         book.save()
#         return Response(LoanSerializer(loan).data, status=status.HTTP_201_CREATED)

#     @action(detail=True, methods=['post'])
#     def return_book(self, request, pk=None):
#         loan = self.get_object()
#         if loan.return_date:
#             return Response({"error": "Book already returned"}, status=status.HTTP_400_BAD_REQUEST)
#         loan.return_date = timezone.now().date()
#         fine = loan.calculate_fine()
#         loan.save()
#         return Response({"message": "Book returned", "fine": fine}, status=status.HTTP_200_OK)




class LoanViewSet(viewsets.ModelViewSet):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['post'])
    def borrow(self, request, pk=None):
        book = self.get_object()  # Retrieve the book using pk from the URL
        member = request.user.member  # Get the authenticated member (assuming the member is linked to the user)
        
        # Check if there are available copies of the book
        if book.available_copies <= 0:
            return Response({"error": "No copies available"}, status=status.HTTP_400_BAD_REQUEST)
        
        # Create a new loan record
        loan = Loan.objects.create(
            book=book,
            member=member,
            due_date=timezone.now().date() + timedelta(days=14)  # Set due date for 14 days
        )
        
        # Decrease the number of available copies
        book.available_copies -= 1
        book.save()
        
        # Return the loan details as response
        return Response(LoanSerializer(loan).data, status=status.HTTP_201_CREATED)
