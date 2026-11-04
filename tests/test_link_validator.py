import datetime
import pytest
from aggregator.processing.link_validator import filter_by_ttl, prune_dead_ats_links
from aggregator.db import init_db, mark_jobs_closed, expire_stale_jobs_in_db, get_active_jobs_from_db


def test_filter_by_ttl():
    today = datetime.date.today()
    fresh_date = (today - datetime.timedelta(days=10)).isoformat()
    stale_date = (today - datetime.timedelta(days=150)).isoformat()

    jobs = [
        {"job_id": "1", "title": "Fresh Job", "posted_date": fresh_date},
        {"job_id": "2", "title": "Stale Job", "posted_date": stale_date},
        {"job_id": "3", "title": "Undated Job"},
    ]

    valid, expired = filter_by_ttl(jobs, max_age_days=120)
    assert expired == 1
    assert len(valid) == 2
    assert {j["job_id"] for j in valid} == {"1", "3"}


def test_db_mark_jobs_closed_and_expire(tmp_path):
    db_file = str(tmp_path / "test.db")
    conn = init_db(db_file)
    today = datetime.date.today().isoformat()
    old_date = "2020-01-01"

    with conn:
        conn.execute(
            "INSERT INTO jobs (job_id, title, posted_date, status) VALUES ('j1', 'Dev', ?, 'active')",
            (today,),
        )
        conn.execute(
            "INSERT INTO jobs (job_id, title, posted_date, status) VALUES ('j2', 'QA', ?, 'active')",
            (today,),
        )
        conn.execute(
            "INSERT INTO jobs (job_id, title, posted_date, status) VALUES ('j3', 'Old', ?, 'active')",
            (old_date,),
        )

    # 1. Test mark_jobs_closed
    updated = mark_jobs_closed({"j1"}, db_path=db_file)
    assert updated == 1

    # 2. Test expire_stale_jobs_in_db
    expired = expire_stale_jobs_in_db(max_age_days=120, db_path=db_file)
    assert expired == 1

    # Active remaining should only be j2
    active = get_active_jobs_from_db(db_path=db_file)
    assert len(active) == 1
    assert active[0]["job_id"] == "j2"
