from datetime import datetime

from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from forms.models import Form, Call, TimeSlot
from forms.serializers import FormSerializer, CallSerializer
from utils.contract_by_agent_token_mixin import ContractByAgentTokenMixin
from utils.drf_permissions.agent_token_permission import AgentTokenPermission


class FormList(ListAPIView):
    """
    List of all forms for settings page.

    Note: that `agent_token` must be provided
    """

    queryset = Form.objects.filter(is_active=True)
    serializer_class = FormSerializer
    permission_classes = [AgentTokenPermission]
    authentication_classes = []


class RetrieveUpdateCall(RetrieveUpdateAPIView):
    """
    Update call from voximplant scenario.

    Note: that `agent_token` must be provided
    """

    queryset = Call.objects.all()
    serializer_class = CallSerializer
    permission_classes = [AgentTokenPermission]
    authentication_classes = []


class GetNextTimeSlot(APIView, ContractByAgentTokenMixin):
    """
    Get next available time slot for contract and get time (`HH:MM:SS`) and `is_tomorrow` flag.

    Note: that `agent_token` must be provided
    """

    def get(self, request):
        time, is_tomorrow = TimeSlot.get_next_timeslot(datetime.now(), contract=self.get_contract())
        return Response({'time': time, 'is_tomorrow': is_tomorrow})
