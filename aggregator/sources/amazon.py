"""Amazon Jobs source connector.

Ingests public software and technology job postings directly from Amazon's
official careers API (https://www.amazon.jobs) without authentication.
"""

import logging
from aggregator.config.sources import SourceConfig
from aggregator.sources.base import BaseJobSource, SourceError

logger = logging.getLogger(__name__)

AMAZON_SEARCH_URL = "https://www.amazon.jobs/en/search.json"
TECH_CATEGORIES = [
    "software-development",
    "solutions-architect",
    "systems-quality-engineering",
    "data-science",
]
MAX_RESULTS_PER_CATEGORY = 100


class AmazonSource(BaseJobSource):
    """Collects engineering and technology roles directly from Amazon India."""

    def __init__(self, config: SourceConfig) -> None:
        super().__init__(config)
        self.session.headers.update({
            "User-Agent": "JobsForIndia-Aggregator/1.0 (https://jobsforindia.local)"
        })

    def collect_jobs(self) -> list[dict]:
        """Collect active tech jobs from Amazon India."""
        all_jobs: list[dict] = []
        seen_ids: set[str] = set()

        logger.info("[Amazon] Querying Amazon India tech career endpoints...")

        for category in TECH_CATEGORIES:
            try:
                params = {
                    "country": "IND",
                    "category": category,
                    "result_limit": MAX_RESULTS_PER_CATEGORY,
                    "sort": "recent",
                }
                data = self._get(AMAZON_SEARCH_URL, params=params)
                if not isinstance(data, dict):
                    continue

                jobs = data.get("jobs", [])
                added_count = 0
                for j in jobs:
                    job_id = str(j.get("id_icims") or j.get("id") or "")
                    if job_id and job_id not in seen_ids:
                        seen_ids.add(job_id)
                        j["_source_type"] = "amazon"
                        j["_company_name"] = "Amazon"
                        all_jobs.append(j)
                        added_count += 1

                logger.debug("[Amazon] Category '%s': %d jobs added", category, added_count)
            except Exception as e:
                logger.warning("[Amazon] Could not fetch category '%s': %s", category, e)
                continue

        logger.info("[Amazon] Total verified Amazon India jobs collected: %d", len(all_jobs))
        return all_jobs

