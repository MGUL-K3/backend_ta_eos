from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import CalculationSerializer
from .utils import generate_seq_of_objects, generate_seq_of_objects_r


class DirectCodeLeftShiftCalculation(APIView):
    serializer_class = CalculationSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = CalculationSerializer(data=request.query_params)

        if not serializer.is_valid():
            return Response(
                data=serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )

        obj_seq = generate_seq_of_objects(
            serializer.validated_data["first_value"],
            serializer.validated_data["second_value"],
        )

        return Response(obj_seq)


class DirectCodeRightShiftCalculation(APIView):
    serializer_class = CalculationSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = CalculationSerializer(data=request.query_params)

        if not serializer.is_valid():
            return Response(
                data=serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )

        obj_seq = generate_seq_of_objects_r(
            serializer.validated_data["first_value"],
            serializer.validated_data["second_value"],
        )

        return Response(obj_seq)
