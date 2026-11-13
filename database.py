
import sqlite3
import secrets


def lost_found():
    return sqlite3.connect("lost_found.db")


def create_table():
    reports = lost_found()
    cur = reports.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS lost_found_items (
            item_id INTEGER PRIMARY KEY,
            item_name TEXT,
            item_type TEXT,
            category TEXT,
            location TEXT,
            description TEXT,
            contact_name TEXT,
            contact_phone TEXT,
            status TEXT,
            date_reported TEXT
        )
    """)

    cur.execute("PRAGMA table_info(lost_found_items)")
    columns = [column[1] for column in cur.fetchall()]

    if "resolution_code" not in columns:
        cur.execute("""
            ALTER TABLE lost_found_items
            ADD COLUMN resolution_code TEXT
        """)

    reports.commit()
    reports.close()


create_table()


def insert_reports(
    item_name,
    item_type,
    category,
    location,
    description,
    contact_name,
    contact_phone,
    status,
    date_reported
):
    reports = lost_found()
    curr = reports.cursor()

    curr.execute("""
        SELECT 1 FROM lost_found_items
        WHERE LOWER(TRIM(item_name)) = LOWER(TRIM(?))
        AND item_type = ?
        AND category = ?
        AND location = ?
        AND description = ?
        AND contact_name = ?
        AND contact_phone = ?
        AND status = ?
        AND date_reported = ?
    """, (
        item_name, item_type, category, location,
        description, contact_name, contact_phone,
        status, date_reported
    ))

    if curr.fetchone():
        reports.close()
        return None

    while True:
        resolution_code = "REP-" + secrets.token_hex(3).upper()

        curr.execute("""
            SELECT 1 FROM lost_found_items
            WHERE resolution_code = ?
        """, (resolution_code,))

        if not curr.fetchone():
            break

    curr.execute("""
        INSERT INTO lost_found_items (
            item_name,
            item_type,
            category,
            location,
            description,
            contact_name,
            contact_phone,
            status,
            date_reported,
            resolution_code
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        item_name,
        item_type,
        category,
        location,
        description,
        contact_name,
        contact_phone,
        status,
        date_reported,
        resolution_code
    ))

    reports.commit()
    reports.close()

    return resolution_code


def get_reports():
    reports = lost_found()
    cur = reports.cursor()

    cur.execute("""
        SELECT * FROM lost_found_items
        WHERE status = 'Open'
        ORDER BY item_id DESC
    """)

    data = cur.fetchall()
    reports.close()

    return data


def resolve_report(resolution_code):
    reports = lost_found()
    cur = reports.cursor()

    cur.execute("""
        UPDATE lost_found_items
        SET status = 'Resolved'
        WHERE resolution_code = ?
        AND status = 'Open'
    """, (resolution_code.strip().upper(),))

    updated = cur.rowcount

    reports.commit()
    reports.close()

    return updated > 0
