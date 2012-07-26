import datetime
import httplib
import json
import time
import urllib


class Site:
    def __init__(self, name, site_token, url):
        self._name = name
        self._site_token = site_token
        self._url = url

    def get_name(self):
        return self._name

    def get_site_token(self):
        return self._site_token

    def get_url(self):
        return self._url


class Visitor:
    def __init__(
        self, visitor_id, site_token, hidden, visits, lead_scores,
        company_information, avg_page_views_per_visit, avg_visit_duration,
        is_lead, total_page_views, total_visits, last_visit_date,
        last_visit_referral_type, is_isp, organization_name, city,
        state_province, postal_code, country, last_form_submission,
        default_lead_score
    ):
        self._visitor_id = visitor_id
        self._site_token = site_token
        self._hidden = hidden
        self._visits = visits
        self._lead_scores = lead_scores
        self._company_information = company_information
        self._avg_page_views_per_visit = avg_page_views_per_visit
        self._avg_visit_duration = avg_visit_duration
        self._is_lead = is_lead
        self._total_page_views = total_page_views
        self._total_visits = total_visits
        self._last_visit_date = last_visit_date
        self._last_visit_referral_type = last_visit_referral_type
        self._is_isp = is_isp
        self._organization_name = organization_name
        self._city = city
        self._state_province = state_province
        self._postal_code = postal_code
        self._country = country
        self._last_form_submission = last_form_submission
        self._default_lead_score = default_lead_score

    def get_visitor_id(self):
        return self._visitor_id

    def get_site_token(self):
        return self._site_token

    def is_hidden(self):
        return self._hidden

    def get_visits(self):
        return self._visits

    def get_lead_scores(self):
        return self._lead_scores

    def get_company_information(self):
        return self._company_information

    def get_avg_page_views_per_visit(self):
        return self._avg_page_views_per_visit

    def get_avg_visit_duration(self):
        return self._avg_visit_duration

    def is_lead(self):
        return self._is_lead

    def get_total_page_views(self):
        return self._total_page_views

    def get_total_visits(self):
        return self._total_visits

    def get_last_visit_date(self):
        return self._last_visit_date

    def get_last_visit_referral_type(self):
        return self._last_visit_referral_type

    def is_isp(self):
        return self._is_isp

    def get_organization_name(self):
        return self._organization_name

    def get_city(self):
        return self._city

    def get_state_province(self):
        return self._state_province

    def get_postal_code(self):
        return self._postal_code

    def get_country(self):
        return self._country

    def get_last_form_submission(self):
        return self._last_form_submission

    def get_default_lead_score(self):
        return self._default_lead_score


class Visit:
    def __init__(
        self, visit_id, visit_date, keyword, referral_serp_rank,
        custom_referral_detail, custom_referral_type, referral_search_engine,
        referral_type, page_views, forms, user_agent
    ):
        self._visit_id = visit_id
        self._visit_date = visit_date
        self._keyword = keyword
        self._referral_serp_rank = referral_serp_rank
        self._custom_referral_detail = custom_referral_detail
        self._custom_referral_type = custom_referral_type
        self._referral_search_engine = referral_search_engine
        self._referral_type = referral_type
        self._page_views = page_views
        self._forms = forms
        self._user_agent = user_agent

    def get_visit_id(self):
        return self._visit_id

    def get_visit_date(self):
        return self._visit_date

    def get_keyword(self):
        return self._keyword

    def get_referral_serp_rank(self):
        return self._referral_serp_rank

    def get_custom_referral_detail(self):
        return self._custom_referral_detail

    def get_custom_referral_type(self):
        return self._custom_referral_type

    def get_referral_search_engine(self):
        return self._referral_search_engine

    def get_referral_type(self):
        return self._referral_type

    def get_page_views(self):
        return self._page_views

    def get_forms(self):
        return self._forms

    def get_user_agent(self):
        return self._user_agent


class PageView:
    def __init__(self, url, referral_url, page_title, ip_address, date_viewed):
        self._url = url
        self._referral_url = referral_url
        self._page_title = page_title
        self._ip_address = ip_address
        self._date_viewed = date_viewed

    def get_url(self):
        return self._url

    def get_referral_url(self):
        return self._referral_url

    def get_page_title(self):
        return self._page_title

    def get_ip_address(self):
        return self._ip_address

    def get_date_viewed(self):
        return self._date_viewed


class Form:
    def __init__(
        self, job_title, first_name, last_name, email_address, company, city,
        state_province, postal_code, phone_number, website, industry,
        salutation, street, country, employees, revenue, mobile, fax, rating,
        form_title, form_url, visit_id, site_token, submission_date
    ):
        self._job_title = job_title
        self._first_name = first_name
        self._last_name = last_name
        self._email_address = email_address
        self._company = company
        self._city = city
        self._state_province = state_province
        self._postal_code = postal_code
        self._phone_number = phone_number
        self._website = website
        self._industry = industry
        self._salutation = salutation
        self._street = street
        self._country = country
        self._employees = employees
        self._revenue = revenue
        self._mobile = mobile
        self._fax = fax
        self._rating = rating
        self._form_title = form_title
        self._form_url = form_url
        self._visit_id = visit_id
        self._site_token = site_token
        self._submission_date = submission_date

    def get_job_title(self):
        return self._job_title

    def get_first_name(self):
        return self._first_name

    def get_last_name(self):
        return self._last_name

    def get_email_address(self):
        return self._email_address

    def get_company(self):
        return self._company

    def get_city(self):
        return self._city

    def get_state_province(self):
        return self._state_province

    def get_postal_code(self):
        return self._postal_code

    def get_phone_number(self):
        return self._phone_number

    def get_website(self):
        return self._website

    def get_industry(self):
        return self._industry

    def get_salutation(self):
        return self._salutation

    def get_street(self):
        return self._street

    def get_country(self):
        return self._country

    def get_employees(self):
        return self._employees

    def get_revenue(self):
        return self._revenue

    def get_mobile(self):
        return self._mobile

    def get_fax(self):
        return self._fax

    def get_rating(self):
        return self._rating

    def get_form_title(self):
        return self._form_title

    def get_form_url(self):
        return self._form_url

    def get_visit_id(self):
        return self._visit_id

    def get_site_token(self):
        return self._site_token

    def get_submission_date(self):
        return self._submission_date


class LeadScore:
    def __init__(
        self, rule_set_name, lead_score, previous_lead_score,
        max_lifetime_lead_score, hidden
    ):
        self._rule_set_name = rule_set_name
        self._lead_score = lead_score
        self._previous_lead_score = previous_lead_score
        self._max_lifetime_lead_score = max_lifetime_lead_score
        self._hidden = hidden

    def get_rule_set_name(self):
        return self._rule_set_name

    def get_lead_score(self):
        return self._lead_score

    def get_previous_lead_score(self):
        return self._previous_lead_score

    def get_max_lifetime_lead_score(self):
        return self._max_lifetime_lead_score

    def get_hidden(self):
        return self._hidden


class CompanyInformation:
    def __init__(
        self, name, phone_number, website, stock_symbol, stock_exchange,
        ownership, employee_count, employee_range, revenue, revenue_range,
        industry, sub_industry, sic_code, address, city, state_province,
        postal_code, country
    ):
        self._name = name
        self._phone_number = phone_number
        self._website = website
        self._stock_symbol = stock_symbol
        self._stock_exchange = stock_exchange
        self._ownership = ownership
        self._employee_count = employee_count
        self._employee_range = employee_range
        self._revenue = revenue
        self._revenue_range = revenue_range
        self._industry = industry
        self._sub_industry = sub_industry
        self._sic_code = sic_code
        self._address = address
        self._city = city
        self._state_province = state_province
        self._postal_code = postal_code
        self._country = country

    def get_name(self):
        return self._name

    def get_phone_number(self):
        return self._phone_number

    def get_website(self):
        return self._website

    def get_stock_symbol(self):
        return self._stock_symbol

    def get_stock_exchange(self):
        return self._stock_exchange

    def get_ownership(self):
        return self._ownership

    def get_employee_count(self):
        return self._employee_count

    def get_employee_range(self):
        return self._employee_range

    def get_revenue(self):
        return self._revenue

    def get_revenue_range(self):
        return self._revenue_range

    def get_industry(self):
        return self._industry

    def get_sub_industry(self):
        return self._sub_industry

    def get_sic_code(self):
        return self._sic_code

    def get_address(self):
        return self._address

    def get_city(self):
        return self._city

    def get_state_province(self):
        return self._state_province

    def get_postal_code(self):
        return self._postal_code

    def get_country(self):
        return self._country


class BadRequestException(Exception):
    pass


class UnauthorizedException(Exception):
    pass


class NotFoundException(Exception):
    pass


class InternalException(Exception):
    pass


class OptifyService:
    _host = 'api.optify.net'
    _datetime_format = '%Y-%m-%d %H:%M:%S'

    def __init__(self, access_token):
        self._access_token = access_token

    def who_am_i(self):
        return self._get('/whoami', 'access_token=' + self._access_token)

    def get_sites(self):
        res = self._get('/v1/sites', 'access_token=' + self._access_token)
        return map(OptifyService._get_site_from_hash, json.loads(res))

    def get_site(self, site_token):
        res = self._get(
            '/v1/sites/' + site_token,
            'access_token=' + self._access_token
        )

        return OptifyService._get_site_from_hash(json.loads(res))

    def get_visitors(
        self, site_token,
        start_date=datetime.datetime.utcnow() + datetime.timedelta(days=-1),
        end_date=datetime.datetime.utcnow(), include_isp=False, offset=0,
        count=10
    ):
        path = '/v1/sites/' + site_token + '/visitors'
        query = urllib.urlencode({
            'start_date': start_date.strftime(self._datetime_format),
            'end_date': end_date.strftime(self._datetime_format),
            'include_isp': include_isp,
            'offset': offset,
            'count': count,
            'access_token': self._access_token
        })

        res = self._get(path, query)
        return map(OptifyService._get_visitor_from_hash, json.loads(res))

    def get_visitor(self, site_token, visitor_id):
        path = '/v1/sites/' + site_token + '/visitors/' + visitor_id
        query = 'access_token=' + self._access_token
        res = self._get(path, query)
        return OptifyService._get_visitor_from_hash(json.loads(res))

    def _get(self, path, query):
        connection = httplib.HTTPSConnection(self._host)
        headers = {
            'Accept': 'application/json, text/plain',
            'X-Optify-Client-Version': '1.0.0-Python'
        }

        connection.request('GET', path + '?' + query, None, headers)

        res = connection.getresponse()
        if (res.status == httplib.BAD_REQUEST):
            raise BadRequestException()
        elif (res.status == httplib.UNAUTHORIZED):
            raise UnauthorizedException()
        elif (res.status == httplib.NOT_FOUND):
            raise NotFoundException()
        elif (res.status == httplib.OK):
            return res.read()

        raise InternalException()

    @staticmethod
    def _get_site_from_hash(h):
        name = h['name']
        site_token = h['site_token']
        url = h['url']
        return Site(name, site_token, url)

    @staticmethod
    def _get_visitor_from_hash(h):
        visitor_id = h['visitor_id']
        site_token = h['site_token']
        hidden = h['hidden']
        visits = map(OptifyService._get_visit_from_hash, h['visits'])
        lead_scores = map(OptifyService._get_lead_score_from_hash, h['leadScores'])

        company_information = map(
            OptifyService._get_company_information_from_hash,
            h['company_information']
        )

        avg_page_views_per_visit = h['avg_pageviews_per_visit']
        avg_visit_duration = h['avg_visit_duration']
        is_lead = h['is_lead']
        total_page_views = h['total_page_views']
        total_visits = h['total_visits']

        last_visit_date = datetime.datetime.fromtimestamp(
            h['last_visit_date'] / 1000
        )

        last_visit_referral_type = h['last_visit_referral_type']
        is_isp = h['is_isp']
        organization_name = h['organization_name']
        city = h['city']
        state_province = h['state_province']
        postal_code = h['postal_code']
        country = h['country']
        last_form_submission = None
        default_lead_score = h['default_lead_score']

        if ('last_form_submission' in h):
            last_form_submission = OptifyService._get_form_from_hash(
                h['last_form_submission']
            )

        return Visitor(
            visitor_id, site_token, hidden, visits, lead_scores,
            company_information, avg_page_views_per_visit, avg_visit_duration,
            is_lead, total_page_views, total_visits, last_visit_date,
            last_visit_referral_type, is_isp, organization_name, city,
            state_province, postal_code, country, last_form_submission,
            default_lead_score
        )

    @staticmethod
    def _get_visit_from_hash(h):
        visit_id = h['visit_id']
        visit_date = datetime.datetime.fromtimestamp(h['visit_date'] / 1000)
        keyword = h['keyword']
        referral_serp_rank = h['referral_serp_rank']
        custom_referral_detail = h['custom_referral_detail']
        custom_referral_type = h['custom_referral_type']
        referral_search_engine = h['referral_search_engine']
        referral_type = h['referral_type']
        page_views = map(OptifyService._get_page_view_from_hash, h['pageviews'])
        forms = map(OptifyService._get_form_from_hash,  h['forms'])
        user_agent = h['user_agent']

        return Visit(
            visit_id, visit_date, keyword, referral_serp_rank,
            custom_referral_detail, custom_referral_type,
            referral_search_engine, referral_type, page_views, forms,
            user_agent
        )

    @staticmethod
    def _get_page_view_from_hash(h):
        url = h['url']
        referral_url = h['referral_url']
        page_title = h['page_title']
        ip_address = h['ip_address']
        date_viewed = datetime.datetime.fromtimestamp(h['date_viewed'] / 1000)

        return PageView(url, referral_url, page_title, ip_address, date_viewed)

    @staticmethod
    def _get_form_from_hash(h):
        job_title = h['job_title']
        first_name = h['first_name']
        last_name = h['last_name']
        email_address = h['email_address']
        company = h['company']
        city = h['city']
        state_province = h['state_province']
        postal_code = h['postal_code']
        phone_number = h['phone_number']
        website = h['website']
        industry = h['industry']
        salutation = h['salutation']
        street = h['street']
        country = h['country']
        employees = h['employees']
        revenue = h['revenue']
        mobile = h['mobile']
        fax = h['fax']
        rating = h['rating']
        form_title = h['form_title']
        form_url = h['form_url']
        visit_id = h['visit_id']
        site_token = h['site_token']
        submission_date = h['submission_date']

        return Form(
            job_title, first_name, last_name, email_address, company, city,
            state_province, postal_code, phone_number, website, industry,
            salutation, street, country, employees, revenue, mobile, fax,
            rating, form_title, form_url, visit_id, site_token, submission_date
        )

    @staticmethod
    def _get_lead_score_from_hash(h):
        rule_set = h['rule_set']
        lead_score = h['lead_score']
        previous_lead_score = h['previous_lead_score']
        max_lifetime_lead_score = h['max_lifetime_lead_score']
        hidden = h['hidden']

        return LeadScore(
            rule_set, lead_score, previous_lead_score, max_lifetime_lead_score,
            hidden
        )

    @staticmethod
    def _get_company_information_from_hash(h):
        name = h['name']
        phone_number = h['phone_number']
        website = h['website']
        stock_symbol = h['stock_symbol']
        stock_exchange = h['stock_exchange']
        ownership = h['ownership']
        employee_count = h['employee_count']
        employee_range = h['employee_range']
        revenue = h['revenue']
        revenue_range = h['revenue_range']
        industry = h['industry']
        sub_industry = h['sub_industry']
        sic_code = h['sic_code']
        address = h['address']
        city = h['city']
        state_province = h['state_province']
        postal_code = h['postal_code']
        country = h['country']

        return CompanyInformation(
            name, phone_number, website, stock_symbol, stock_exchange,
            ownership, employee_count, employee_range, revenue, revenue_range,
            industry, sub_industry, sic_code, address, city, state_province,
            postal_code, country
        )
