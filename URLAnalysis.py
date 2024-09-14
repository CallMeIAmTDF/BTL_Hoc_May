import ipaddress
import json
import re
import socket
import ssl
from datetime import date, datetime
import dns
import requests
import sympy
from dateutil.parser import parse as date_parse

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/50.0.2661.102 Safari/537.36'}

ids = ['NONE', 'A', 'NS', 'MD', 'MF', 'CNAME', 'SOA', 'MB', 'MG', 'MR', 'NULL', 'WKS', 'PTR', 'HINFO', 'MINFO', 'MX',
       'TXT', 'RP', 'AFSDB', 'X25', 'ISDN', 'RT', 'NSAP', 'NSAP-PTR', 'SIG', 'KEY', 'PX', 'GPOS', 'AAAA', 'LOC', 'NXT',
       'SRV', 'NAPTR', 'KX', 'CERT', 'A6', 'DNAME', 'OPT', 'APL', 'DS', 'SSHFP', 'IPSECKEY', 'RRSIG', 'NSEC', 'DNSKEY',
       'DHCID', 'NSEC3', 'NSEC3PARAM', 'TLSA', 'HIP', 'CDS', 'CDNSKEY', 'CSYNC', 'SPF', 'UNSPEC', 'EUI48', 'EUI64',
       'TKEY', 'TSIG', 'IXFR', 'AXFR', 'MAILB', 'MAILA', 'ANY', 'URI', 'CAA', 'TA', 'DLV']


# having_IP_Address


def diff_month(d1, d2):
    return (d1.year - d2.year) * 12 + d1.month - d2.month


def years_difference(date_str):
    given_date = datetime.strptime(date_str, '%b %d %H:%M:%S %Y GMT')
    now = datetime.utcnow()
    years_diff = now.year - given_date.year
    if (now.month, now.day) < (given_date.month, given_date.day):
        years_diff -= 1
    return years_diff


def having_ip_address(url):
    try:
        ipaddress.ip_address(url)
        return 1
    except IndexError:
        return -1


# URL_Length
def url_length(url):
    if len(url) < 54:
        return 1
    elif 54 <= len(url) <= 75:
        return 0
    else:
        return -1


# Shortining_Service
def shortining_service(url):
    if re.findall(
            "goo.gl|bit.ly|t.co|tinyurl.com|ow.ly|buff.ly|is.gd|bl.ink|cutt.ly|rb.gy|mcaf.ee|shorte.st|soo.gd|v.gd",
            url):
        return 1
    else:
        return -1


# having_At_Symbol
def having_at_symbol(url):
    if re.findall("@", url):
        return 1
    else:
        return -1


# double_slash_redirecting
def double_slash_redirecting(url):
    if re.findall(r"[^https?:]//", url):
        return -1
    else:
        return 1


# Prefix_Suffix
def prefix_suffix(url):
    if re.findall(r"https?://[^\-]+-[^\-]+/", url):
        return -1
    else:
        return 1


# having_Sub_Domain
def having_sub_domain(url):
    pass


# SSLfinal_State
def ssl_final_state(url, hostname):
    try:
        port = 443
        context = ssl.create_default_context()
        with socket.create_connection((hostname, port)) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                cert = ssock.getpeercert()
                if cert:
                    if years_difference(cert['notBefore']) >= 1:
                        return 1
                    return 0
                return -1
    except IndexError:
        return -1


# Domain_registeration_length
def domain_registeration_length(url):
    pass


# Favicon
def favicon(url):
    pass


# port
def port(url, domain):
    try:
        port = domain.split(":")[1]
        if port:
            return 1
        else:
            return -1
    except IndexError:
        return -1


# HTTPS_token
def https_token(url, domain):
    if re.findall("^https\-", domain):
        return -1
    else:
        return 1


# Request_URL
def request_url(url):
    pass


# URL_of_Anchor
def url_of_anchor(url):
    pass


# Links_in_tags
def links_in_tags(url):
    pass


# SFH
def sfh(url):
    return -1


# Submitting_to_email
def submitting_to_email(url, response):
    if re.findall(r"[mail()|mailto:?]", response.text):
        return 1
    else:
        return -1


# Abnormal_URL
def abnormal_url(url, response):
    if response.text == "":
        return 1
    else:
        return -1


# Redirect
def redirect(url, response):
    if len(response.history) <= 4:
        return 0
    else:
        return 1


# on_mouseover
def on_mouseover(url, response):
    if re.findall("<script>.+onmouseover.+</script>", response.text):
        return 1
    else:
        return -1


# RightClick
def right_click(url, response):
    if re.findall(r"event.button ?== ?2", response.text):
        return 1
    else:
        return -1


# popUpWidnow
def popup_window(url, response):
    if re.findall(r"alert\(", response.text):
        return 1
    else:
        return -1


# Iframe
def iframe(url, response):
    if re.findall(r"[<iframe>|<frameBorder>]", response.text):
        return 1
    else:
        return -1


# age_of_domain
def age_of_domain(url, whois_response):
    try:
        registration_date = \
            re.findall(r'Registration Date:</div><div class="df-value">([^<]+)</div>', whois_response.text)[0]
        if diff_month(date.today(), date_parse(registration_date)) >= 6:
            return -1
        else:
            return 1
    except IndexError:
        return 1


# DNSRecord
def dns_recode(url, domain):
    for a in ids:
        try:
            answers = dns.resolver.query(domain, a)
            if answers:
                return 1
        except Exception as e:
            pass
    return -1


# web_traffic
def web_traffic(url):
    # alexa không còn hoạt động
    url = (f"https://pro.similarweb.com/widgetApi/WebsiteOverview/WebRanks/SingleMetric?country=999&from=2024%7C08"
           f"%7C01&to=2024%7C08%7C31&includeSubDomains=true&isWindow=false&keys={
           url}&timeGranularity=Monthly&webSource=Total")
    try:
        data = json.loads(requests.get(url).text)
        first_key = next(iter(data))
        if data["Data"][first_key]["GlobalRank"]["Value"] < 100000:
            return 1
        else:
            return 0
    except Exception as e:
        return -1


# Page_Rank
def page_rank(url, rank_checker_response):
    try:
        data = re.findall(r"<span[^>]*>(.*?)</span>",
                          re.findall(r"<h2><b>(.*?)</b></h2><br/?>", rank_checker_response.text)[0])[0]
        if data[0] == "/":
            data = "0" + data
        rank = sympy.simplify(data)
        if rank < 0.2:
            return -1
        else:
            return 1
    except IndexError:
        return -1


# Google_Index
def google_index(url, rank_checker_response):
    data = re.findall(r"Indexed URLs:\s*([\d,]+)<br\/?>", rank_checker_response.text)[0]
    if data != "":
        return 1
    else:
        return -1


# Links_pointing_to_page
def links_pointing_to_page(url, response):
    number_of_links = len(re.findall(r"<a href=", response.text))
    if number_of_links == 0:
        return 1
    elif number_of_links <= 2:
        return 0
    else:
        return -1


# Statistical_report
def statistical_report(url):
    pass


def url_analysis(url):
    res = requests.get(url)
    domain = re.findall(r"://([^/]+)/?", url)[0]
    whois_response = requests.get("https://www.whois.com/whois/" + domain)
    rank_checker_response = requests.post("https://www.checkpagerank.net/index.php", {
        "name": domain
    }, headers=headers)

    return [
        having_ip_address(url),
        url_length(url),
        shortining_service(url),
        having_at_symbol(url),
        double_slash_redirecting(url),
        prefix_suffix(url),
        having_sub_domain(url),
        ssl_final_state(url, domain),
        domain_registeration_length(url),
        favicon(url),
        port(url, domain),
        https_token(url, domain),
        request_url(url),
        url_of_anchor(url),
        links_in_tags(url),
        sfh(url),
        submitting_to_email(url, res),
        abnormal_url(url, res),
        redirect(url, res),
        on_mouseover(url, res),
        right_click(url, res),
        popup_window(url, res),
        age_of_domain(url, whois_response),
        dns_recode(url, domain),
        web_traffic(url),
        page_rank(url, rank_checker_response),
        google_index(url, rank_checker_response),
        links_pointing_to_page(url, res),
        statistical_report(url)
    ]
