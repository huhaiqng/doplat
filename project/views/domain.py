import json
from django.conf import settings
from aliyunsdkalidns.request.v20150109.DescribeDomainRecordsRequest import DescribeDomainRecordsRequest
from aliyunsdkalidns.request.v20150109.DescribeDomainsRequest import DescribeDomainsRequest
from rest_framework.views import APIView
from rest_framework.response import Response


class GetGaingon666Domain(APIView):
    def get(self, request, format=None):
        client = settings.ALIAPI_GAINHON666
        page = request.GET.get('page')
        per_page = request.GET.get('per_page')

        req = DescribeDomainsRequest()
        req.set_accept_format('json')

        req.set_PageNumber(page)
        req.set_PageSize(per_page)

        res = client.do_action_with_exception(req).decode('utf-8')
        return Response(json.loads(res))


class GetGaingon666DomainRecord(APIView):
    def get(self, request, format=None):
        domain_name = request.GET.get('domain_name')
        page = request.GET.get('page')
        per_page = request.GET.get('per_page')

        client = settings.ALIAPI_GAINHON666
        req = DescribeDomainRecordsRequest()
        req.set_accept_format('json')

        req.set_DomainName(domain_name)
        req.set_PageNumber(page)
        req.set_PageSize(per_page)

        res = client.do_action_with_exception(req).decode('utf-8')

        return Response(json.loads(res))


class GetLingfannaoDomain(APIView):
    def get(self, request, format=None):
        client = settings.ALIAPI_LINGFANNAO
        page = request.GET.get('page')
        per_page = request.GET.get('per_page')

        req = DescribeDomainsRequest()
        req.set_accept_format('json')

        req.set_PageNumber(page)
        req.set_PageSize(per_page)

        res = client.do_action_with_exception(req).decode('utf-8')
        return Response(json.loads(res))


class GetLingfannaoDomainRecord(APIView):
    def get(self, request, format=None):
        domain_name = request.GET.get('domain_name')
        page = request.GET.get('page')
        per_page = request.GET.get('per_page')

        client = settings.ALIAPI_LINGFANNAO
        req = DescribeDomainRecordsRequest()
        req.set_accept_format('json')

        req.set_DomainName(domain_name)
        req.set_PageNumber(page)
        req.set_PageSize(per_page)

        res = client.do_action_with_exception(req).decode('utf-8')

        return Response(json.loads(res))
