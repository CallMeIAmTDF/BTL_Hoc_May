import ipaddress
import re
import requests
from datetime import date
from dateutil.parser import parse as date_parse


# having_IP_Address
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
def ssl_final_state(url):
    pass


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
    pass


# Submitting_to_email
def submitting_to_email(url, response):
    if re.findall(r"[mail\(\)|mailto:?]", response.text):
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
def age_of_domain(url):
    pass


# DNSRecord
def dns_recode(url):
    return -1


# web_traffic
def web_traffic(url):
    pass


# Page_Rank
def page_rank(url):
    pass


# Google_Index
def google_index(url):
    pass


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
