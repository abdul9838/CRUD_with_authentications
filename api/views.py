from rest_framework.viewsets import ModelViewSet
from .models import Student
from .serializers import StudentSerializer
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated , IsAdminUser ,DjangoModelPermissions, IsAuthenticatedOrReadOnly  ,DjangoModelPermissionsOrAnonReadOnly,DjangoObjectPermissions

class StudentApi(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [SessionAuthentication]
    # permission_classes = [IsAdminUser]
    # permission_classes = [IsAuthenticatedOrReadOnly]
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    # permission_classes = [DjangoObjectPermissions]