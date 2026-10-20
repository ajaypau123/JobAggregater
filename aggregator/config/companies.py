"""Directory of curated tech companies with official public ATS endpoints.

Each company is verified to provide an unauthenticated, public REST API
via Greenhouse, Lever, Ashby, or SmartRecruiters.
"""

from dataclasses import dataclass, field


@dataclass(frozen=True)
class ATSCompany:
    name: str                                # Display company name (e.g. "Meesho")
    ats_type: str                            # "greenhouse" | "lever" | "ashby" | "smartrecruiters"
    slug: str                                # Board token / subdomain slug
    extra_params: dict | None = None         # Optional query parameters (e.g. {"country": "in"})


# Curated list of top-tier companies actively hiring in India and/or Worldwide Remote
DEFAULT_ATS_COMPANIES: list[ATSCompany] = [
    # ── Greenhouse ─────────────────────────────────────────────────────────────
    ATSCompany(name="InMobi", ats_type="greenhouse", slug="inmobi"),
    ATSCompany(name="Databricks", ats_type="greenhouse", slug="databricks"),
    ATSCompany(name="Grafana Labs", ats_type="greenhouse", slug="grafanalabs"),
    ATSCompany(name="GitLab", ats_type="greenhouse", slug="gitlab"),
    ATSCompany(name="Canonical", ats_type="greenhouse", slug="canonical"),
    ATSCompany(name="Elastic", ats_type="greenhouse", slug="elastic"),
    ATSCompany(name="Stripe", ats_type="greenhouse", slug="stripe"),
    ATSCompany(name="Figma", ats_type="greenhouse", slug="figma"),
    ATSCompany(name="Cloudflare", ats_type="greenhouse", slug="cloudflare"),
    ATSCompany(name="Thoughtworks", ats_type="greenhouse", slug="thoughtworks"),
    ATSCompany(name="Karat", ats_type="greenhouse", slug="karat"),
    ATSCompany(name="MongoDB", ats_type="greenhouse", slug="mongodb"),
    ATSCompany(name="Twilio", ats_type="greenhouse", slug="twilio"),
    ATSCompany(name="Pinterest", ats_type="greenhouse", slug="pinterest"),
    ATSCompany(name="Airbnb", ats_type="greenhouse", slug="airbnb"),
    ATSCompany(name="Robinhood", ats_type="greenhouse", slug="robinhood"),
    ATSCompany(name="Instacart", ats_type="greenhouse", slug="instacart"),
    ATSCompany(name="HackerRank", ats_type="greenhouse", slug="hackerrank"),
    ATSCompany(name="Okta", ats_type="greenhouse", slug="okta"),
    ATSCompany(name="Coinbase", ats_type="greenhouse", slug="coinbase"),
    ATSCompany(name="Scale AI", ats_type="greenhouse", slug="scaleai"),
    ATSCompany(name="Lyft", ats_type="greenhouse", slug="lyft"),
    ATSCompany(name="Reddit", ats_type="greenhouse", slug="reddit"),
    ATSCompany(name="Gusto", ats_type="greenhouse", slug="gusto"),
    ATSCompany(name="Discord", ats_type="greenhouse", slug="discord"),
    ATSCompany(name="Checkr", ats_type="greenhouse", slug="checkr"),

    # ── Lever ──────────────────────────────────────────────────────────────────
    ATSCompany(name="Meesho", ats_type="lever", slug="meesho"),
    ATSCompany(name="CRED", ats_type="lever", slug="cred"),
    ATSCompany(name="Spotify", ats_type="lever", slug="spotify"),

    # ── Greenhouse Additional MNCs ─────────────────────────────────────────────
    ATSCompany(name="Datadog", ats_type="greenhouse", slug="datadog"),
    ATSCompany(name="Rubrik", ats_type="greenhouse", slug="rubrik"),
    ATSCompany(name="Mozilla", ats_type="greenhouse", slug="mozilla"),

    # ── Ashby ──────────────────────────────────────────────────────────────────
    ATSCompany(name="Linear", ats_type="ashby", slug="linear"),
    ATSCompany(name="Notion", ats_type="ashby", slug="notion"),
    ATSCompany(name="Cursor", ats_type="ashby", slug="cursor"),
    ATSCompany(name="Ramp", ats_type="ashby", slug="ramp"),
    ATSCompany(name="Perplexity", ats_type="ashby", slug="perplexity"),

    # ── SmartRecruiters ────────────────────────────────────────────────────────
    ATSCompany(name="Bosch Group", ats_type="smartrecruiters", slug="BoschGroup", extra_params={"country": "in"}),
    ATSCompany(name="Ubisoft", ats_type="smartrecruiters", slug="Ubisoft2", extra_params={"country": "in"}),
    ATSCompany(name="Avery Dennison", ats_type="smartrecruiters", slug="AveryDennison", extra_params={"country": "in"}),
]


@dataclass(frozen=True)
class WorkdayCompany:
    """Configuration for an enterprise company using Workday's public CXS API."""
    name: str                                # Display company name (e.g. "PwC", "Nvidia")
    subdomain: str                           # Subdomain prefix (e.g. "pwc.wd3", "nvidia.wd5")
    tenant: str                              # Workday tenant ID (e.g. "pwc", "nvidia")
    site: str                                # Career site slug (e.g. "Global_Experienced_Careers")
    country_filter: str = "India"            # Search keyword or country filter


# Curated Big 4 & Global Tech MNCs using Workday with verified public endpoints
DEFAULT_WORKDAY_COMPANIES: list[WorkdayCompany] = [
    WorkdayCompany(name="PwC", subdomain="pwc.wd3", tenant="pwc", site="Global_Experienced_Careers"),
    WorkdayCompany(name="Nvidia", subdomain="nvidia.wd5", tenant="nvidia", site="NVIDIAExternalCareerSite"),
    WorkdayCompany(name="Mastercard", subdomain="mastercard.wd1", tenant="mastercard", site="CorporateCareers"),
    WorkdayCompany(name="Adobe", subdomain="adobe.wd5", tenant="adobe", site="external_experienced"),
    WorkdayCompany(name="HP", subdomain="hp.wd5", tenant="hp", site="ExternalCareerSite"),
    WorkdayCompany(name="Autodesk", subdomain="autodesk.wd1", tenant="autodesk", site="Ext"),
]

